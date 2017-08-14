from check_gnocchi_service import *

def RHELOSP_25031():
    out = 1

    out = check_aodh_alarm_list(alarm_out)
    if out[0] != 0:
        print("Aodh alarm list is not found!")
        return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_25031()
    if res == 0:
        print("RHELOSP_25031 Finished successfully")
    else:
        print("RHELOSP_25031 failed")
    sys.exit(res)
