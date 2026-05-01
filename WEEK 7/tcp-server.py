from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# meng bind server 
serverSocket.bind (
    ('', serverPort)
)

# server siap menerima koneksi
serverSocket.listen(1)
print ("[SYSTEM] server TCP siap digunakan")

running = True 
while running:

    # menyetujui koneksi dari client
    connectionSocket, addr = serverSocket.accept()

    while True:
        # pesan yang diterima = 10101010101
        message = connectionSocket.recv(2048).decode()

        if not message:
            break

        #cek apakah "exit" ?
        if message.lower() == "exit":
            print ("[SYSTEM] client ingin keluar")
            running = False
            break

        # memodifikasi menjadi capslock
        modifiedMessage = message.upper()
        print("[SERVER] diterima: ", modifiedMessage)

        #kirim ke client
        connectionSocket.send(
            modifiedMessage.encode()
        )

    connectionSocket.close()

serverSocket.close()