from check_gnocchi_service import *

def RHELOSP_33764_test():
    res = 1

    #Check that in ceilometer.conf the default event_dispatchers = gnocchi
    field = "event_dispatchers"
    value = "gnocchi"
    print("Checking that the %s in %s is equal to %s" % (field, ceilometer_conf, value))
    res = check_conf_file(ceilometer_conf, field, value)

    if res !=0:
        return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_33764_test()
    if res == 0:
        print("RHELOSP_33764 Finished successfully")
    else:
        print("RHELOSP_33764 failed")
    sys.exit(res)
