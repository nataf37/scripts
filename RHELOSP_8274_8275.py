from check_gnocchi_service import *

def RHELOSP_8274_8275_test():
    out = 1

    out = gnocchi_archive_policy_create(archive_policy_name)
    if out[0] != 0:
        print("Policy for %s wasn't created!"%archive_policy_name)
        return 1
    out = gnocchi_archive_policy_delete(archive_policy_name)
    if out[0] != 0:
        print("Policy for %s wasn't deleted!"%archive_policy_name)
        return 1
    out = gnocchi_archive_policy_is_deleted(archive_policy_name)
    if out[0] != 0:
        print("Policy for %s wasn't deleted!" % archive_policy_name)
        return 1
    return 0

if __name__ == "__main__":
    res = RHELOSP_8274_8275_test()
    if res == 0:
        print("RHELOSP_8274_8275 Finished successfully")
    else:
        print("RHELOSP_8274_8275 failed")
    sys.exit(res)