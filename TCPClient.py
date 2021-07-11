from socket import *

serverName = '主机ip'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)         # 底层网络IPv4，TCP套接字
clientSocket.connect((serverName, serverPort))      # 建立连接
sentence = input("Input a lowercase sentence:\n")   
clientSocket.send(sentence.encode())                         # 通过套接字进入TCP连接发送sentence
modifiedSentence = clientSocket.recv(2048)
print('From server:', modifiedSentence.decode())
clientSocket.close()
