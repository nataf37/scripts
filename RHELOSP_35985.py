from check_gnocchi_service import *

def RHELOSP_35985_test():
    res = 1

    #1. Checking that the gnocchi backend is file
    #. 1.1 - you're supposed to run this on controller and under sudo

    service = "gnocchi"
    file = "/etc/gnocchi/gnocchi.conf"
    field = "driver"
    value = "file"
    print("Checking that %s backend is %s" % (service, value))
    res = check_docker_conf_file(service, file, field, value)

    # 1. Create new instance
    res, id = create_new_resource("instance")
    print("resource_id=%s" % id)
    if res != 1:
        resource_id = id
    else:
        return 1

    time.sleep(300)

    #1.1 Check that the resource is added to metric list
    res = test_new_resource("instance", resource_id)
    if res != 0:
        return 1

    #1.2 Check the measures of the resource
    old_line = ''
    new_line = ''
    for val in instance_values_assigned_new:
        res = get_measures(resource_id, val)
        if res[0] != 0:
            return 1

    old_line = res[1]

    #2. Restart the service
    process="gnocchi-metricd"
    res = restart_docker_process(process)
    if res != 0:
        return 1

    #3. Check the measures after restart
    for val in instance_values_assigned_new:
        res = get_measures(resource_id, val)
        if res[0] != 0:
            return 1

    new_line = res[1]

    if old_line == new_line:
        res = 0
    else:
        print "The measures weren't preserved, the test failed!"
        return 1

    return 0


if __name__ == "__main__":
    res = RHELOSP_35985_test()
    if res == 0:
        print("RHELOSP_35985_test Finished successfully")
    else:
        print("RHELOSP_35985_test failed")
    sys.exit(res)