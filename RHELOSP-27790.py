from check_gnocchi_service import *
#TODO First switch to instance you need to check
def RHELOSP_27790_test():
    out = 1

    for aodh_process in aodh_process_list:
        out = check_openstack_service(aodh_process)

        if out == 0:
            print("%s service is running while it's supposed to be dockerized!"% aodh_process)
            return 1
        else:
            print("%s service is not running!"% aodh_process)
            out = 0

    return out

if __name__ == "__main__":
    res = RHELOSP_27790_test()
    if res == 0:
        print("RHELOSP_27790 Finished successfully")
    else:
        print("RHELOSP_27790 failed")
    sys.exit(res)