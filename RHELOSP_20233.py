from check_gnocchi_service import *

def RHELOSP_20233_test():
    out = 1

    out = check_openstack_endpoint("panko", "event")
    if out != 0:
        print("Panko endpoint is not found!")
        return 1

    return out

if __name__ == "__main__":
    res = RHELOSP_20233_test()
    if res == 0:
        print("RHELOSP_20233 Finished successfully")
    else:
        print("RHELOSP_20233 failed")
    sys.exit(res)