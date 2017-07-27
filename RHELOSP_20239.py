from check_gnocchi_service import *

def RHELOSP_20239_test():
    out = 1

    out = ceilometer_event_show()
    if out != 0:
        print("Event not shown in the list!")
        return 1
    return out

if __name__ == "__main__":
    res = RHELOSP_20239_test()
    if res == 0:
        print("Finished successfully")
