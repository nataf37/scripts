from check_gnocchi_service import *

def RHELOSP_39201_test():
    res = 1

    #Check event list
    event_name='volume.create.start'
    res, er = check_openstack_event_type_list(event_name)
    if res != 1:
        res = 0
    else:
        return 1

    res, event_id = event_show(event_name)
    if res != 1:
        print ("Event ID: %s"%event_id)
        res = 0
    else:
        return 1

    trait = 'image_id'
    res, trait_val = ceilometer_filter_by_trait(event_name, trait)
    if res != 1:
        print ("%s: %s"%(trait,event_id))
        res = 0
    else:
        return 1

    trait = 'instance_id'
    res, trait_val = ceilometer_filter_by_trait(event_name, trait)
    if res != 1:
        print ("%s: %s"%(trait,event_id))
        res = 0
    else:
        return 1

    return res


if __name__ == "__main__":
    res = RHELOSP_39201_test()
    if res == 0:
        print("RHELOSP_39201_test Finished successfully")
    else:
        print("RHELOSP_39201_test failed")
    sys.exit(res)