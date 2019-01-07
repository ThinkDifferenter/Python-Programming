from socket import *
from time import ctime

def server():
    print("=====================时间戳TCP服务器=====================");

    HOST = '127.0.0.1'  #主机号为空白表示可以使用任何可用的地址。
    PORT = 21567  #端口号
    BUFSIZ = 1024  #接收数据缓冲大小
    ADDR = (HOST, PORT)

    tcpSerSock = socket(AF_INET, SOCK_STREAM) #创建TCP服务器套接字
    tcpSerSock.bind(ADDR)  #套接字与地址绑定
    tcpSerSock.listen(5) #监听连接，同时连接请求的最大数目

    while True:
        print('等待客户端的连接...')
        tcpCliSock, addr = tcpSerSock.accept()   #接收客户端连接请求
        print('取得连接:', addr)

        while True:
            data = tcpCliSock.recv(BUFSIZ)  #连续接收指定字节的数据，接收到的是字节数组
            if not data:  #如果数据空白，则表示客户端退出，所以退出接收
                break
            #tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
            tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8')) #向客户端发送时间戳数据，必须发送字节数组

        tcpCliSock.close()  #关闭与客户端的连接
    tcpSerSock.close()  #关闭服务器socket



def client():
    print("=====================TCP客户端=====================");

    HOST = '127.0.0.1'  #服务器ip地址，等价于localhost
    PORT = 21567  #通信端口号
    BUFSIZ = 1024  #接收数据缓冲大小
    ADDR = (HOST, PORT)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)  #创建客户端套接字
    tcpCliSock.connect(ADDR)  #发起TCP连接

    while True:
        data = input('> ')   #接收用户输入
        if not data:  #如果用户输入为空，直接回车就会发送""，""就是代表false
            break
        tcpCliSock.send(bytes(data, 'utf-8'))   #客户端发送消息，必须发送字节数组
        data = tcpCliSock.recv(BUFSIZ)   #接收回应消息，接收到的是字节数组
        if not data:   #如果接收服务器信息失败，或没有消息回应
            break
        print(data.decode('utf-8'))  #打印回应消息，或者str(data,"utf-8")

    tcpCliSock.close() #关闭客户端socket


if __name__=='__main__':
    
