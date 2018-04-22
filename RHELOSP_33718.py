from check_gnocchi_service import *

def RHELOSP_33718_test():
    res = 1, ''

    #Test the docker processes

    processes_list=aodh_process_list+panko_process_list+ceilometer_process_list+gnocchi_process_list
    for pr in processes_list:
        print("Checking that %s processes run" % (pr))

        res = check_docker_process(pr)
        if res != 0:
            print ("The process %s doesn't exist!"%pr)
            return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_33718_test()
    if res == 0:
        print("RHELOSP_33718 Finished successfully")
    else:
        print("RHELOSP_33718 failed")
    sys.exit(res)
