#!/bin/bash

easy_install pip;easy_install pip3
pip install virtualenv
yum install git -y
virtualenv ~/.venv
source ~/.venv/bin/activate
git clone https://github.com/redhat-openstack/infrared
pip install -U pip
cd infrared
pip install .

##Clean UP##
ir virsh -vv --host-address seal30.qa.lab.tlv.redhat.com --host-key ~/.ssh/id_rsa --cleanup true

##Provision 13/14##
ir virsh -vv --host-address=seal30.qa.lab.tlv.redhat.com --host-key=~/.ssh/id_rsa --topology-nodes=undercloud:1,controller:2,compute:2,ceph:2 -e override.undercloud.cpu=8 -e override.undercloud.memory=24576 -e override.undercloud.disk.disk1.size=65 --image-url http://ikook.tlv.redhat.com/gen_images/cloud/rhel-guest-image-7.6-latest.x86_64.qcow2

##UnderCloud Installlation##
ir tripleo-undercloud -vv --mirror tlv --version 14 --build passed_phase2 --images-task rpm --ssl=yes --config-options "DEFAULT.enable_telemetry=true" > uc-14.log 2>&1 

##OverCloud Installation##
ir tripleo-overcloud -vv --version 14 --introspect yes --tagging yes --deploy yes --containers yes --deployment-files virt --overcloud-ssl yes > oc-14.log 2>&1 &

infrared
#infrared virsh --host-address <hypervisor_ip> --host-key <private_ssh_key> --topology-nodes <topology> -e <arguments>


#Create an image:

wget http://ikook.tlv.redhat.com/gen_images/cloud/CentOS-7-x86_64-GenericCloud.qcow2

openstack image create --disk-format qcow2 --container-format bare --public --file CentOS-7-x86_64-GenericCloud.qcow2 centos-7-image

openstack flavor create --public m1.extra_tiny --id auto --ram 256 --disk 0 --vcpus 1

openstack server create --image centos-7-image --flavor m1.extra_tiny  MyFirstInstance (--nic net-id=<NEt ID> in case of undercloud)
												    |openstack network list|


