from socket import *  # import socket
from datetime import *  # import date and time

# Ask the user to enter URL server
URLServer = input("--- Enter The Website: ")
serverPort = 80  # defined the port on 80
clientSocket = socket(AF_INET, SOCK_STREAM)  # create the client's socket
# TCP connection must be established between the client and server
# after that the client can send data to server(or vice versa) using a TCP socket
clientSocket.connect((URLServer, serverPort))
# print the date and time at that moment before sending the request
print(datetime.now())
clientSocket.send("HEAD / HTTP/1.1\r\n".encode())  # HEAD method of
# HTTP to get HTTP response from a specific webserver
# send sentence through the client's socket and into the TCP connection
clientSocket.send("Hostname:URLServer \r\n\r\n".encode())
# take the response time before the response of the connection
response_time_before = datetime.now()
modifiedSentence = clientSocket.recv(1024)
# take the response time before the response of the connection
response_time_after = datetime.now()
# final response time will be the subtraction between time before from time after
final_response_time = response_time_after - response_time_before
print("response_time: ", final_response_time)
print("from server: ", modifiedSentence.decode())
clientSocket.close()  # close socket
