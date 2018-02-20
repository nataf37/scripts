from check_gnocchi_service import *
import os
def RHELOSP_25997_test():
    out = 1
    service = "gnocchi"
    lines = {"workers":"48","metric_processing_delay":"60"}
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
    res = RHELOSP_25997_test()
    if res == 0:
        print("RHELOSP_25997 Finished successfully")
    else:
        print("RHELOSP_25997 failed")
    sys.exit(res)