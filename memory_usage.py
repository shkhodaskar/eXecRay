import os, psutil, time

#Gets list of all processes running at time of execution. Returns a set
def _getProcessBeforeExec():
    current_processes = set()
    for proc in psutil.process_iter():
        try:
            current_processes.add(proc.name)
        except psutil.noSuchProcess:
            pass
    return current_processes

def processData(process_list):
    while True:
        for proc in psutil.process_iter():
            try:
                pn = proc.name
            except psutil.NoSuchProcess:
                pass
            else:
                if pn not in process_list:
                    print("New Process:", pn, flush=True)
                    process_list.add(pn)


def display_process_data(p):
    print("New Process Detected with PID:{}".format(psutil.Process(p)))
        #print(psutil.Process(p))

if __name__ == '__main__':
    cp = _getProcessBeforeExec()
    processData(cp)
    #print(len(cp), len(set(cp)))
