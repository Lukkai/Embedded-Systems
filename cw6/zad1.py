import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("google.com" , 80))
    s.sendall(b"GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")
    dostane = str(s.recv(4096), 'utf-8')
    with open("twojastara.txt", "w") as f:
        f.write(dostane)