import os, psutil, time

def _getProcessBeforeExec():
    current_processes = []
    processlist = os.popen("tasklist").readlines()
    for p in processlist:
        try:
            current_processes.append(int(p[29:34]))
        except:
            pass
    return current_processes

def display_process_data(pl):
    for p in pl:
        print(f"New Process Detected with PID: {p}\n", psutil.Process(p))

def processData(current_process):
    old = []
    while True:
        new_processes = []
        process_after_exec = os.popen("tasklist").readlines()
        for np in process_after_exec:
            if np not in current_process:
                new_processes.append(np)
        if len(new_processes) != 0 and sorted(old) != sorted(current_process):
            old = new_processes
            display_process_data()
        #time.sleep(2)

if __name__ == '__main__':
    cp = _getProcessBeforeExec()
    processData(cp)