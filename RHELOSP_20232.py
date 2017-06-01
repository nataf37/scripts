from check_gnocchi_service import *

def RHELOSP_20232_test():
    out = 1

    out = check_openstack_service("panko", "event")
    if out != 0:
        print("Panko service is not running!")
        return 1

    return out

if __name__ == "__main__":
    res = RHELOSP_20232_test()
    if res == 0:
        print("Finished successfully")