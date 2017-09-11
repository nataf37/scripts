from check_gnocchi_service import *
#TODO First switch to instance you need to check
def RHELOSP_24695_test():
    out = 1

    out = check_system_process("ceilometer-collector")
    if out == 0:
        print("Ceilometer-collector service is running!")
        return 1
    else:
        print("Ceilometer-collector service is not running!")
        out = 0

    return out

if __name__ == "__main__":
    res = RHELOSP_24695_test()
    if res == 0:
        print("RHELOSP_24695 Finished successfully")
    else:
        print("RHELOSP_24695 failed")
    sys.exit(res)