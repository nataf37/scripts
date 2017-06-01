from check_gnocchi_service import *

def RHELOSP_7043_test():
    res = 1
    '''
    # change pipeline
    res = edit_pipeline(pipeline_file, gnocchi_pipeline_instance_input)
    if res != 0:
        return 1
    # change gnocchi resource file
    res = edit_source(gnocchi_resources_file, gnocchi_resources_instance_input)
    if res != 0:
        return 1

    # Remove all the existing instances
    # 1.Get the list of existing instances
    instance_list = find_resources('instance')
    # 2. Remove the instances
    for ins in instance_list:
        res = remove_resource(ins, 'instance')
        if res != 0:
            print("Couldn't delete %s with id %s" % ('instance', ins))
            return 1

    # Restart the processes
    for proc in proc_list:
        res = restart_process(proc)
        if res != 0:
            return 1
    '''

    # Create new instance
    res, id = create_new_resource("instance")
    if res != 1:
        resource_id = id
        res = 0
    else:
        return 1

    #Rename the instance
    new_ins_name = 'InstanceGnocchiTest7043'
    res = rename_resource(resource_id, 'instance', new_ins_name)
    if res !=0:
        print("Couldn't rename resource %s to %s"%(resource_id, new_ins_name))
        return 1

    #Wait several polling cycles
    print('Waiting for instance to update in metric. Need to wait for 1 hour')
    for i in xrange(60):
        time.sleep(60)
        print('Waiting for update from nova. %d minutes left'%i)


    #Check the new name
    new_name = show_resource('instance', resource_id)
    if new_name != new_ins_name:
        print("The name of metric %s isn't corresponding to the name of instance %s"%(new_name,new_ins_name))
        return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_7043_test()
    if res == 0:
        print("Finished successfully")