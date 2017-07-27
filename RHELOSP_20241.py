from check_gnocchi_service import *

def RHELOSP_20241_test():
    out = 1

    out = ceilometer_filter_by_trait()
    if out != 0:
        print("Event not found in the list!")
        return 1
    return out

if __name__ == "__main__":
    res = RHELOSP_20241_test()
    if res == 0:
        print("Finished successfully")