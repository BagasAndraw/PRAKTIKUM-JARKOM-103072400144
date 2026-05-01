# SOCKET = penjumlahan, pengurangan, pembagian, perkalian
from socket import *    # Import All

serverName = "localhost"
serverPort = 12000

# AF_INET = ipv4 | SOCK_STREAM = TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# hubungan | connect 
clientSocket.connect(
    (serverName, serverPort)
)

print ("[SYSTEM] Masukkan pesan")

running = True
while running:

    # INPUT
    message = input("> ")

    # mengirim ke server 
    #encode = abcde = 101010101
    clientSocket.send(message.encode())

    #kalo exit = socket ditutup
    if message.lower() == "exit":
        print("[SYSTEM] keluar dari program")
        running = False
        break 

    # menerima pesan dari server
    # abc = 10101010101
    modifiedMessage = clientSocket.recv(2048)

    print ("[SERVER] pesan: ", modifiedMessage.decode())

# menutup socket yang tidak dipakai
clientSocket.close()
print ("[SYSTEM] socket ditutup")