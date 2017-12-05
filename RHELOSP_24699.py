from check_gnocchi_service import *

def RHELOSP_24699_test():
    out = 1

    out = check_openstack_user("gnocchi")
    if out != 0:
        print("No gnocchi user found!")
        return 1

    out = check_openstack_service("gnocchi", "metric")
    if out != 0:
        print("Gnocchi service is not running!")
        return 1

    out = check_openstack_endpoint("gnocchi", "metric")
    if out != 0:
        print("Gnocchi endpoint is not found!")
        return 1

    out = list_resources()
    if out != 0:
        print("Gnocchi resource list is not found!")
        return 1

    return out

if __name__ == "__main__":
    res = RHELOSP_24699_test()
    if res == 0:
        print("RHELOSP_24699 Finished successfully")
    else:
        print("RHELOSP_24699 failed")
    sys.exit(res)