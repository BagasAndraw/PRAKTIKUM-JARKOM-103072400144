from socket import *
import sys

# command line:
# python client.py localhost 6789 index.html

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

# membuat socket client
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect ke server
clientSocket.connect((server_host, server_port))

# membuat HTTP GET request
request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"

# kirim request
clientSocket.send(request.encode())

# menerima response
response = clientSocket.recv(4096)

# tampilkan response
print(response.decode())

# tutup socket
clientSocket.close()