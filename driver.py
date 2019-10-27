import process_listener as pl
import utils
import logfile
import os
import static_analysis


if __name__ == '__main__':
    ''' driver code which analyzes the uploaded file '''
    
    analyze_file = r"C:\Users\Sahil\Documents\Projects\SDHacks\a.exe"
    cp = pl.get_current_processes()
    os.startfile(analyze_file)
    xray_objects = pl.listener(cp)
    ret = static_analysis.execute_and_crosscheck_strings(analyze_file)
    logfile.process_log(xray_objects, ret,"./mylogfile.txt")
