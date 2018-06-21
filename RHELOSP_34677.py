from check_gnocchi_service import *

def RHELOSP_34677_test():
    res = 1

    #1. Check that there is no demo project
    field = "project"
    proj_value = "demo"
    print("Checking that there is no %s in the list of %s" % (proj_value, field))
    res = check_field(field, proj_value)

    if res[0] !=0:
        return 1

    #2. Create demo project
    if res[1] != 'Got':
        print("Creating %s %s" % (proj_value, field))
        res = build_field(field, proj_value)

        if res[0] !=0:
            return 1

    #3.0. Check that there is no demo user
    field = "user"
    user_value = "demo"
    print("Checking that there is no %s in the list of %s" % (user_value, field))
    res = check_field(field, user_value)

    if res[0] !=0:
        return 1
    #3.1. Create demo user
    if res[1] != 'Got':
        print("Creating %s %s" % (user_value, field))
        res = build_field(field, user_value)

        if res[0] !=0:
            return 1

    #4. Create role
    field = "role"
    value = "user"
    print("Creating %s %s" % (user_value, field))
    res = build_field(field, user_value)

    if res[0] !=0:
        return 1

    #5. Add demo to user role
    role = "demo"
    res = add_role(proj_value, user_value, role)

    if res[0] !=0:
        return 1

    #6. Check that the project has been created
    field = "project"
    proj_value = "demo"
    print("Checking that there is %s in the list of %s" % (proj_value, field))
    res = check_field(field, proj_value)

    if res[0] != 0:
        return 1

    #7. Create new demorc file, replace pass, project and user to demo
    res = copy_file(orig_rc, demo_rc)
    if res[0] !=0:
        return 1

    res = change_file(demo_rc, 'OS_USERNAME', 'demo')
    if res[0] !=0:
        return 1

    res = change_file(demo_rc, 'OS_PASSWORD', 'demo')
    if res[0] !=0:
        return 1

    res = change_file(demo_rc, 'OS_PROJECT_NAME', 'demo')
    if res[0] !=0:
        return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_34677_test()
    if res == 0:
        print("RHELOSP_34677 Finished successfully")
    else:
        print("RHELOSP_34677 failed")
    sys.exit(res)
