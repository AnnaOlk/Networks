#lab1

#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

PORT = 8887
HOST = ''

#Prepare a server socket
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

            
    try:
        message = connectionSocket.recv(1024)              
        filename = message.split()[1]                 
        f = open(filename[1:]) 

        outputdata = f.read()
                  
        #Send one HTTP header line into socket

	connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
	connectionSocket.send(outputdata)

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
	connectionSocket.send('\n404 NOT FOUND\n\n')

        #Close client socket
	connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
