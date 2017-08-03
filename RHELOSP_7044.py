from check_gnocchi_service import *

def RHELOSP_7044_test():
    res = 1
    """
    #change pipeline
    res = edit_pipeline(pipeline_file, gnocchi_pipeline_image_input)
    if res != 0:
        print("Can't change the pipeline file!")
        return 1
    print("Change pipeline file")

    #change gnocchi resource file
    res =edit_source(gnocchi_resources_file, gnocchi_resources_image_input)
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
    
    #Restart the processes
    for proc in proc_list:
        res = restart_process(proc)
        if res != 0:
            print("Couldn't restart %s"%proc)
            return 1
    time.sleep(60)
    print("Restart the processes")
    """
    #Create new image
    res, id = create_new_resource("image")
    if res !=1:
        resource_id = id
        res = 0
    else:
        print("Couldn't create image")
        return 1
    time.sleep(60)
    print("Created image")

    #Check that the resource is added to metric list
    res = test_new_resource("image", resource_id)
    if res == 1:
        return 1

    print("Check that the image is added to metric")

    #Rename the image
    new_image_name = 'ImageGnocchiTest7044'
    res = rename_resource(resource_id, 'image', new_image_name)
    if res !=0:
        print("Couldn't rename resource %s to %s"%(resource_id, new_image_name))
        return 1
    print("Rename image")

    #Wait several polling cycles
    print('Waiting for image to update in metric')
    time.sleep(60)
    print('Waiting for image to update in metric')
    time.sleep(60)
    print('Waiting for image to update in metric')
    time.sleep(60)
    print('Checking that the image is updated')

    #Check the new name
    new_name = show_resource('image', resource_id)
    if new_name != new_image_name:
        print("The name of metric %s isn't corresponding to the name of image %s"%(new_name,new_image_name))
        return 1
    print("The image has been renamed successfully")

    return 0

if __name__ == "__main__":
    res = RHELOSP_7044_test()
    if res == 0:
        print("RHELOSP_7044 Finished successfully")
    else:
        print("RHELOSP_7044 failed")
    sys.exit(res)