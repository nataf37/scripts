from check_gnocchi_service import *


def RHELOSP_7044_pretest():
    # change pipeline
    res = edit_pipeline(pipeline_file, gnocchi_pipeline_image_input)
    if res != 0:
        print("Can't change the pipeline file!")
        return 1
    print("Change pipeline file")

    # change gnocchi resource file
    res = edit_source(gnocchi_resources_file, gnocchi_resources_image_input)
    if res != 0:
        print("Can't change the gnocchi file!")
        return 1
    print("Change gnocchi resource file")

    '''
    #Remove all the existing images
    #1.Get the list of existing images
    image_list = find_resources('image')
    #2. Remove the images
    for im in image_list:
        res = remove_resource(im, 'image')
        if res !=0:
            print("Couldn't delete %s with id %s"%('image', im))
            return 1
    print("Remove all the existing images")
    '''

    # Restart the processes
    for proc in proc_list:
        res = restart_process(proc)
        if res != 0:
            print("Couldn't restart %s" % proc)
            return 1
    time.sleep(60)
    print("Restart the processes")
    return 0

if __name__ == "__main__":
    res = RHELOSP_7044_pretest()
    if res == 0:
        print("Finished successfully")