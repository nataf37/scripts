import glob
import os
import subprocess
import time
import fileinput
from definitions import *
import sys


def create_new_resource(resource_type, resource_name=""):
    if resource_type == "instance":
        if resource_name == "":
            resource_name = "MyFirstInstance"

        (res, metric_id) = resource_exists('server',resource_name)
        if res == 0:
            print "Instance %s already exists" % resource_name
            return 0, metric_id

        # build image
        res = create_new_resource("image")
        # build flavor
        if res != 1:
            res = create_new_resource("flavor")
            if res != 1:

                p = subprocess.Popen(
                    "openstack server create --image centos-7-image --flavor m1.extra_tiny  %s" % resource_name,
                    stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                if err is None:
                    if "Missing value" in output:
                        print("Missing value auth-url required for auth plugin password")
                        return 1, ''
                    else:
                        print("Instance is built!")
                        for line in output.splitlines():
                            if "id" in line:
                                id_arr = line.split('|')
                                metric_id = id_arr[2].strip()
                                return 0, metric_id
                        print("Couldn't find instance id")
                        return 1,''
                else:
                    print("There was error", err)
                    return 1, ''
            else:
                print("Couldn't create flavor")
                return 1,''
        else:
            print("Couldn't create image")
            return 1,''

        print("Error building instance")
        return 1,''


    elif resource_type == "image":
        if resource_name == "":
            resource_name = "centos-7-image"
        # get image
        p = subprocess.Popen("wget %s" % image_source, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if err == None:
            print("source ~/stackrc")
            p1 = subprocess.Popen('source ~/stackrc',stdout=subprocess.PIPE, shell=True)
            (output, err) = p1.communicate()
            if err != None:
                print("Couldn't find ~/stackrc")
                print(output)
                return 1,''

            (res, metric_id) = resource_exists('image', resource_name)
            if res == 0:
                print "Image %s already exists" % resource_name
                return 0, metric_id

            print("openstack image create --disk-format qcow2 --container-format bare --public --file %s %s" %(image_name,resource_name))
            p2 = subprocess.Popen(
                "openstack image create --disk-format qcow2 --container-format bare --public --file %s %s" %(image_name,resource_name),
                stdout=subprocess.PIPE, shell=True)
            (output, err) = p2.communicate()
            if err is None:
                if "Missing value" in output:
                    print("Missing value auth-url required for auth plugin password")
                    return 1,''
                else:
                    print("Image is built!")
                    for line in output.splitlines():
                        if "id" in line:
                            id_arr = line.split('|')
                            metric_id = id_arr[2].strip()
                            print("Here is the id: ", metric_id)
                            return 0, metric_id
                    return 1,''
            else:
                print("Error building image")
                return 1,''

    elif resource_type == "flavor":
        if resource_name == "":
            resource_name = "m1.extra_tiny"

        (res, metric_id) = resource_exists('flavor',resource_name)
        if res == 0:
            print "Flavor %s already exists"%resource_name
            return 0, metric_id

        p = subprocess.Popen(
            "openstack flavor create --public %s --id auto --ram 256 --disk 0 --vcpus 1" % resource_name,
            stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if err is None:
            if "Missing value" in output:
                print("Missing value auth-url required for auth plugin password")
                return 1,''
            else:
                print("Flavor is built!")
                for line in output.splitlines():
                    if "id" in line:
                        id_arr = line.split('|')
                        metric_id = id_arr[2].strip()
                        print("Resource id is %s"%metric_id)
                        return 0, metric_id
                print("Error building flavor")
                return 1,''

        else:
            print("Error building flavor")
            return 1,''

    elif resource_type == "volume":
        if resource_name == "":
            resource_name = "my-volume"

        (res, metric_id) = resource_exists('volume',resource_name)
        if res == 0:
            print "Volume %s already exists"%resource_name
            return 0, metric_id

        p = subprocess.Popen("openstack volume create --size 2 %s" % resource_name, stdout=subprocess.PIPE,
                             shell=True)
        (output, err) = p.communicate()
        if err is None:
            if "Missing value" in output:
                print("Missing value auth-url required for auth plugin password")
                return 1,''
            else:
                print("Volume is built!")
                for line in output.splitlines():
                    if "id" in line and not "None" in line:
                        id_arr = line.split('|')
                        metric_id = id_arr[2].strip()
                        print("Resource id is %s" % metric_id)
                        return 0, metric_id
                else:
                    return 1,''

    elif resource_type == "network":
        if resource_name == "":
            resource_name = "FakeNetGnocchi"

        (res, metric_id) = resource_exists('network',resource_name)
        if res == 0:
            print "Network %s already exists"%resource_name
            return 0, metric_id

        p = subprocess.Popen("openstack network create %s" % resource_name, stdout=subprocess.PIPE,
                             shell=True)
        (output, err) = p.communicate()
        if err is None:
            if "Missing value" in output:
                print("Missing value auth-url required for auth plugin password")
                return 1,''
            else:
                print("Network is built!")
                for line in output.splitlines():
                    if "id" in line:
                        id_arr = line.split('|')
                        metric_id = id_arr[2].strip()
                        print("Resource id is %s" % metric_id)
                        return 0, metric_id
                else:
                    return 1,''
        else:
            print("Error building network")
            return 1,''
    else:
        print("Not known resource %s" % resource_type)
        return 1,''

def alarm_type_exists(alarm_type):
    print("ceilometer help")
    p = subprocess.Popen("ceilometer help", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1, ''
        else:
            for line in output.splitlines():
                print(line)
                if alarm_type in line:
                    id_arr = line.split('|')
                    metric_id = id_arr[1].strip()
                    print("Resource id is %s" % metric_id)
                    return 0, metric_id
            print("Didn't find resource in the list")
            return 1, ''
    print("There was a problem with list", err)
    return 1, ''

def resource_exists(resource_type, resource_name):
    print("openstack %s list"%resource_type)
    p = subprocess.Popen("openstack %s list"%resource_type,stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                print(line)
                if resource_name in line:
                    id_arr = line.split('|')
                    metric_id = id_arr[1].strip()
                    print("Resource id is %s"%metric_id)
                    return 0, metric_id
            print("Didn't find resource in the list")
            return 1,''
    print("There was a problem with list",err)
    return 1, ''

def ceilometer_event_list():
    print("ceilometer event-list")
    event_name ="identity.domain.created"
    p = subprocess.Popen("ceilometer event-list",stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                print(line)
                if event_name in line:
                    print 'Event %s found!'%event_name
                    return 0, ''
            print("Didn't find %s in the list"%event_name)
            return 1,''
    print("There was a problem with list",err)
    return 1, ''

def ceilometer_event_show():
    print("ceilometer event-list")
    event_name ="identity.domain.created"
    p = subprocess.Popen("ceilometer event-list",stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                print(line)
                if event_name in line:
                    id_arr = line.split('|')
                    metric_id = id_arr[1].strip()
                    print("Resource id is %s"%metric_id)

                    print("ceilometer event-show %s"%metric_id)
                    p = subprocess.Popen("ceilometer event-show %s"%metric_id, stdout=subprocess.PIPE, shell=True)
                    (output1, err1) = p.communicate()
                    if err1 is None:
                        if "Missing value" in output1:
                            print("Missing value auth-url required for auth plugin password")
                            return 1, ''
                        else:
                            for line1 in output1.splitlines():
                                print(line1)
                                if event_name in line1:
                                    id_arr1 = line1.split('|')
                                    ev_type = id_arr1[1].strip()
                                    if "event_type" in ev_type:
                                        print('Event %s exists'%event_name)
                                        return 0, ''
                            print("Didn't find event_type %s "%event_name)
                            return 1, ''
                    else:
                        print("Problem with event-show")
                        return 1, ''
            print("Didn't find %s in the list"%event_name)
            return 1,''
    print("There was a problem with list",err)
    return 1, ''

def check_openstack_event_type_list():
    print("ceilometer event-type-list")
    event_name ="image.update"
    p = subprocess.Popen("ceilometer event-type-list",stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                print(line)
                if event_name in line:
                    print 'Event type %s found!'%event_name
                    return 0, ''
            print("Didn't find %s in the list"%event_name)
            return 1,''
    print("There was a problem with type list",err)
    return 1, ''

def check_openstack_trait_list():
    event_name = "volume.create.start"
    print("ceilometer trait-description-list -e %s"%event_name)
    trait_name = "created_at"
    p = subprocess.Popen("ceilometer trait-description-list -e %s"%event_name,stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                print(line)
                if trait_name in line:
                    print 'Trait type %s found in %s!'%(trait_name,event_name)
                    return 0, ''
            print("Didn't find %s in the list"%event_name)
            return 1,''
    print("There was a problem with trait list",err)
    return 1, ''


def test_new_resource(resource_name, resource_id):
    if resource_name == "network":
        resource_name = 'instance_network_interface'
    p = subprocess.Popen("openstack metric resource list | grep %s" % resource_name, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1
        else:
            for line in output.splitlines():
                print(line)
                if resource_name in line:
                    id_arr = line.split('|')
                    metric_id = id_arr[1].strip()
                    if resource_id == metric_id:
                        print("The resource %s is in metric list" % resource_name)
                        return 0
            print("The resource %s is not found in metric list" % resource_id)
            return 1

        print("The resource %s is not found in metric list" % resource_name)
        return 1

    print('Problem with openstack metric resource list')
    return 1


def remove_resource(resource_id, resource_name):
    p = subprocess.Popen("openstack %s delete %s*" % (resource_name, resource_id), stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        return 0
    else:
        print("There was a problem deleting %s with id %s" % (resource_name, resource_id))
        return 1


def rename_resource(resource_id, resource_type, resource_name):
    if resource_type != 'instance':
        p = subprocess.Popen("openstack %s set --name %s %s" % (resource_type, resource_name, resource_id),
                             stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
    else:
        p = subprocess.Popen('nova update --name %s %s' % (resource_name, resource_id), stdout=subprocess.PIPE,
                             shell=True)
        (output, err) = p.communicate()
    if err is None:
        return 0
    else:
        print("There was a problem renaming %s with id %s" % (resource_type, resource_id))
        return 1


def find_resources(resource_name):
    resource_list = []
    p = subprocess.Popen("openstack metric resource list | grep %s" % resource_name, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                if resource_name in line:
                    id_arr = line.split('|')
                    metric_id = id_arr[1].strip()
                    resource_list.append(metric_id)
    return resource_list

def check_aodh_alarm(outline):
    counter = 0
    max_counter = len(aodh_alarm_list)
    for aodh_line in aodh_alarm_list:
        if aodh_line in outline:
            counter = counter + 1
        else:
            print outline
            print("Didn't find %s in the list" % aodh_line)
            return False
    if counter == max_counter:
        return True

def check_aodh_alarm_list(extracted_alarm):
    alarm_name="MyAlarm"
    alarm_type="test"
    res1=False
    print("aodh alarm create --name '%s' -t %s"%(alarm_name, alarm_type))

    p = subprocess.Popen("aodh alarm create --name '%s' -t %s"%(alarm_name, alarm_type),stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                #print(line)
                if extracted_alarm in line:
                    print 'This alarm: %s is not supposed to be in the list!'%extracted_alarm
                    return 1, ''

                if aodh_alarm_list[0] in line:
                    print line
                    res1 = check_aodh_alarm(line)

                if res1:
                    print("The aodh list os full, %s is not in it", extracted_alarm)
                    return 0, ''
            print "Didn't find the list"
            return 1, ''
    else:
        print("There was a problem with aodh list",err)
        return 1, ''

def show_resource(resource_type, resource_id):
    metric_name = ""
    if resource_type=="instance":
        look_for_name = "display_name"
    elif resource_type == 'image':
        look_for_name = "name"
    elif resource_type == "network":
        look_for_name = "instance_network_interface"
    p = subprocess.Popen("openstack metric resource show --type %s %s" % (resource_type, resource_id), stdout=subprocess.PIPE,
                         shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                print(line)
                if look_for_name in line:
                    #print("Display line: %s"%line)
                    id_arr = line.split('|')
                    metric_name = id_arr[2].strip()
    return metric_name


def test_values_assigned(resource_id, metric_name):
    print("openstack metric measures show --aggregation max --resource-id %s %s" % (resource_id,metric_name))
    p = subprocess.Popen("openstack metric measures show --aggregation max --resource-id %s %s" % (resource_id,metric_name),
                         stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                if line == "":
                    print("No measures of %s" % metric_name)
                    return 1
                else:
                    print("Found measures for %s" % metric_name)
                    return 0
    print("Problem getting measures for %s" % resource_id)
    return 1


def restart_process(process_name):
    p = subprocess.Popen("sudo -S systemctl restart %s" % process_name, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        print("%s restarted" % process_name)
        return 0
    else:
        print("Couldn't restart %s" % process_name)
        return 1


def check_process(process_name):
    output = subprocess.check_output(['ps', '-A'])
    if process_name in output:
        print("%s is up an running!" % process_name)
        return 0
    else:
        print("No %s in the list" % process_name)
        return 1

def check_httpd_process(process_name):
    p = subprocess.Popen("systemctl status httpd", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        for line in output.splitlines():
            if process_name in line:
                print("%s is up an running!" % process_name)
                return 0
            else:
                print("No %s in the list" % process_name)
                return 1

def check_openstack_service(service_name, service_type="metric"):
    p = subprocess.Popen("openstack service list", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                if service_name in line:
                    print("%s service is running in openstack" % service_name)
                    if service_type in line:
                        print("The type is %s" % service_type)
                        return 0
                    else:
                        print("The type isn't %s" % service_type)
                        return 1
    return 2

def check_openstack_endpoint(service_name, service_type="metric"):
    p = subprocess.Popen("openstack endpoint list", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                if service_name in line:
                    print("%s endpoint is found in openstack" % service_name)
                    if service_type in line:
                        print("The type is %s" % service_type)
                        return 0
                    else:
                        print("The type isn't %s" % service_type)
                        return 1
    return 1


def check_openstack_user(user_name):
    p = subprocess.Popen("openstack user list", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                if user_name in line:
                    print('%s user exists in openstack' % user_name)
                    return 0
    else:
        print("There is no user %s" % user_name)
        return 1


def check_system_process(process_name):
    p = subprocess.Popen("sudo -S systemctl status openstack-%s*" % process_name, stdout=subprocess.PIPE, shell=True)
    flag = False
    (output, err) = p.communicate()
    if err is None:
        if "Missing value" in output:
            print("Missing value auth-url required for auth plugin password")
            return 1,''
        else:
            for line in output.splitlines():
                if flag:
                    i += 1
                    if i == 2:
                        i = 0
                        if "active" in line:
                            print("%s process is active in openstack" % process_name)
                            return 0
                        else:
                            return 1
                else:
                    if process_name in line:
                        # print("%s process is running in openstack"%process_name)
                        flag = True
                        i = 0
    return 2


def edit_pipeline(pipeline_file, edit_fields):
    processing_source = False
    if os.path.isfile(pipeline_file):
        with open(pipeline_file, 'r') as pipefile:
            for line in pipefile:
                if edit_fields.split('\n')[4] in line:
                    print("The pipeline file already contains the fields")
                    return 0

    if os.path.isfile(pipeline_file):
        print("Trying to change %s"%pipeline_file)
        for line in fileinput.input(pipeline_file, inplace=1):
          if line.startswith('sources'):
              processing_source = True
          else:
            if processing_source:
              print(edit_fields)
              processing_source = False
          print line,
    else:
        print("Cannot open %s" % pipeline_file)
    return 0

def edit_source(source_file, edit_fields):
    processing_source = False
    if os.path.isfile(source_file):
        with open(source_file, 'r') as editfile:
            for line in editfile:
                if edit_fields.split('\n')[5] in line:
                    print("The gnocchi_resources file already contains the fields")
                    return 0

    if os.path.isfile(source_file):
        print("Trying to change %s"%source_file)
        for line in fileinput.input(source_file, inplace=1):
          if line.startswith('resources'):
              processing_source = True
          else:
            if processing_source:
              print(edit_fields)
              processing_source = False
          print line,
    else:
        print("Cannot open %s" % pipeline_file)
    return 0
'''
def edit_source(source_file, edit_fields):
    if os.path.isfile(source_file):
        target = open(source_file, 'r+')
        print("Opening file %s"%source_file)
        for line in target.readline():
            print(line)
            if "resources" in line:
                target.readline()
                target.write(edit_fields)
                target.close()
                return 0
    else:
        print("Cannot open %s" % source_file)
    return 1
'''

def disable_non_metric_meters(value):
    res = 1
    if os.path.isfile(ceilometer_conf):
        f = open(ceilometer_conf, 'r+')
        d = f.readlines()
        f.seek(0)
        for i in d:
            if "disable_non_metric_meters" not in i:
                f.write(i)
            else:
                f.write("disable_non_metric_meters=%s" % value)
                res = 0
        f.truncate()
        f.close()
        if res == 1:
            print("Couldn't find disable_non_metric_meters string in %s" % ceilometer_conf)
            return 0
        return res
    print("Couldn't open the %s file" % ceilometer_conf)
    return res


import os.path
import subprocess

password_for_sudo = 'redhat'

def started_as_root():
    if subprocess.check_output('whoami').strip() == 'root':
        return True
    return False

def runing_with_root_privileges():
    print 'i am root'

def runing_as_user():
    print 'i am not root'

def change_to_root():
    if started_as_root():
        print 'calling the function under root'
        runing_with_root_privileges()
    else:
        print "Need to change to root"
        current_script = os.path.realpath(__file__)
        os.system('echo %s|sudo -S python %s' % (password_for_sudo, current_script))

def change_from_root():
    if started_as_root():
        print('Changing from root')
        current_script = os.path.realpath(__file__)
        os.system('echo %s|python %s' % (password_for_sudo, current_script))
    else:
        runing_as_user()


if __name__ == '__main__':
    change_to_root()