from socket import *

serverName = '主机ip'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)                      # 底层网络IPv4，UDP套接字
sentence = input("Input a lowercase sentence:\n")   
clientSocket.sendto(sentence.encode(), (serverName, serverPort))         # 发送时附上目的地址
modifiedSentence, serverAddress = clientSocket.recvfrom(2048)   # 取缓存长度2048作为输入
print('From server:', modifiedSentence.decode())
clientSocket.close()
