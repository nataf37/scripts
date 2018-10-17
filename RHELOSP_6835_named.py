from check_gnocchi_service import *

def RHELOSP_6835_test():
    res = 1
    '''
    change_to_root()
    # Edit the pipeline file
    res = edit_pipeline(pipeline_file, gnocchi_pipeline_input)
    if res != 0:
        print("Couldn't change the file %s"%pipeline_file)
        return 1

    #edit the gnocchi_source file
    res = edit_source(gnocchi_resources_file, gnocchi_resources_input)
    if res != 0:
        print("Couldn't change the file %s" % gnocchi_resources_file)
        return 1

    change_from_root()

    #Restart the processes
    for proc in proc_list:
        res = restart_process(proc)
        if res != 0:
            print("Couldn't restart the process %s"%proc)
            return 1
    '''

    #Create new instance
    res_name = str(int(1000.0*random()))
    res, id = create_new_resource("instance", res_name)
    print("resource_id=%s"%id)
    if res !=1:
        resource_id = id
    else:
        return 1

    time.sleep(300)

    #Check that the resource is added to metric list
    res = test_new_resource("instance", resource_id)
    if res != 0:
        return 1

    #Check the measures of the resource
    for val in instance_values_assigned_new:
        res = test_values_assigned(resource_id,val)
        if res[0] != 0:
            return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_6835_test()
    if res == 0:
        print("RHELOSP_6835 Finished successfully")
    else:
        print("RHELOSP_6835 failed")
    sys.exit(res)
