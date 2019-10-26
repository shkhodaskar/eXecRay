class ProcessXray():

    def __init__(self, process_id):
        import psutil
        import sys import platform
        self.pid = process_id

        self.os = platform
        self.osdict = {'linux2': None, 'win32': None, 'darwin': None}

        if self.os not in osdict:
            raise OSNotSupportedException(f"Your OS is not supported: {self.os}")


class OSNotSupportedException(Exception):
    pass
