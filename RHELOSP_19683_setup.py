from check_gnocchi_service import *

def RHELOSP_19683_setup():
    #Instance
    # Edit the pipeline file
    res = edit_pipeline(pipeline_file, gnocchi_pipeline_input)
    if res != 0:
        return 1

    # edit the gnocchi_source file
    res = edit_source(gnocchi_resources_file, gnocchi_resources_input)
    if res != 0:
        return 1

    # Restart the processes
    for proc in proc_list:
        res = restart_process(proc)
        if res != 0:
            return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_19683_setup()
    if res == 0:
        print("RHELOSP_19683 Finished successfully")
    else:
        print("RHELOSP_19683 failed")
    sys.exit(res)