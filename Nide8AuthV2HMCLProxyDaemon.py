import os,time
a = 1
while a == 1:
    os.system('java -jar ./Nide8AuthV2HMCLProxy.jar &')
    time.sleep(600)
    pid = os.popen('ps -ef | grep Nide8AuthV2HMCLProxy').readlines()[0].split()[1]
    os.system('kill -9 '+pid)