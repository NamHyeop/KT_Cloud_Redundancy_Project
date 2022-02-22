import os
import psutil
import time

# from kubernetes import client, config
from flask import Flask

current_cpu_state = 0

def _check_usage_of_cpu_and_memory():
    pid = os.getpid()
    py = psutil.Process(pid)

    # cpu_usage = os.popen("ps aux | grep " + str(pid) + " | grep -v grep | awk '{print $3}'").read()
    #current_cpu_state = psutil.cpu_percent()
    # cpu_usage = cpu_usage.replace("\n", "")
    memory_usage = round(py.memory_info()[0] / 2. ** 30, 2)
    #print("current cpu state perecent : " + str(psutil.cpu_percent()))
    
    l1, l2, l3 = psutil.getloadavg()
    CPU_use = str((l1 / os.cpu_count())* 100)
    print("cpu_status " + CPU_use)
    current_cpu_state = CPU_use
    print("cpu_freq" + str(psutil.cpu_freq))
    #print("cpu_usage = " + str(cpu_usage))
    print("mempory_usage = " + str(memory_usage))
    print("=" * 20)
    return CPU_use

app = Flask(__name__)

@app.route('/')
@app.route('/GetCpuInfo')
def GetCpuInfo():
    current_cpu_state = _check_usage_of_cpu_and_memory()
    return str(current_cpu_state)

if __name__ == '__main__':
    app.run(host='172.20.10.5', port=9090)
    while 1:
        time.sleep(1)
        # _check_usage_of_cpu_and_memory()

