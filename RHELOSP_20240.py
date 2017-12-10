from check_gnocchi_service import *

def RHELOSP_20240_test():
    out = 1
    event_name = "identity.domain.created"
    out = ceilometer_filter_by_event_type(event_name)
    if out[0] != 0:
        print("Event not found in the list!")
        return 1
    return 0

if __name__ == "__main__":
    res = RHELOSP_20240_test()
    if res == 0:
        print("RHELOSP_20240 Finished successfully")
    else:
        print("RHELOSP_20240 failed")
    sys.exit(res)