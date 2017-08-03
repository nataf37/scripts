from check_gnocchi_service import *

def RHELOSP_6835_pretest():

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

    return 0

if __name__ == "__main__":
    res = RHELOSP_6835_pretest()
    if res == 0:
        print("RHELOSP_6835_pretest Finished successfully")
    else:
        print("RHELOSP_6835_pretest failed")
    sys.exit(res)