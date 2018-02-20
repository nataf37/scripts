from check_gnocchi_service import *

def RHELOSP_33116_test():
    res = 1

    #Create new instance
    res, id = create_new_resource("instance")
    print("resource_id=%s"%id)
    if res !=1:
        resource_id = id
    else:
        return 1

    print("Waiting for 5 min for the metrics to appear")
    time.sleep(300)

    #Check that the resource is added to metric list
    res = test_new_resource("instance", resource_id)
    if res != 0:
        return 1

    #Check the memory bandwidth measures of the resource
    for val in mbm_measures:
        res = test_values_assigned(resource_id,val)
        if res == 0:
            print("The measures aren't supposed to be there!")
            return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_33116_test()
    if res == 0:
        print("RHELOSP_33116 Finished successfully")
    else:
        print("RHELOSP_33116 failed")
    sys.exit(res)
