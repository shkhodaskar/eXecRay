import memory_usage as mu
import utils


if __name__ == '__main__':
    cp = mu.get_current_processes()
    xray_objects = mu.listener(cp)
    for i in xray_objects:
        i.get_hardware_resources()
    
