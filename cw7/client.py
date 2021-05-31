import socket

    
HOST = ''
PORT = 2200
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print('Socket created')

    while True:
        msg = input()
        s.send(bytes(msg,"utf-8"))
        data = s.recv(1024)
        print(data.decode("UTF-8"))
        if msg.upper() == "END":
            print('.Connection closed')
            break
    s.close()