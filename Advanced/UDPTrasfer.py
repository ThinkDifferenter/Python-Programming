from socket import *
from time import ctime

def server():
    print("=====================时间戳UDP服务器=====================");

    HOST = '127.0.0.1'   #主机号为空白表示可以使用任何可用的地址。
    PORT = 21567  #端口号
    BUFSIZ = 1024  #接收数据缓冲大小
    ADDR = (HOST, PORT)

    udpSerSock = socket(AF_INET, SOCK_DGRAM) #创建udp服务器套接字
    udpSerSock.bind(ADDR)  #套接字与地址绑定

    while True:
        print('等待接收消息...')
        data, addr = udpSerSock.recvfrom(BUFSIZ) #连续接收指定字节的数据，接收到的是字节数组
        udpSerSock.sendto(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'), addr)  #向客户端发送时间戳数据，必须发送字节数组
        print('响应消息到', addr)
        print('响应消息为', str(data,'utf-8')
        

    udpSerSock.close()  #关闭服务器socket



def client():
    print("=====================UDP客户端=====================");

    HOST = '127.0.0.1'   #本机测试
    PORT = 21567  #端口号
    BUFSIZ = 1024  #接收消息的缓冲大小
    ADDR = (HOST, PORT)

    udpCliSock = socket(AF_INET, SOCK_DGRAM) #创建客户端套接字

    while True:
        data = input('> ')  #接收用户输入
        if not data:   #如果用户输入为空，直接回车就会发送""，""就是代表false
            break
        udpCliSock.sendto(bytes(data,'utf-8'), ADDR)  #客户端发送消息，必须发送字节数组
        data, ADDR = udpCliSock.recvfrom(BUFSIZ)  #接收回应消息，接收到的是字节数组
        if not data:   #如果接收服务器信息失败，或没有消息回应
            break
        print(str(data,'utf-8'))  #打印回应消息

    udpCliSock.close()#关闭客户端socket


if __name__=='__main__':
    server()


