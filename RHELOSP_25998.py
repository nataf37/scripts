from check_gnocchi_service import *
import os
def RHELOSP_25998_test():
    out = 1
    service = "gnocchi"
    lines = {"workers":"4","metric_processing_delay":"30"}
    for l in lines:
        out = check_conf(service, l, lines[l])
        if out == 0:
            print("The values are in the conf file.")
            out = 0
        else:
            print("There was an error in the conf file!")
            return 1
    return out

if __name__ == "__main__":
    res = RHELOSP_25998_test()
    if res == 0:
        print("RHELOSP_25998 Finished successfully")
    else:
        print("RHELOSP_25998 failed")
    sys.exit(res)