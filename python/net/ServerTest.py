from socket import *


socket = socket(AF_INET, SOCK_DGRAM)
socketAdder = ('', 8889)
socket.bind(socketAdder)

while True:
    recvData = socket.recvfrom(1024)
    print recvData