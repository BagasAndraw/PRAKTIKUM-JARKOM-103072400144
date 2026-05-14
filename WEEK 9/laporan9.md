# Modul 9 - WEB SERVER
## Pengantar
Pada modul ini, akan mempelajari dasar pemrograman socket TCP menggunakan Python dengan membuat web server sederhana yang dapat menerima permintaan HTTP, mengirimkan file HTML kepada client, serta menampilkan pesan “404 Not Found” jika file tidak tersedia. Praktikan juga akan menjalankan server menggunakan alamat IP dan port tertentu, kemudian mengaksesnya melalui browser untuk memastikan server berhasil menampilkan halaman web yang diminta.

## Deskripsi
Web server adalah perangkat lunak atau sistem yang berfungsi untuk menerima, memproses, dan merespons permintaan (request) dari klien melalui jaringan, biasanya menggunakan protokol HTTP atau HTTPS. Ketika pengguna mengakses suatu alamat website melalui browser, web server akan mencari sumber daya yang diminta, seperti file HTML, gambar, atau data lainnya, kemudian mengirimkannya kembali sebagai respons agar dapat ditampilkan kepada pengguna. Web server juga dapat menangani berbagai kondisi, seperti kesalahan akses atau file yang tidak ditemukan, serta menjadi komponen utama dalam komunikasi antara pengguna dan aplikasi berbasis web. 

## 9.5 Skeleton Kode Python Untuk Web Server

```python
#import socket module 
from socket import * 
import sys # In order to terminate the program 

serverSocket = socket(AF_INET, SOCK_STREAM)

print ("Web server is running...")
#Prepare a server socket 
#Fill in start 
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end 

while True: 
    #Establish the connection 
    print('Ready to serve...') 
    
    connectionSocket, addr = serverSocket.accept()
    
    try: 
        message = connectionSocket.recv(1024).decode()
        
        filename = message.split()[1]                
        f = open(filename[1:])                         
        outputdata = f.read()

        #Send one HTTP header line into socket 
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):            
            connectionSocket.send(outputdata[i].encode()) 
        
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 

    except IOError: 
        #Send response message for file not found 
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send(
            "<html><body><h1>404 Not Found</h1></body></html>".encode()
        )

        #Close client socket 
        connectionSocket.close() 

serverSocket.close() 
sys.exit()  #Terminate the program after sending the corresponding data
```
Perubahan pada skeleton code dilakukan dengan melengkapi bagian yang kosong agar web server dapat berjalan. Penambahan bind() dan listen() digunakan untuk menjalankan server pada port tertentu, sedangkan accept() dipakai untuk menerima koneksi client. Request HTTP diterima menggunakan recv(), kemudian server membaca file HTML yang diminta dan mengirimkannya kembali ke browser disertai header HTTP/1.1 200 OK. Selain itu, ditambahkan penanganan error 404 Not Found jika file yang diminta tidak tersedia, serta close() untuk menutup koneksi setelah proses selesai.
### Jalankan Program

![hasil](../assests/image/Week9(1).png)
Lalu buka browser ketik localhost:6789/index.html

![hasil](../assests/image/Week9(2).png)

 file tidak ditemukan (IOError) karena belum membuat file .html, server mengirimkan 404 Not Found beserta halaman HTML sederhana sebagai respons.

Buat file index.html
```html
<!DOCTYPE html>
<html>
    <h1>
        hello word
    </h1>
</html>
```
Selanjutnya jalankan ulang skeleton.py ,lalu buka browser lagi.
### Hasil Output
![hasil](../assests/image/Week9(3).png)

File index.html berhasil ditampilkan pada browser sehingga menunjukkan bahwa web server telah berjalan dengan baik.

## 9.6 Latihan Tambahan

### 1. Multithreaded Web Server
Dengan metode multithreading, setiap koneksi client akan diproses pada thread terpisah sehingga server dapat melayani beberapa request secara paralel. Pendekatan ini meningkatkan responsivitas server dan membuat proses komunikasi client-server menjadi lebih efisien.

### Implementasi Code (server.py)
```python
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
```

### Jalankan Program
![hasil](../assests/image/Week9(4).png)

### Hasil Output
![hasil](../assests/image/Week9(3).png)

File index.html berhasil ditampilkan menggunakan multithreaded web server. Hasil tampilan pada browser serupa dengan skeleton web server pada sebelumnya, namun pada implementasi ini setiap koneksi client diproses menggunakan thread terpisah sehingga server dapat melayani beberapa client secara bersamaan.

### 2. HTTP Client (client.py)
Selain itu, pada latihan ini juga menggunakan HTTP client sederhana tanpa menggunakan browser. Client akan terhubung ke server menggunakan socket TCP, kemudian mengirim request HTTP metode GET untuk meminta file index.html dari server.
```python
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
```

### Jalankan Program

Sebelum menjalankan client, terlebih dahulu jalankan server.py, lalu jalan client menggunakan perintah,

```
python client.py localhost 6789 index.html
```

### Hasil Output
![hasil](../assests/image/Week9(5).png)

Berdasarkan output di atas, munculnya tulisan "/index.html" pada terminal server.py menunjukkan bahwa server berhasil menerima request HTTP dari browser untuk mengakses file index.html. Selanjutnya, HTTP client berhasil terhubung ke server menggunakan socket TCP dan mengirim request HTTP GET untuk meminta file tersebut. Server kemudian memberikan respons HTTP/1.1 200 OK yang menandakan bahwa request berhasil diproses dan file yang diminta berhasil ditemukan pada server. Hal ini menunjukkan bahwa komunikasi antara client dan web server telah berjalan dengan baik.



