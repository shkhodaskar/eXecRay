import os, psutil, time
import utils
import datasets
#Gets list of all processes running at time of execution. Returns a set
def get_current_processes():
    current_processes = set()
    for proc in psutil.process_iter():
        try:
            current_processes.add(proc.name)
        except psutil.noSuchProcess:
            pass
    return current_processes

def listener(process_list):
    process_xray_list = []
    timer = 0
    while timer <= 15:
        for proc in psutil.process_iter():
            try:
                pn = proc.name
            except psutil.NoSuchProcess:
                pass
            else:
                if pn not in process_list and proc.name().lower() not in datasets.ignored_windows_services:
                    process_xray_object = utils.ProcessXray(proc.pid)
                    process_xray_list.append(process_xray_object)

                    print("New Process:", proc.name(), flush=True)
                    process_list.add(pn)
        time.sleep(1)
        timer += 1

    return process_xray_list


def display_process_data(p):
    print("New Process Detected with PID:{}".format(psutil.Process(p)))
        #print(psutil.Process(p))

if __name__ == '__main__':
    cp = get_current_processes()
    listener(cp)
    #print(len(cp), len(set(cp)))
