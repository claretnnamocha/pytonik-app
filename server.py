from pytonik import serv as server
import os

LOCAL_PORT = 6060
HOST = 'localhost'

PORT = os.environ.get('PORT')
if PORT == None:
    PORT = LOCAL_PORT
    HOST = ''

server.run(host=HOST, port=PORT)
