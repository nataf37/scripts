from check_gnocchi_service import *

def RHELOSP_40410_test():
    res = 1


    #Create new image
    res, id = create_new_resource("instance", "Test_40410")
    print("resource_id=%s"%id)
    if res !=1:
        resource_id = id
    else:
        return 1

    time.sleep(60)

    #Check that the resource is added to metric list
    res = test_new_resource("instance", resource_id)
    if res != 0:
        return 1

    if res == 0:
        open("/tmp/RHELOSP_40410", "w+")

    #Check the metrics of the resource
    metrics_list = ['cpu', 'cpu_util']
    for val in metrics_list:
        res = test_values_assigned(resource_id,val)
        if res[0] != 0:
            return 1
    open("/tmp/RHELOSP_40412", "w+")
    return 0

if __name__ == "__main__":
    res = RHELOSP_40410_test()
    if res == 0:
        print("RHELOSP_40410_12 Finished successfully")
    else:
        print("RHELOSP_40410_12 failed")
    sys.exit(res)
