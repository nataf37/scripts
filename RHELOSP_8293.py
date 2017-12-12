from check_gnocchi_service import *

def RHELOSP_8292_test():
    out = 1
    res_type = 'image'

    #Create new image
    res, id = create_new_resource(res_type)
    if res !=1:
        resource_id = id
        res = 0
    else:
        print("Couldn't create image")
        return 1

    print("Created image")

    #Check that the resource is added to metric list
    res = test_new_resource(res_type, resource_id)
    if res == 1:
        return 1

    out = search_resource(res_type, resource_id)
    if out[0] != 0:
        print("The resource search is empty!")
        return 1


    return 0

if __name__ == "__main__":
    res = RHELOSP_8292_test()
    if res == 0:
        print("RHELOSP_8292 Finished successfully")
    else:
        print("RHELOSP_8292 failed")
    sys.exit(res)