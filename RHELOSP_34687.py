from check_gnocchi_service import *

def RHELOSP_34687_test():
    res = 1

    #1. Operate under admin user
    res = switch_context(orig_rc)
    if res != 0:
        return 1

    #2. Get resource_id of demo user
    res, demo_id = get_resource_id("user", "demo")
    if res != 1:
        res = 0
    else:
        return 1

    #3. Check that there is no demo user
    field = "user"
    proj_value = "demo"
    user_value = "demo2"
    print("Checking that there is no %s in the list of %s" % (user_value, field))
    res = check_field(field, user_value)

    if res[0] !=0:
        return 1

    #4. Create demo user
    if res[1] != 'Got':
        print("Creating %s %s" % (user_value, field))
        res = build_field(field, user_value)

        if res[0] !=0:
            return 1

    #5. Add demo2 to user role
    role = "user"
    res = add_role(proj_value, user_value, role)

    if res[0] != 0:
        return 1

    #6. Create new demo2rc file, replace pass, project and user
    res = copy_file(orig_rc, demo2_rc)
    if res[0] !=0:
        return 1

    res = change_file(demo_rc, 'OS_USERNAME', user_value)
    if res[0] !=0:
        return 1

    res = change_file(demo_rc, 'OS_PASSWORD', user_value)
    if res[0] !=0:
        return 1

    res = change_file(demo_rc, 'OS_PROJECT_NAME', proj_value)
    if res[0] !=0:
        return 1

    #7. Operate under demo2 user
    res = switch_context(demo2_rc)
    if res != 0:
        return 1


    #8. Find demo metrics under demo2 user. They must be seen since it's the same project
    res = find_metrics(demo_id, "instance")
    if res[0] != 0:
        return 1
    else:
        print "Found demo metrics under demo2!"
        res = 0

    return 0



if __name__ == "__main__":
    res = RHELOSP_34687_test()
    if res == 0:
        print("RHELOSP_34687_test Finished successfully")
    else:
        print("RHELOSP_34687_test failed")
    sys.exit(res)