from check_gnocchi_service import *
#TODO First switch to instance you need to check
def RHELOSP_27789_test():
    out = 1

    for ceilo_process in ceilometer_process_list:
        out = check_openstack_service(ceilo_process)

        if out == 0:
            print("%s service is running while it's supposed to be dockerized!"% ceilo_process)
            return 1
        else:
            print("%s service is not running!"% ceilo_process)
            out = 0

    return out

if __name__ == "__main__":
    res = RHELOSP_27789_test()
    if res == 0:
        print("RHELOSP_27789 Finished successfully")
    else:
        print("RHELOSP_27789 failed")
    sys.exit(res)