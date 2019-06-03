#!/bin/bash

#This script should be run under root user
#This script should be run from the hypervisor

backup(){

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
}

restore(){
}


main(){
backup
}

main
