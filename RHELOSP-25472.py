from check_gnocchi_service import *
def RHELOSP_25472_test():
    out = 1
    line = "Scope(Class[Panko::Api]): This Class is deprecated"
    service_name = "gnocchi"
    out = check_log(service_name, line)
    if out == 0:
        print("Found the line in %s logs."% service_name)
        out = 0
    else:
        print("Did not find the line in %s logs."% service_name)
        return 1

    return out

if __name__ == "__main__":
    res = RHELOSP_25472_test()
    if res == 0:
        print("RHELOSP_25472 Finished successfully")
    else:
        print("RHELOSP_25472 failed")
    sys.exit(res)