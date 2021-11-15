#!C:\Users\HP\Desktop\PYTHON\healtcheck.py
import shutil
import psutil

#return true if machine is good. machine is good if the disk usage is > 20% free
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = round(du.free/du.total*100)
    return free > 20
#machine is healthy if cpu usage < 75%
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("Check resources, carajo!")
    print()
    if not check_disk_usage("/"):
        print("Disk usage too high.")
    else:
        print("Processor usage too high.")
else:
    print("Resources are good, bro!")
