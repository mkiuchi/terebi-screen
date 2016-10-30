import socket, atexit
from zeroconf import ServiceInfo, Zeroconf
from uuid import getnode

version = '0.0.2'

zeroconf = Zeroconf()
fqdn        = socket.gethostname()
ipAddr      = socket.gethostbyname(fqdn)
serviceType = "_http._tcp.local."
serviceName = "terebi-screen." + serviceType
serviceDesc = {'service': 'Tetebi Screen', 'version': version, 'path': '/ui/'}

info = ServiceInfo(serviceType,
                          serviceName,
                          socket.inet_aton(ipAddr),
                          8888,
                          0, 0,
                          serviceDesc,
                          fqdn+".local.")
def unregisterService():
    zeroconf.unregister_service(info)

atexit.register(unregisterService)
zeroconf.register_service(info)

