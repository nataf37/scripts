from check_gnocchi_service import *

def RHELOSP_39205_test():
    res = 1

    #Check metric list
    res_type = 'volume'
    res_name = "my-first-volume"
    res, id = create_new_resource(res_type,)
    if res != 1:
        resource_id = id
        res = 0
    else:
        return 1

    #Find image_id and instance_id  in resource attributes
    gnocchi_param_name = 'image_id'
    res, param_val = check_gnocchi_resource_param(resource_id, gnocchi_param_name)
    if res != 0:
        return 1
    else:
        print ("Metric %s is %s"%(gnocchi_param_name, param_val))

    gnocchi_param_name = 'instance_id'
    res, param_val = check_gnocchi_resource_param(resource_id, gnocchi_param_name)
    if res != 0:
        return 1
    else:
        print ("Metric %s is %s"%(gnocchi_param_name, param_val))

    return res


if __name__ == "__main__":
    res = RHELOSP_39205_test()
    if res == 0:
        print("RHELOSP_39205_test Finished successfully")
    else:
        print("RHELOSP_39205_test failed")
    sys.exit(res)