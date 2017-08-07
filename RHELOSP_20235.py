from check_gnocchi_service import *

def RHELOSP_20235_test():
    out = 1

    out = check_openstack_event_type_list()
    if out[0] != 0:
        print("Ceilometer event type list is not found!")
        return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_20235_test()
    if res == 0:
        print("RHELOSP_20235 Finished successfully")
    else:
        print("RHELOSP_20235 failed")
    sys.exit(res)