import os, psutil, time

def _getProcessBeforeExec():
    current_processes = []
    processlist = os.popen("tasklist").readlines()
    for p in processlist:
        try:
            current_processes.append(int(p[29:34]))
        except:
            pass
    processData(current_processes)

def display_process_data(pl):
    for p in pl:
        try:
            print("New Process Detected with PID:{}".format(psutil.Process(p)))
        except:
            pass
        #print(psutil.Process(p))

def processData(previous_processes):
    new_processes = []
    while True:
        get_total_processes = os.popen("tasklist").readlines()
        for p in get_total_processes:
            try:
                c = int(p[29:34])
            except:
                pass
            else:  
                if c not in previous_processes:
                    new_processes.append(c)

        display_process_data(new_processes)
        time.sleep(2)
        new_processes += previous_processes
        
if __name__ == '__main__':
    cp = _getProcessBeforeExec()
    processData(cp)