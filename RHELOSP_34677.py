from check_gnocchi_service import *

def RHELOSP_34677_test():
    res = 1

    #1. Check that there is no demo project
    field = "project"
    value = "demo"
    print("Checking that there is no %s in the list of %s" % (value, field))
    res = check_field(field, value)

    if res[0] !=0:
        return 1

    #2. Create demo project
    print("Creating %s %s" % (value, field))
    res = build_field(field, value)

    if res[0] !=0:
        return 1

    #3. Create demo user
    field = "user"
    value = "demo"
    print("Creating %s %s" % (value, field))
    res = build_field(field, value)

    if res[0] !=0:
        return 1

    #4. Create role
    field = "role"
    value = "user"
    print("Creating %s %s" % (value, field))
    res = build_field(field, value)

    if res[0] !=0:
        return 1

    #5. Add demo to user role

    return 0

if __name__ == "__main__":
    res = RHELOSP_34677_test()
    if res == 0:
        print("RHELOSP_34677 Finished successfully")
    else:
        print("RHELOSP_34677 failed")
    sys.exit(res)
