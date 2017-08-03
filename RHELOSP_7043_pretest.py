from check_gnocchi_service import *

def RHELOSP_7043_pretest():
    # change pipeline
    res = edit_pipeline(pipeline_file, gnocchi_pipeline_instance_input)
    if res != 0:
        return 1
    # change gnocchi resource file
    res = edit_source(gnocchi_resources_file, gnocchi_resources_instance_input)
    if res != 0:
        return 1

    '''
    # Remove all the existing instances
    # 1.Get the list of existing instances
    instance_list = find_resources('instance')
    # 2. Remove the instances
    for ins in instance_list:
        res = remove_resource(ins, 'instance')
        if res != 0:
            print("Couldn't delete %s with id %s" % ('instance', ins))
            return 1
            
    '''
    # Restart the processes
    for proc in proc_list:
        res = restart_process(proc)
        if res != 0:
            return 1
    return 0

if __name__ == "__main__":
    res = RHELOSP_7043_pretest()
    if res == 0:
        print("RHELOSP_7043_pretest Finished successfully")
    else:
        print("RHELOSP_7043_pretest failed")
    sys.exit(res)