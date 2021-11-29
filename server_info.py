from os import name
import psutil as ps
import datetime
import platform

def GetCPUInformation():
    CPU_INFO={
            'CPU_TIMES':ps.cpu_times()._asdict(),
            'CPU_PERCENT':ps.cpu_percent(),
            'CPU_TIMES_PERCENT':ps.cpu_times_percent()._asdict(),
            'CPU_COUNT':ps.cpu_count(),
            'CPU_STATS':ps.cpu_stats()._asdict(),
            'CPU_FREQ':ps.cpu_freq()._asdict(),
            "CPU_TEMPERATURE":ps.sensors_temperatures(fahrenheit=False) if platform.system()=="Linux" else [] 
        }
    return(
        CPU_INFO
    )

def GetMemoryInformation():
    MEM_INFO={
        "VIRTUAL_MEMORY":ps.virtual_memory()._asdict(),
        "SWAP":ps.swap_memory()._asdict(),
    }
    return(
        MEM_INFO
    )

def GetDiscInformation(path="/"):
    DISC_INFO={
        "DISK_PARTITION":ps.disk_partitions(),
        "DISK_USAGE":ps.disk_usage(path=path)._asdict(),
        "DISC_IO_COUNTERS":ps.disk_io_counters()._asdict()
    }
    return(
        DISC_INFO
    )

def GetNetworkInformation():
    NET_INFO={
        "NET_IO_COUNTERS":ps.net_io_counters()._asdict(),
        "NET_CONNECTIONS":ps.net_connections(),
        "NET_INTERFACE_ADDR":ps.net_if_addrs(),
        "NET_INTERFACE_STAT":ps.net_if_stats(),
    }
    return(
        NET_INFO
    )

def GetServerInformation():
    SERVER_INFO={
        'BOOT_TIME':datetime.datetime.fromtimestamp(ps.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
        "USERS":ps.users(),
        'PROCESS':[proc.info for proc in ps.process_iter(['pid', 'name', 'username'])]
    }

    return(
        SERVER_INFO
    )
# print(GetCPUInformation())
# print(GetMemoryInformation())
# # print(GetDiscInformation())
# print(GetNetworkInformation()["NET_CONNECTIONS"][0])
# print(GetServerInformation())