import socket

    
HOST = ''
PORT = 2200
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    print('Socket created')

    while True:
        msg = input()
        sock.send(bytes(msg,"utf-8"))
        if msg.upper() == "END":
            print('.Connection closed')
            break
        data = sock.recv(1024)
        print("Result: " + data.decode("UTF-8"))
    sock.close()