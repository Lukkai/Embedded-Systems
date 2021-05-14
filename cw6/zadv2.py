import socket

# create an INET, STREAMing socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# connect to the web server on port 80 - the normal http port
    s.connect(("example.com" , 80))
# sends a HTTP request to host
    s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\nAccept: text/html\r\n\r\n")
# This reads whatever data the client sends
    request = str(s.recv(4096), 'utf-8')
# print request answer and write to file
    print("GET request: {}".format(request))
    with open("request.txt", "w") as f:
        f.write(request)