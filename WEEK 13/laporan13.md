# Modul 13 - Ethernet dan ARP

## PENGANTAR
Modul ini membahas konsep dasar Ethernet dan Address Resolution Protocol (ARP) dalam jaringan komputer. Ethernet merupakan teknologi komunikasi data yang digunakan untuk menghubungkan perangkat-perangkat dalam jaringan lokal (LAN) serta mengatur proses pengiriman dan penerimaan data antar perangkat. Sementara itu, ARP merupakan protokol yang berfungsi untuk menerjemahkan alamat IP menjadi alamat fisik (MAC Address) sehingga data dapat dikirim ke perangkat tujuan dengan benar. Melalui pembahasan ini, diharapkan dapat dipahami peran Ethernet sebagai media komunikasi pada lapisan data link dan fungsi ARP sebagai penghubung antara alamat logis dan alamat fisik dalam proses komunikasi jaringan komputer.

## PENGERTIAN
## 1. Ethernet
teknologi jaringan yang digunakan untuk menghubungkan perangkat-perangkat seperti komputer, printer, server, dan switch dalam sebuah jaringan lokal (LAN). Fungsi dari ethernet ini adalah sbg berikut :
* Mengirim dan menerima data antar perangkat dalam jaringan.
* Menentukan format data yang dikirim melalui kabel jaringan.
* Menggunakan alamat fisik yang disebut MAC Address untuk mengidentifikasi setiap perangkat.
### Cara kerja Ethernet
1. Komputer membuat data yang akan dikirim.
2. Data dibungkus menjadi frame Ethernet.
3. Frame berisi:
MAC Address sumber
MAC Address tujuan
Data
4. Informasi pengecekan kesalahan
Frame dikirim melalui media jaringan (kabel UTP atau fiber).
5. Perangkat tujuan menerima dan memproses data tersebut.

## 2.  ARP (Address Resolution Protocol)
protokol yang digunakan untuk mencari MAC Address berdasarkan IP Address dalam jaringan lokal. ARP diperlukan karena saat sebuah komputer ingin mengirim data ke IP tertentu, Ethernet membutuhkan MAC Address tujuan. Jika MAC Address belum diketahui, komputer menggunakan ARP untuk mencarinya.

### Cara Kerja ARP
Misalnya:  
Komputer A: IP 192.168.1.10  
Komputer B: IP 192.168.1.20

1. Komputer A ingin mengirim data ke 192.168.1.20.
2. Komputer A memeriksa ARP Cache.

3. Jika MAC Address belum ada, Komputer A mengirim ARP Request ke seluruh jaringan:  
"Siapa yang memiliki IP 192.168.1.20?"

4. Komputer B menjawab dengan ARP Reply:  
"Saya memiliki IP 192.168.1.20, MAC Address saya AA:BB:CC:DD:EE:FF."  
5. Komputer A menyimpan informasi tersebut di ARP Cache.
6. Data kemudian dikirim menggunakan frame Ethernet ke MAC Address Komputer B.

## LANGKAH PERCOBAAAN

## 1. Melakukan Caching ARP

Buka CMD pada device, pilih Run as Administrator, lalu ketik perintah:

```cmd
arp -d *
```

Perintah tersebut berfungsi untuk menghapus seluruh data cache ARP (Address Resolution Protocol) yang tersimpan di dalam komputer Anda.

## 2. Protocol Disabling IPv4 pada wireshark

Selanjutnya buka wireshark, pilih tab Analyze &rarr; Enable Protocols, lalu filter ip dan cari ipv4, kemudian nonaktifkan pada IPv4

![hasil](../assests/image/Week13(1).png)

Langkah ini guna untuk mengabaikan IPv4 pada capturing wireshark, agar mudah melakukan pencarian Broadcasting pada wireshark

## 3. Mengamati Aksi ARP

Kosongkan cache ARP , seperti yang dijelaskan di atas, dengan mengetik perintah pada cmd


    arp –d 
    
 Kemudian masukkan URL berikut ke dalam browser
  ```   
http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-lab-file3.html\
 ```
 Langkah selanjutnya kembali ke wireshark, lakukan filtering dengan ketik perintah "arp"

 ![hasil](../assests/image/Week13(3).png)

 Berdasarkan hasil capture menggunakan Wireshark dengan filter ARP, teramati paket ARP Request yang dikirim secara broadcast oleh host dengan alamat IP 192.168.18.12 dan MAC Address 60:ff:9e:ae:fa:a6. Pada kolom Info terlihat pesan "Who has 192.168.18.36? Tell 192.168.18.12", yang menunjukkan bahwa host pengirim sedang mencari alamat MAC dari perangkat yang memiliki IP 192.168.18.36. Paket tersebut dikirim ke alamat broadcast ff:ff:ff:ff:ff:ff karena alamat MAC tujuan belum diketahui, yang juga ditunjukkan oleh nilai Target MAC Address sebesar 00:00:00:00:00:00. Selain itu, terlihat beberapa ARP Request lain yang ditujukan ke alamat IP 192.168.18.10, 192.168.18.21, dan 192.168.18.83, menandakan bahwa host 192.168.18.12 sedang melakukan proses pencarian atau pembaruan informasi alamat MAC beberapa perangkat dalam subnet yang sama. Hasil pengamatan ini menunjukkan mekanisme kerja ARP dalam menerjemahkan alamat IP menjadi alamat MAC sebelum proses komunikasi data dilakukan melalui Ethernet, sehingga perangkat dapat berkomunikasi secara langsung setelah alamat fisik tujuan berhasil diperoleh melalui ARP Reply.

    