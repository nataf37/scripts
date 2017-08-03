from check_gnocchi_service import *

def RHELOSP_20231_test():
    out = 1

    out = check_openstack_user("panko")
    if out != 0:
        print("No panko user found!")
        return 1
    return out

if __name__ == "__main__":
    res = RHELOSP_20231_test()
    if res == 0:
        print("RHELOSP_20231 Finished successfully")
    else:
        print("RHELOSP_20231 failed")
    sys.exit(res)