from check_gnocchi_service import *


def RHELOSP_20607_test():
    out = 1
    # Test that the services are not running
    for proc in gnocchi_service_list:
        out = check_system_process(proc)
        if out == 0:
            print("%s is running!" % proc)
            return 1

    # check openstack services
    out = check_openstack_service("gnocchi", "metric")
    if out == 0:
        print("Gnocchi service is running!")
        return 1

    # check api
    out = check_httpd_process('gnocchi_wsgi')
    if out == 0:
        print("Gnocchi api is running!")
        return 1

    out = check_openstack_user("gnocchi")
    if out == 0:
        print("Gnocchi user found!")
        return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_20607_test()
    if res == 0:
        print("RHELOSP_20607 Finished successfully")
    else:
        print("RHELOSP_20607 failed")
    sys.exit(res)