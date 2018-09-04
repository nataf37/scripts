from check_gnocchi_service import *

def RHELOSP_39201_test():
    res = 1

    # Create new volume: 1
    res_type = 'volume'
    res, id = create_new_resource(res_type,"my-first-volume")
    if res != 1:
        resource_id = id
        res = 0
    else:
        return 1

    # Create new volume: 2
    res_type = 'volume'
    res, id = create_new_resource(res_type,"my-second-volume")
    if res != 1:
        resource_id_2 = id
        res = 0
    else:
        return 1

    #Check the time of creation in volume list

    param_name = 'created_at'
    res, timestamp = check_resource_param(res_type, resource_id, param_name)
    if res != 0:
        return 1
    else:
        print ("%s %s %s timestamp is %s"%(res_type, resource_id, param_name, timestamp))
    # Check the time of creation in gnocchi

    gnocchi_param_name = 'started_at'
    res, timestamp = check_gnocchi_resource_param(resource_id, param_name)
    if res != 0:
        return 1
    else:
        print ("Metric %s timestamp is %s"%(param_name, timestamp))
    return 0

if __name__ == "__main__":
    res = RHELOSP_39201_test()
    if res == 0:
        print("RHELOSP_39201_test Finished successfully")
    else:
        print("RHELOSP_39201_test failed")
    sys.exit(res)