from check_gnocchi_service import *

def RHELOSP_39283_test():
    res = 1
    resource_id = 0
    #Find volume in metric list
    res, id = get_resource_id('volume', 'my-volume')
    if res != 1:
        resource_id = id
        res = 0
    else:
        return 1

    #Delete volume
    res = remove_resource(resource_id, 'volume')
    if res != 0:
        return 1
    else:
        print ("Volume %s is deleted"%(resource_id))
    return res

    #Check that volume is not in the list anymore
    res1 = find_resource_by_ip(resource_id)
    if res == 1:
        res = 0
    else:
        print("The resource wasn't deleted!")
        return 1


if __name__ == "__main__":
    res = RHELOSP_39283_test()
    if res == 0:
        print("RHELOSP_39283_test Finished successfully")
    else:
        print("RHELOSP_39283_test failed")
    sys.exit(res)