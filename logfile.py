def process_log(process_object_list, analysis_report, filename="mylogfile.txt"):
    ''' generates process report based on both static and dynamic analysis '''

    logfile = open(filename, 'w+')
    object_log_list = []
    count = 1
    for o in process_object_list:
        object_details = o.get_hardware_resources()
        name = object_details["Name"]
        cpu_times = object_details["cpu_times"]
        cpu_percent = object_details["cpu_percent"]
        create_time = object_details["create_time"]
        ppid = object_details["ppid"]
        status = object_details["status"]
        object_str = "{}.\n{} --> PID: {}\nCPU_TIMES: {}\nCPU_PERCENT: {}\
        \nCREATE_TIME: {}\nPARENT_PROCESS_ID: {}\nSTATUS: {}\n\n".format(\
        count,name,o.pid,cpu_times,cpu_percent,create_time,ppid,status)
        object_log_list.append(object_str)
        count += 1
    analysis = "Static Analysis Report:\nAfter analyzing the executable, these are potentially dangerous keywords found within the file:\n"
    report = ',\n'.join(analysis_report)
    analysis = analysis + report
    combined_string = '\n'.join(object_log_list)
    logfile.write(combined_string)
    logfile.write(analysis)
    logfile.close()
