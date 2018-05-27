from check_gnocchi_service import *

def RHELOSP_34688_test():
    res = 1

    #1. Check that there is no test project
    field = "project"
    proj_value = "test"
    print("Checking that there is no %s in the list of %s" % (proj_value, field))
    res = check_field(field, proj_value)

    if res[0] !=0:
        return 1

    #2. Create test project
    if res[1] != 'Got':
        print("Creating %s %s" % (proj_value, field))
        res = build_field(field, proj_value)

        if res[0] !=0:
            return 1

    #3.0. Check that there is no test user
    field = "user"
    user_value = "test"
    print("Checking that there is no %s in the list of %s" % (user_value, field))
    res = check_field(field, user_value)

    if res[0] !=0:
        return 1
    #3.1. Create test user
    if res[1] != 'Got':
        print("Creating %s %s" % (user_value, field))
        res = build_field(field, user_value)

        if res[0] !=0:
            return 1

    #5. Add test to user role
    role = "user"
    res = add_role(proj_value, user_value, role)

    if res[0] !=0:
        return 1

    #6. Check that the project has been created
    field = "project"

    print("Checking that there is %s in the list of %s" % (proj_value, field))
    res = check_field(field, proj_value)

    if res[0] != 0:
        return 1

    #7. Create new testrc file, replace pass, project and user to test
    res = copy_file(orig_rc, test_rc)
    if res[0] !=0:
        return 1

    res = change_file(test_rc, 'OS_USERNAME', user_value)
    if res[0] !=0:
        return 1

    res = change_file(test_rc, 'OS_PASSWORD', user_value)
    if res[0] !=0:
        return 1

    res = change_file(test_rc, 'OS_PROJECT_NAME', proj_value)
    if res[0] !=0:
        return 1

    #8. Switch to testrc file
    res = switch_context(test_rc)
    if res != 0:
        return 1

    #9. Test that the list of resources is empty
    res = list_resources
    if res[1] != 'Empty':
        return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_34688_test()
    if res == 0:
        print("RHELOSP_34688_test Finished successfully")
    else:
        print("RHELOSP_34688_test failed")
    sys.exit(res)