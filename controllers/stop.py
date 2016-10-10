#
# Endpoint:
#   /stop
#
from controllers import play

def stop_get() -> str:
    print(play.playthread)
    play.playthread.join(0)
    return({"result": "stop success"}, 200)
