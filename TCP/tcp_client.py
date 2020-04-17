import socket

#创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建连
s.connect(("www.sina.com.cn",80))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据
buffer = []
while True:
    #每次最多接收1K数据
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
#关闭连接
s.close()

#查看接收到的内容
header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
print("*"*50)
print(html.decode("utf-8"))
#把接收的数据写入文件
