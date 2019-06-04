#!/bin/bash

#This script should be run under root user
#This script should be run from the hypervisor

PoolId=8a99f9a969d97b74016a3f9defe77d37

backup(){

logit "Starting Back up process"

ssh undercloud-0 " 
	yum -y install mariadb ;
	cp /var/lib/config-data/puppet-generated/mysql/root/.my.cnf .;
	mkdir /backup;
	chown stack: /backup;
	mysqldump --opt --all-databases > /root/undercloud-all-databases.sql;
	cd /backup;
	tar --xattrs --ignore-failed-read -vcf \
	    undercloud-backup-`date +%F`.tar \
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
logit "Backup process has been completed" 
}

restore(){

ssh undercloud-0 "
	subscription-manager register --serverurl=https://subscription.rhn.stage.redhat.com --username=qa-automation --password=qa-automation --auto-attach;
	subscription-manager attach --pool=$PoolId;
	subscription-manager repos --disable=*;
	subscription-manager repos --enable=rhel-7-server-rpms --enable=rhel-7-server-extras-rpms --enable=rhel-7-server-rh-common-rpms --enable=rhel-ha-for-rhel-7-server-rpms --enable=rhel-7-server-openstack-14-rpms;
	yum update -y;
	reboot;
	"



}


logit(){
     echo $(date) $1
}


main(){
    backup
}

main
