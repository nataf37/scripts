from check_gnocchi_service import *
import sys

def RHELOSP_6841_pretest():
    # Edit the pipeline file
    res = edit_pipeline(pipeline_file, gnocchi_pipeline_image_input)
    if res != 0:
        return 1

    # edit the gnocchi_source file
    res = edit_source(gnocchi_resources_file, gnocchi_resources_image_input)
    if res != 0:
        return 1

    # Disable non_metric in ceilometer_conf
    res = disable_non_metric_meters("True")
    if res != 0:
        return 1

    # Restart the processes
    for proc in proc_list:
        res = restart_process(proc)
        if res != 0:
            return 1


    return 0

if __name__ == "__main__":
    res = RHELOSP_6841_pretest()
    if res == 0:
        print("RHELOSP_6841_pretest Finished successfully")
    else:
        print("RHELOSP_6841_pretest failed")
    sys.exit(res)