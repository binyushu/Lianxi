# -*-coding:utf-8-*-

import socket

clinet = socket.socket()
clinet.connect(("192.168.1.1", 8080))
data = input("请输入你要发送的数据：\n")
clinet.send(data.encode("utf-8"))
clinet.close()
