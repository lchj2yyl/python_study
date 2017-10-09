from socket import *


socket = socket(AF_INET, SOCK_DGRAM)

sendAddr = ('127.0.0.1', 8889)

while True:
    client_input = raw_input('input a str : ')
    if client_input == 'exit':
        print 'will exit'
        socket.close()
        break
    socket.sendto(client_input, sendAddr)
print 'exit'

