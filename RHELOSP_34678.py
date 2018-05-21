from check_gnocchi_service import *

def RHELOSP_34678_test():
    res = 1

    #0. Operate under admin user
    res = switch_context(orig_rc)
    if res != 0:
        return 1

    #1. Create new image
    res, id = create_new_resource("image", "AdminImage")
    if res != 1:
        resource_id = id
        res = 0
    else:
        return 1

    time.sleep(60)

    # Check that the resource is added to metric list
    res = test_new_resource("image", resource_id)
    if res != 0:
        return 1

    # Check the measures of the resource
    for val in image_value_check:
        res = test_values_assigned(resource_id, val)
        if res[0] != 0:
            return 1

    return 0



if __name__ == "__main__":
    res = RHELOSP_34678_test()
    if res == 0:
        print("RHELOSP_34678_test Finished successfully")
    else:
        print("RHELOSP_34678_test failed")
    sys.exit(res)