import subprocess
import os
import re
import time

PID_FILENAME = "chatbotid.txt"

def isChatBotRunning(fileName):
    try:
        f = open(fileName)
        pid = str(f.read())
    except:
        return False  # if we can't open the file or read valid data, then no

    ps = subprocess.Popen("ps -ef | grep " + pid , shell=True, stdout=subprocess.PIPE)
    output = ps.stdout.read().decode('utf-8')
    ps.stdout.close()
    ps.wait()
    if re.search(pid, output) is None:
        return False # PID was not found
    else:
        return True

if __name__ == "__main__":
    if isChatBotRunning(PID_FILENAME):
        print("Is running")
    else:
        print("Needs to start up")
        f = open(PID_FILENAME, 'w')
        f.write(str(os.getpid()))
        f.close()
#        time.sleep(1000)  somthing to test with
        ######
        #
        # start chatbot programming
        #
        ######
