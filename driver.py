import process_listener as pl
import utils


if __name__ == '__main__':
    cp = pl.get_current_processes()
    xray_objects = pl.listener(cp)
    # for i in xray_objects:
    #     i.get_hardware_resources()
