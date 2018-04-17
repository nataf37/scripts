from check_gnocchi_service import *

def RHELOSP_33721_test():
    res = 1, ''

    #Find the IP of telemetry node
    node_name = "telemetry"
    print("Checking that %s node exists" % (node_name))
    res = get_node_ip(node_name)

    if res[0]!=0:
        return 1

    print('The %s node exists, IP=%s'%(node_name,res[1]))
    return 0

if __name__ == "__main__":
    res = RHELOSP_33721_test()
    if res == 0:
        print("RHELOSP_33721 Finished successfully")
    else:
        print("RHELOSP_33721 failed")
    sys.exit(res)
