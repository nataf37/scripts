from check_gnocchi_service import *


def RHELOSP_6842_pretest():
    # Edit the pipeline file
    res = edit_pipeline(pipeline_file, gnocchi_pipeline_volume_input)
    if res != 0:
        return 1

    # edit the gnocchi_source file
    res = edit_source(gnocchi_resources_file, gnocchi_resources_volume_input)
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
    res = RHELOSP_6842_pretest()
    if res == 0:
        print("Finished successfully")