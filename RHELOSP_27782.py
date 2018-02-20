from check_gnocchi_service import *
#TODO First switch to instance you need to check
def RHELOSP_27782_test():
    out = 1

    for aodh_process in aodh_process_list:
        out = check_docker_process(aodh_process)
        if out == 0:
            print("%s service is running!"% aodh_process)
            out = 0
        else:
            print("%s service is not running!"% aodh_process)
            return 1

    return out

if __name__ == "__main__":
    res = RHELOSP_27782_test()
    if res == 0:
        print("RHELOSP_27782 Finished successfully")
    else:
        print("RHELOSP_27782 failed")
    sys.exit(res)