#!/bin/bash

#This script should be run under root user
#This script should be run from the hypervisor

PoolId=8a99f9a969d97b74016a3f9defe77d37

backup_undercloud(){

logit "Starting Undercloud-0 Back up process"

ssh undercloud-0 " 
	yum -y install mariadb ;
	cp /var/lib/config-data/puppet-generated/mysql/root/.my.cnf .;
	mkdir /backup;
	chown stack: /backup;
	mysqldump --opt --all-databases > /root/undercloud-all-databases.sql;
	cd /backup;
	tar --xattrs --ignore-failed-read -vcf \
	    undercloud-backup.tar \
	    /etc \
	    /var/log \
	    /var/lib/glance \
	    /var/lib/certmonger \
	    /var/lib/registry \
	    /var/lib/config-data \
	    /srv/node \
	    /root \
	    /home/stack;
	"
logit "Backup undercloud-0 process has been completed" 
}

restore_undercloud(){


logit "Starting restore up process"
ssh undercloud-0 "
	subscription-manager register --serverurl=https://subscription.rhn.stage.redhat.com --username=qa-automation --password=qa-automation --auto-attach;
	subscription-manager attach --pool=$PoolId;
	subscription-manager repos --disable=*;
	subscription-manager repos --enable=rhel-7-server-rpms --enable=rhel-7-server-extras-rpms --enable=rhel-7-server-rh-common-rpms --enable=rhel-ha-for-rhel-7-server-rpms --enable=rhel-7-server-openstack-14-rpms;
	yum update -y;
	reboot;
	"
logit "Waiting 30 seconds for reboot to occur"
sleep 30
ssh undercloud-0 "
	yum install -y ntp
	systemctl start ntpd
	systemctl enable ntpd
	ntpdate pool.ntp.org
	systemctl restart ntpd
	yum install -y mariadb mariadb-server
	systemctl start mariadb
	mysql -uroot -e"set global max_allowed_packet = 1073741824;"
	tar -xvC / -f undercloud-backup.tar etc/my.cnf.d/server.cnf
	tar -xvC / -f undercloud-backup.tar root/undercloud-all-databases.sql
	mysql -u root < /root/undercloud-all-databases.sql
	tar -xvf undercloud-backup.tar root/.my.cnf
	OLDPASSWORD=$(sudo cat root/.my.cnf | grep -m1 password | cut -d'=' -f2 | tr -d "'")
	mysqladmin -u root password "$OLDPASSWORD"
	rmdir root
	mysql -e 'select host, user, password from mysql.user;'
	HOST="192.0.2.1"
	USERS=$(mysql -Nse "select user from mysql.user WHERE user != \"root\" and host = \"$HOST\";" | uniq | xargs)
	for USER in $USERS ; do mysql -e "drop user \"$USER\"@\"$HOST\"" || true ;done
	mysql -e 'flush privileges'
	useradd stack
	passwd stack
	echo "stack ALL=\(root\) NOPASSWD:ALL" | tee -a /etc/sudoers.d/stack
	chmod 0440 /etc/sudoers.d/stack
	tar -xvC / -f undercloud-backup.tar home/stack
	yum -y install policycoreutils-python
	tar --xattrs -xvC / -f undercloud-backup-$TIMESTAMP.tar var/lib/glance
	tar --xattrs -xvC / -f undercloud-backup-$TIMESTAMP.tar srv/node
	tar -xvC / -f undercloud-backup-$TIMESTAMP.tar etc/pki/instack-certs/undercloud.pem
	tar -xvC / -f undercloud-backup-$TIMESTAMP.tar etc/pki/ca-trust/source/anchors/*
	restorecon -R /etc/pki
	semanage fcontext -a -t etc_t "/etc/pki/instack-certs(/.*)?"
	restorecon -R /etc/pki/instack-certs
	update-ca-trust extract
	su - stack
	sudo yum install -y python-tripleoclient
	openstack undercloud install
	"
logit "Restore is done"
}

create_machine(){
	
	curl -o /tmp/rhel7-guest-official.qcow2 http://10.12.50.1/pub/rhel-7-x86_64-latest.qcow2
	qemu-img create -f qcow2 /tmp/rhel7-guest.qcow2 120G
	yum -y install libguestfs-xfs
	virt-resize --expand /dev/sda1 /tmp/rhel7-guest-official.qcow2 /tmp/rhel7-guest.qcow2
	qemu-img create -f qcow2 -b /tmp/rhel7-guest.qcow2 /var/lib/libvirt/images/undercloud.qcow2
	virt-customize -a undercloud.qcow2 --root-password password:redhat --uninstall cloud-init



}

restore_unedrcloud(){


	virsh shutdown undercloud-0
	virsh snapshot-revert --domain undercloud-0 --snapshotname underlcoud-clean.xml 
	virsh start undercloud-0

}

logit(){
     echo $(date) $1
}


main(){
    backup_undercloud
    restore_undercloud
    restore_undercloud

}

main
