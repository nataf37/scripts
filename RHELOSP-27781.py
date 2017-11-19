from check_gnocchi_service import *
#TODO First switch to instance you need to check
def RHELOSP_27781_test():
    out = 1

    for ceilometer_process in ceilometer_process_list:
        out = check_docker_process(ceilometer_process)
        if out == 0:
            print("%s service is running!"% ceilometer_process)
            out = 0
        else:
            print("%s service is not running!"% ceilometer_process)
            return 1

    return out

if __name__ == "__main__":
    res = RHELOSP_27781_test()
    if res == 0:
        print("RHELOSP_27781 Finished successfully")
    else:
        print("RHELOSP_27781 failed")
    sys.exit(res)