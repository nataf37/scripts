from check_gnocchi_service import *
#TODO First switch to instance you need to check
def RHELOSP_27788_test():
    out = 1

    for panko_process in panko_process_list:
        out = check_openstack_service(panko_process)

        if out == 0:
            print("%s service is running while it's supposed to be dockerized!"% panko_process)
            return 1
        else:
            print("%s service is not running!"% panko_process)
            out = 0

    return out

if __name__ == "__main__":
    res = RHELOSP_27788_test()
    if res == 0:
        print("RHELOSP_27788 Finished successfully")
    else:
        print("RHELOSP_27788 failed")
    sys.exit(res)