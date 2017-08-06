from check_gnocchi_service import *

def RHELOSP_20238_test():
    out = 1

    out = ceilometer_event_list()
    if out[0] != 0:
        print("No event list found!")
        return 1
    return 0

if __name__ == "__main__":
    res = RHELOSP_20238_test()
    if res == 0:
        print("RHELOSP_20238 Finished successfully")
    else:
        print("RHELOSP_20238 failed")
    sys.exit(res)
