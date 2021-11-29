import csv
import time
from psutil import cpu_times
import server_info
from datetime import date, datetime, timedelta
import subprocess
import platform

CPU_HEADER=[*server_info.GetCPUInformation().keys()]
RAM_HEADER=[*server_info.GetMemoryInformation().keys()]
NET_HEADER=[*server_info.GetNetworkInformation().keys()]

today = date.today()
def init_file():
     with open('cpu.csv', 'w') as CPU, open('RAM.csv', 'w') as RAM, open('net.csv', 'w') as NET:
        cpu_writer=csv.writer(CPU)
        ram_writer=csv.writer(RAM)
        net_writer=csv.writer(NET)

        return cpu_writer.writerow(CPU_HEADER), ram_writer.writerow(RAM_HEADER), net_writer.writerow(NET_HEADER)


def logPerformance():
    # init_file()
    interval = int(time.time() + 60)
    pace=0
    CPU_DATA, RAM_DATA, NET_DATA = [], [], []
    while True:
        try:
            with open(f'cpu{interval}.csv', 'w') as CPU, open(f'ram{interval}.csv', 'w') as RAM, open(f'net{interval}.csv', 'w') as NET:
                cpu_writer=csv.writer(CPU)
                ram_writer=csv.writer(RAM)
                net_writer=csv.writer(NET)
                print(pace)
                CPU_DATA.append([server_info.GetCPUInformation()[x] for x in CPU_HEADER])
                RAM_DATA.append([server_info.GetMemoryInformation()[x] for x in RAM_HEADER])
                NET_DATA.append([server_info.GetNetworkInformation()[x] for x in NET_HEADER])
                time.sleep(5)
                pace+=5
                if pace % 10 ==0:
                    cpu_writer.writerow(CPU_HEADER)
                    cpu_writer.writerows(CPU_DATA)

                    ram_writer.writerow(RAM_HEADER)
                    ram_writer.writerows(RAM_DATA)

                    net_writer.writerow(NET_HEADER)
                    net_writer.writerows(NET_DATA)

                    try:
                        subprocess.subprocess.run(["powershell", "-Command", "Get-ChildItem –Path  . –Recurse | Where-Object {$_.CreationTime –lt (Get-Date).AddMinutes(-1)} | Remove-Item"], capture_output=True)
                    except:
                        pass
                    logPerformance()
        except KeyboardInterrupt:
            exit(0)

if __name__ == "__main__":
    logPerformance()