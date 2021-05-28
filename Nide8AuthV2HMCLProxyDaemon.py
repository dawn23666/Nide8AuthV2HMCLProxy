import os,time,sys
a = 1
def kill_Nide8AuthV2HMCLProxy():
    pid = os.popen('ps -ef | grep Nide8AuthV2HMCLProxy').readlines()[0].split()[1]
    os.system('kill -9 '+pid)
while a == 1:
    try:
        os.system('java -jar ./Nide8AuthV2HMCLProxy.jar &')
        time.sleep(600)
        kill_Nide8AuthV2HMCLProxy()
    except KeyboardInterrupt:
        kill_Nide8AuthV2HMCLProxy()
        sys.exit()