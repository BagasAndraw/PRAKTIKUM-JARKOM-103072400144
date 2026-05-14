from socket import *
import threading

def handle_client(connectionSocket):
    try:
        # menerima pesan user
        # 1010101010 = "message" 
        message = connectionSocket.recv(1024). decode()

        # message = /GET /index.html HTTP/1.1
        message = message[4:15]
        print(message)
        # index.html, hello.html
        # filename = message.split()[1]

        # membuka index.html serta menghilangkan "/"
        f = open(message[1:])
        
        # membaca file html
        outputData = f.read()

        # kirim respon
        connectionSocket.send(
            "HTTP/1.1 200 OK\r\n\r\n".encode()
        )

        # kirim data
        connectionSocket.sendall(outputData.encode())

        # tutup koneksi 
        connectionSocket.close()
    
    except IOError:
        # kirim respon bila tidak ditemukan
        connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\n\r\n".encode()
        )

        # kirim data 404
        connectionSocket.send(
            "<h1>404 Not Found</h1>".encode()
        )

        # tutup koneksi
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',6789))
serverSocket.listen(5)      # dapat menerima sebanyak 5 client
print("[SYSTEM] server is running ...")

while True:
    connectionSocket, addr = serverSocket.accept()
    
    #membuat dan tujuan target thread nya, beserta parameter
    thread = threading.Thread(
        target=handle_client,
        args=(connectionSocket,)
        )
    
    #menjalankan
    thread.start()
