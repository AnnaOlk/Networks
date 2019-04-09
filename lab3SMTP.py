from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.uvic.ca'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
mailFrom = 'mail from: <annaolkhovskaia@gmail.com> \r\n'
clientSocket.send(mailFrom.encode())
recv1 = clientSocket.recv(1024).decode() 
print(recv)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. 
rcptTo = 'rcpt to: <annaolkhovskaia@gmail.com> \r\n'
clientSocket.send(rcptTo.encode())
recv1 = clientSocket.recv(1024).decode() 
print(recv)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response. 
dataCommand = 'Data\r\n'
clientSocket.send(dataCommand.encode())
recv1 = clientSocket.recv(1024).decode() 
print(recv)
if recv1[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
# Message ends with a single period.
clientSocket.send((msg + endmsg).encode())
recv1 = clientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'quit\r\n'
clientSocket.send(quitCommand.encode())
recv1 = clientSocket.recv(1024).decode() 
print(recv)
if recv1[:3] != '221':
    print('221 reply not received from server.')
clientSocket.close()
