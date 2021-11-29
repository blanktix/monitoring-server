import os
import platform
from datetime import date, timedelta

today = date.today()
#Check whether the connection is suspicious
def CheckListeningPort():
    OS=platform.system()
    if OS=="Windows":
        os.system("netstat -b")
    else:
        os.system("netstat -p | awk 'NR>1' | sed '/Active/q' | sed '$d'")

#Check new file stored in server
def CheckForNewFile(dir="."):
    OS=platform.system()
    # We will specify the date to last week
    date_delta= today - timedelta(days=7)
    if OS=="Windows":
        date=date_delta.strftime("%m-%d-%Y")
        os.system(f"FORFILES /P {dir} /S /D +{date}")
    else:
        date=date_delta.strftime("%m/%d/%Y")
        os.system(f"find {dir} -newermt {date}")

def CheckLogService():
    pass

# CheckListeningPort()
# CheckForNewFile()