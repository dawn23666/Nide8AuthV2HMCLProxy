import os,sys
try:
    pid = os.popen('ps -ef | grep Nide8AuthV2HMCLProxy').readlines()[0].split()[1]
    os.system('kill -9 '+pid)
except:
    pass
os.system('java -jar ./Nide8AuthV2HMCLProxy.jar &')