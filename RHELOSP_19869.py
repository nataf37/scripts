from check_gnocchi_service import *

def RHELOSP_19869_test():
    out = 1
    for proc in gnocchi_service_list:
        out = check_system_process(proc)
        if out != 0:
            print("%s is not running!" % proc)
            return 1

    out = check_openstack_service("gnocchi", "metric")
    if out != 0:
        print("Gnocchi service is not running!")
        return 1

    out = check_openstack_user("gnocchi")
    if out != 0:
        print("No gnocchi user found!")
        return 1
    return out

if __name__ == "__main__":
    res = RHELOSP_19869_test()
    if res == 0:
        print("RHELOSP_19869 Finished successfully")
    else:
        print("RHELOSP_19869 failed")
    sys.exit(res)