from check_gnocchi_service import *

def RHELOSP_6844_test():
    res = 1
    '''
    # Edit the pipeline file
    res = edit_pipeline(pipeline_file, gnocchi_pipeline_input)
    if res != 0:
        return 1

    #edit the gnocchi_source file
    res = edit_source(gnocchi_resources_file, gnocchi_resources_input)
    if res != 0:
        return 1

    #Restart the processes
    for proc in proc_list:
        res = restart_process(proc)
        if res != 0:
            return 1
    '''

    #Create new instance
    res, id = create_new_resource("instance")
    if res !=1:
        resource_id = id
        res = 0
    else:
        return 1

    time.sleep(60)

    #Check that the resource is added to metric list
    res = test_new_resource("instance", resource_id)
    if res != 0:
        return 1

    #Check the measures of the resource
    for val in instance_value_check:
        res = test_values_assigned(resource_id,val)
        if res[0] != 0:
            return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_6844_test()
    if res == 0:
        print("RHELOSP_6844 Finished successfully")
    else:
        print("RHELOSP_6844 failed")
    sys.exit(res)