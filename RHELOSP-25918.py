from check_gnocchi_service import *
import os
def RHELOSP_25918_test():
    out = 1

    path = ["/var/log/aodh/", "/var/log/gnocchi/"]
    line = "combination"
    for p in path:
        for logfile in os.listdir(p):
            print logfile
            if os.path.isfile(logfile):
                out = check_log_for_errors(logfile, line)
                if out == 0:
                    print("Log is clear.")
                    out = 0
                else:
                    print("There was an error in the log %s!"% logfile)
                    return 1

    return out

if __name__ == "__main__":
    res = RHELOSP_25918_test()
    if res == 0:
        print("RHELOSP_25918 Finished successfully")
    else:
        print("RHELOSP_25918 failed")
    sys.exit(res)