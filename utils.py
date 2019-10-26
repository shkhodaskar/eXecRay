class ProcessXray():

    def __init__(self, process_id):
        import psutil
        from sys import platform
        self.pid = process_id
        self.proc = psutil.Process(self.pid)
        self.name = self.proc.name
        self.os = platform
        self.osdict = {'linux2': None, 'win32': None, 'darwin': None}
        self.harware_resources = {}

        if self.os not in self.osdict:
            raise OSNotSupportedException(f"Your OS is not supported: {self.os}")


    def get_network_activity(self):
        pass


    def get_io_activity(self):
        pass

    def get_hardware_resources(self):

        with self.proc.oneshot():
            self.hardware_resources["Name"] = self.proc.name()
            self.hardware_resources["cpu_times"] = self.proc.cpu_times()
            self.hardware_resources["cpu_percent"] = self.proc.cpu_percent()
            self.hardware_resources["create_time"] = self.proc.create_time()
            self.hardware_resources["ppid"] = self.proc.ppid()
            self.hardware_resources["status"] = self.proc.status()

        print(self.hardware_resources())






class OSNotSupportedException(Exception):
    pass

if __name__ == '__main__':
    x = ProcessXray(1234)
