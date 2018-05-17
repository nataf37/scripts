from check_gnocchi_service import *

def RHELOSP_34681_test():
    res = 1

    #0. Operate under admin user
    res = switch_context(orig_rc)
    if res != 0:
        return 1

    #1. Get resource_id of admin user
    res, admin_id = get_resource_id("user", "admin")
    if res != 1:
        res = 0
    else:
        return 1

    #2. Get resource_id of demo user
    res, demo_id = get_resource_id("user", "demo")
    if res != 1:
        res = 0
    else:
        return 1

    #3. Find demo metrics under admin user
    res = find_metrics(demo_id, "instance")
    if res[0] != 0:
        return 1
    else:
        print "Found demo metrics under admin!"
        res = 0

    return 0



if __name__ == "__main__":
    res = RHELOSP_34681_test()
    if res == 0:
        print("RHELOSP_34681_test Finished successfully")
    else:
        print("RHELOSP_34681_test failed")
    sys.exit(res)