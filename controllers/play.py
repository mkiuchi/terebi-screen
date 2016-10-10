#
# Endpoint:
#   /play
#
import sys, os, threading, time
from subprocess import Popen
global playthread
playthread = "mkmkmk"

class playThread(threading.Thread):
    def __init__(self, sid, channel_type, channel):
        super(playThread, self).__init__()
        self.sid = sid
        self.channel_type = channel_type
        self.channel = channel
        self.stoprequest = threading.Event()

    def run(self):
        #print("==start sub thread==")
        os.environ["DISPLAY"] = ":0"
        p = Popen(["ffplay", "-vf", "scale=720:-1", "tcp://0.0.0.0:8888?listen"], close_fds=True)
        mypid = p.pid
        f = open('/tmp/terebi.pid', 'w')
        f.write(str(mypid))
        f.close()
        while not self.stoprequest.isSet():
            time.sleep(1)
            continue
        p.kill()
        os.remove('/tmp/terebi.pid')
    
    def join(self, timeout=None):
        self.stoprequest.set()
        super(playThread, self).join(timeout)

def play_get(sid, channel_type, channel) -> str:
    #print(os.path.exists('/tmp/terebi.pid'))
    if os.path.exists('/tmp/terebi.pid'):
        return({"result": "already running"}, 500)
    else:
        global playthread
        playthread = playThread(sid, channel_type, channel)
        playthread.start()
        return({"result": "start success"}, 200)

        
