from check_gnocchi_service import *
import sys

#TODO First switch to instance you need to check
def RHELOSP_24696_test(cloud):
    out = 1

    if cloud == "over":
        out = check_system_process("ceilometer-polling")
        if out != 0:
            print("Ceilometer-polling service is not running!")
            return 1
        else:
            print("Ceilometer-polling service is running!")

    if cloud == "under":
        out = check_system_process("ceilometer-central")
        if out != 0:
            print("Ceilometer-central service is not running!")
            return 1
        else:
            print("Ceilometer-central service is running!")

    out = check_system_process("ceilometer-notification")
    if out != 0:
        print("Ceilometer-notification service is not running!")
        return 1
    else:
        print("Ceilometer-notification service is running!")

    return out

if __name__ == "__main__":
    #Arguement is "under" or "over"
    if  len(sys.argv) > 1:
        res = RHELOSP_24696_test(sys.argv[1])
    else:
        res = 1

    if res == 0:
        print("RHELOSP_24696 Finished successfully")
    else:
        print("RHELOSP_24696 failed")
    sys.exit(res)