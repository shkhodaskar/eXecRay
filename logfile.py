def process_log(filename, process_object_list):
    file = open(filename, "a")
    count = 0
    for i in process_object_list:
        hardware_details = i.get_hardware_resources()
        print(hardware_details)
        hardware_string = "{count}\nProcess Name: {}".format(hardware_details["Name"])
        count +=1
        file.write(hardware_string)
    print("log-created!")
