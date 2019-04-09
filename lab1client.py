#lab1

from socket import *
#import socket
import sys # In order to terminate the program

clientSocket = socket(AF_INET, SOCK_STREAM)
 
HOST = sys.argv[1]
PORT = sys.argv[2]
FILE = sys.argv[3]

print 'host ' + HOST + ' PORT ' + PORT + ' FILE ' + FILE
 

clientSocket.connect((HOST, int(PORT)))

message = "GET /" + FILE+ "\r\n"

clientSocket.send(message)

reply = clientSocket.recv(1024)
clientSocket.close()
print reply
