from pytonik import serv
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = sock.getsockname()[1]
print(sock.getsockname())
serv.run(host="", path="", port=port)