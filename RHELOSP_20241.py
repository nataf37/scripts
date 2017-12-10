from check_gnocchi_service import *

def RHELOSP_20241_test():
    out = 1
    event_name="alarm.creation"
    out = ceilometer_filter_by_trait(event_name)
    if out != 0:
        print("Event not found in the list!")
        return 1
    return 0

if __name__ == "__main__":
    res = RHELOSP_20241_test()
    if res == 0:
        print("RHELOSP_20241 Finished successfully")
    else:
        print("RHELOSP_20241 failed")
    sys.exit(res)