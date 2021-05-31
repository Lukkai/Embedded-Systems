import socket
import ssl

def web_body(device):
    html = """<html>
    <head>
    <title>Device state</title>
    </head>
    <body>
    <p>State of device: <b>""" + device + """</b></p>
    <p><a href="/?on"><button class="button">Turn On</button></a></p>
    <p><a href="/?off"><button class="button2">Turn Off</button></a></p>
    </body>
    </html>"""
    html = bytes(html,"utf-8")
    return html


HOST = ''
PORT = 2200

device = "OFF"

with open("device.txt","r") as f:
    device = f.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    print('Socket is now listening')
    s.listen(15)
    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024).decode()
            print('Content = %s' % request)
            deviceOn = request.find('/?on')
            deviceOff = request.find('/?off')
            print(deviceOn)
            print(deviceOff)

            if deviceOn == 4:
                print('device ON')
                device = "ON"

            if deviceOff == 4:
                print('device OFF')
                device = "OFF"

            response = web_body(device)
            conn.send(b'HTTP/1.1 200 OK\n')
            conn.send(b'Content-Type: text/html\n')
            conn.send(b'Connection: close\n\n')
            conn.sendall(response)
            f = open("device.txt", "w")
            f.write(device)
            f.close()