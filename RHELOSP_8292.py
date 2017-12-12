from check_gnocchi_service import *

def RHELOSP_8292_test():
    out = 1

    out = list_resources()
    if out != 0:
        print("The resource list is empty!")
        return 1


    return 0

if __name__ == "__main__":
    res = RHELOSP_8292_test()
    if res == 0:
        print("RHELOSP_8292 Finished successfully")
    else:
        print("RHELOSP_8292 failed")
    sys.exit(res)