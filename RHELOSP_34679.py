from check_gnocchi_service import *

def RHELOSP_34679_test():
    res = 1

    #0. Operate under demo user
    res = switch_context(demo_rc)
    if res != 0:
        return 1

    #1. Create new instance
    res, id = create_new_resource("instance", "DemoInstance")
    if res != 1:
        resource_id = id
        res = 0
    else:
        return 1

    time.sleep(60)

    # Check that the resource is added to metric list
    res = test_new_resource("instance", resource_id)
    if res != 0:
        return 1

    # Check the measures of the resource
    for val in instance_value_check:
        res = test_values_assigned(resource_id, val)
        if res != 0:
            return 1

    return 0



if __name__ == "__main__":
    res = RHELOSP_34679_test()
    if res == 0:
        print("RHELOSP_34679_test Finished successfully")
    else:
        print("RHELOSP_34679_test failed")
    sys.exit(res)