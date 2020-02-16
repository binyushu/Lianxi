# -*-coding:utf-8-*-

import socket
import threading


# 获取客户端连接并启动线程去处理
def handl_sock(sokc, addr):
    while True:
        tmp_data = new_socket.recv(1024)
        print(tmp_data.decode("utf-8"))
        input_data = input()
        new_socket.send(input_data.encode("utf-8"))


#创建套接字
server = socket.socket()

#绑定IP和端口
server.bind(("", 8080))

#让默认的套接字由主动变为被动listen
server.listen()

#等待客户连接，阻塞
new_socket, new_addr = server.accept()


clinet_thread = threading.Thread(target=handl_sock,args=(new_socket,new_addr))
clinet_thread.start()








# print(data)
# new_socket.close()
