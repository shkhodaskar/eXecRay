#static analysis module
import datasets
import subprocess
import time
import pdb
#function that gets the file Name, and returns relative file path
def get_relative_file_path(file):
    ''' gets relative file path and returns it '''

    return f'uploads/{file}'

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

#function that executes strings -subprocess and execute strings

#function that takes a strings output and the list of banned words and checks to see which words are in there

if __name__ == '__main__':
    #print(datasets.malicious_strings)
    c = execute_and_crosscheck_strings('a.exe')
    print(c)
