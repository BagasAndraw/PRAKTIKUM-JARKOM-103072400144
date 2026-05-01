# Modul 7 - SOCKET PROGAMMING
## Deskripsi 
Socket programming adalah teknik dalam pemrograman komputer yang digunakan untuk memungkinkan dua perangkat (biasanya melalui jaringan seperti internet) saling berkomunikasi menggunakan socket sebagai titik akhir koneksi. Secara sederhana, socket bisa dibayangkan seperti “pintu komunikasi” antara dua program. Melalui socket, data bisa dikirim dan diterima, baik dalam satu komputer maupun antar komputer yang berbeda.

## Penerapan TCP
## TCP client
```python
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
```

## TCP Server
```python
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
```

## Output Simulasi TCP

![hasil](../assests/image/Week7(3).png)

## Alur TCP

1. Server dijalankan & listen
2. Client dijalankan & connect ke server
3. Server menerima koneksi
4. Client kirim pesan
5. Server terima & proses pesan
6. Server kirim balasan
7. Client terima balasan
8. Ulangi sampai “exit”
9. Koneksi ditutup

## Penerapan UDP
## UDP Client
```python
from socket import *
import sys

# Konfigurasi alamat dan port server
serverName = '10.217.0.110'
serverPort = 12000

# Inisialisasi socket UDP di luar loop agar tidak dibuat berulang-ulang
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)  # Batas waktu tunggu 5 detik

print("Ketik 'exit' untuk mematikan server dan keluar, atau 'keluar' untuk tutup client saja.\n")

try:
    while True:
        # Input pesan dari pengguna
        message = input('Masukkan kalimat lowercase : ')
        
        # Validasi jika input kosong
        if not message:
            continue

        # Mengirim pesan ke server
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        
        # Cek apakah pengguna ingin keluar
        if message.lower() == 'exit':
            print("Perintah exit dikirim. Mematikan server dan menutup klien...")
            break
        elif message.lower() == 'keluar':
            print("Menutup klien...")
            break
        
        try:
            # Menerima balasan dari server
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print(f"Balasan dari Server: {modifiedMessage.decode()}\n")
        except timeout:
            print("Kesalahan : Server tidak merespons (Timeout).\n")

except Exception as e:
    print(f"Terjadi kesalahan : {e}")
finally:
    # Menutup koneksi socket secara permanen saat loop berhenti
    clientSocket.close()
    print("Koneksi ditutup.")
```

## UDP Server
```python
from socket import *
import sys

# Konfigurasi server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print(f"Server UDP siap menerima pesan pada port {serverPort}")
print("Ketik 'exit' dari sisi klien untuk mematikan server secara remote.\n")

try:
    while True:
        # Menerima pesan dari klien
        message, clientAddress = serverSocket.recvfrom(2048)
        
        # Mendekode pesan
        original_message = message.decode().strip()
        
        # Cek apakah pesan adalah perintah untuk keluar
        if original_message.lower() == 'exit':
            print(f"Mematikan server...")
            break
        
        # Mengubah pesan menjadi huruf kapital
        modifiedMessage = original_message.upper()
        
        # Menampilkan informasi klien dan isi pesan
        print(f"Diterima dari {clientAddress[0]}:{clientAddress[1]}: {original_message}")
        print(f"Mengirim balik : {modifiedMessage}")
        
        # Mengirim kembali pesan yang telah diubah ke klien
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        
except Exception as e:
    print(f"\nTerjadi kesalahan : {e}")
finally:
    print("Server telah berhenti.")
    serverSocket.close()
    sys.exit(0)
```

## Output Simulasi UDP

![hasil](../assests/image/Week7(2).png)

## Alur UDP

1. Server dijalankan & bind ke port
2. Server menunggu pesan (recvfrom)
3. Client dijalankan
4. Client kirim pesan ke server (sendto)
5. Server menerima pesan + alamat client
6. Server proses (ubah ke huruf besar)
7. Server kirim balasan ke client (sendto)
8. Client menerima balasan (recvfrom)
9. Ulangi sampai “exit”
10. Socket ditutup

## Kesimpulan

Pada percobaan yang dilakukan, TCP menggunakan koneksi terlebih dahulu (connection-oriented), sehingga komunikasi antara client dan server berjalan lebih stabil dan terjamin. Data yang dikirim pasti diterima dan diproses secara berurutan. Namun, prosesnya sedikit lebih kompleks karena harus melalui tahap koneksi.
UDP tidak memerlukan koneksi (connectionless), sehingga pengiriman data lebih sederhana dan cepat. Client bisa langsung mengirim pesan ke server tanpa proses awal. Namun, UDP tidak menjamin data diterima, sehingga bisa terjadi timeout jika server tidak merespons atau alamat tujuan salah.