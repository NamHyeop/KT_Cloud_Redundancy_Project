import subprocess
import os
import time
import requests

url = "http://172.20.10.5:9090"
param = {'current_cpu_state' : 'num'}

# subprocess.call(["ls", "-al"])

while 1:
    time.sleep(2)
    responseCpuValue = requests.get(url, params= param, verify=False)
    print(responseCpuValue.text)
    cpuValue = int(float(responseCpuValue.text))
    if cpuValue > 70:
        print(cpuValue)
        path = os.getcwd()
        os.system('cd {}'.format(os.getcwd()))
        os.system('dir')
        os.system('vagrant up')
        break
    else:
        print("not yet")
