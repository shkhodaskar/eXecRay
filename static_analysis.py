#static analysis module
import datasets
import subprocess
import time
import pdb

def execute_and_crosscheck_strings(filepath):
    ''' takes file and malware list as input and does a cross check'''
    collected = []
    string = "strings {}".format(filepath)
    subproc = None
    for i in datasets.malicious_strings:
        curr = string + " | findstr {}".format(i)
        try:
            subproc = subprocess.check_output(curr, shell = True)
            decoded = subproc.decode("utf-8").split('\r\n')
            collected += decoded
        except:
            pass
    ret = set(collected)
    try:
        ret.remove('')
    except KeyError:
        pass

    return ret

if __name__ == '__main__':
    c = execute_and_crosscheck_strings('a.exe')
