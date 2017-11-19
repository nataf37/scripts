from check_gnocchi_service import *
#TODO First switch to instance you need to check
def RHELOSP_27779_test():
    out = 1

    for panko_process in panko_process_list:
        out = check_docker_process(panko_process)
        if out == 0:
            print("%s service is running!"% panko_process)
            out = 0
        else:
            print("%s service is not running!"% panko_process)
            return 1

    return out

if __name__ == "__main__":
    res = RHELOSP_27779_test()
    if res == 0:
        print("RHELOSP_27779 Finished successfully")
    else:
        print("RHELOSP_27779 failed")
    sys.exit(res)