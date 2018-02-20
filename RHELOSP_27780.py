from check_gnocchi_service import *
#TODO First switch to instance you need to check
def RHELOSP_27780_test():
    out = 1

    for gnocchi_process in gnocchi_process_list:
        out = check_docker_process(gnocchi_process)
        if out == 0:
            print("%s service is running!"% gnocchi_process)
            out = 0
        else:
            print("%s service is not running!"% gnocchi_process)
            return 1

    return out

if __name__ == "__main__":
    res = RHELOSP_27780_test()
    if res == 0:
        print("RHELOSP_27780 Finished successfully")
    else:
        print("RHELOSP_27780 failed")
    sys.exit(res)