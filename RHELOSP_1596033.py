from check_gnocchi_service import *

def RHELOSP_1596033_test():
    res = 1
    met_id_list = []
    #get list of all metrics
    res = get_met_list(met_id_list)
    if res != 0:
        print("There was a problem with metric list")
        return 1
    else:
        res = 0


    #Check that all the metrics have measures
    for metric_id in met_id_list:
        res1 = get_measures_by_id(metric_id)
        if res1 == 1:
            print("Measures od metric %s not found!"%metric_id)


    return res


if __name__ == "__main__":
    res = RHELOSP_1596033_test()
    if res == 0:
        print("RHELOSP_1596033_test Finished successfully")
    else:
        print("RHELOSP_1596033_test failed")
    sys.exit(res)