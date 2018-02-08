from check_gnocchi_service import *
#TODO First switch to instance you need to check
def RHELOSP_27787_test():
    out = 1

    for gnocchi_process in gnocchi_process_list:
        out = check_openstack_service(gnocchi_process)

        if out == 0:
            print("%s service is running while it's supposed to be dockerized!!"% gnocchi_process)
            return 1
        else:
            print("%s service is not running!"% gnocchi_process)
            out = 0

    return out

if __name__ == "__main__":
    res = RHELOSP_27787_test()
    if res == 0:
        print("RHELOSP_27787 Finished successfully")
    else:
        print("RHELOSP_27787 failed")
    sys.exit(res)