from check_gnocchi_service import *

def RHELOSP_40414_test():
    res = 1


    #Test cpu metric measures from gnocchi
    #1. Find instance, get it's id
    ins_id = "0"
    instance_list = find_resources('instance')
    if instance_list == []:
        return 1
    else:
        ins_id = instance_list[0]
        print("Instance ID = %s"% ins_id)

    # 2. Observe cpu and cpu_util measures
    #2.1 Observe cpu
    res, id = test_values_assigned(ins_id, 'cpu', 'rate:mean')
    if res != 0:
        print("Problem with cpu measures")
        return 1
    #2.2 Observe cpu_util
    res, id = test_values_assigned(ins_id, 'cpu_util', 'mean')
    if res != 0:
        print("Problem with cpu_util measures")
        return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_40414_test()
    if res == 0:
        print("RHELOSP_40414 Finished successfully")
    else:
        print("RHELOSP_40414 failed")
    sys.exit(res)
