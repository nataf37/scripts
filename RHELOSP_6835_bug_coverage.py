from check_gnocchi_service import *

def RHELOSP_6835_bug_coverage_test():
    res = 1


    #Create new instance
    res, id = create_new_resource("instance")
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
    for val in instance_values_assigned_bug_coverage:
        res = test_values_assigned(resource_id,val)
        if res[0] != 0:
            return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_6835_bug_coverage_test()
    if res == 0:
        print("RHELOSP_6835_bug_coverage Finished successfully")
    else:
        print("RHELOSP_6835_bug_coverage failed")
    sys.exit(res)
