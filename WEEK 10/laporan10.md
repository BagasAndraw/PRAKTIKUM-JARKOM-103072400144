# Modul 10 - IP
## Deskripsi
Pada modul ini mahasiswa diminta memahami konsep IP Address beserta perbedaan IPv4 dan IPv6, melakukan traceroute pada sebuah website untuk melihat jalur paket data, serta menjelaskan fungsi ICMP, MTU, dan TTL dalam proses komunikasi jaringan. Selain itu, mahasiswa juga harus melakukan capture paket menggunakan Wireshark untuk menemukan contoh fragmentasi paket dan lalu lintas IPv6
## 1. Apa itu IP adress?
IP Address (Internet Protocol Address) adalah alamat unik yang berbeda setiap device yang digunakan untuk mengidentifikasi perangkat dalam suatu jaringan komputer, baik jaringan lokal maupun internet. IP Address berfungsi sebagai identitas dan alamat tujuan agar data dapat dikirim dan diterima dengan benar antar perangkat.

Untuk memeriksa IP pada laptop, gunakan perintah "ipconfig" (windows) pada command prompt
```
ipconfig
```
![hasil](../assests/image/Week10(1).png)

Secara umum, IP Address terbagi menjadi dua versi, yaitu :

- IPv4 yang menggunakan format angka 32-bit seperti 192.168.43.121
- IPv6 yang menggunakan format 128-bit seperti fe80::ebb6:76a9:7f3e:cd40%13

dibuat untuk mengatasi keterbatasan jumlah alamat pada IPv4.

## 2. Traceout pada suatu website
Jalankan Traceout melalui Command Prompt (windows) dengan perintah :
```
> tracert gaia.cs.umass.edu 
``` 
Hasil Traceout :

![hasil](../assests/image/Week10(2).png)

Contoh Traceout pada website lain, misal youtube.com

![hasil](../assests/image/Week10(3).png)

Berdasarkan hasil traceroute di atas, paket data menuju gaia.cs.umass.edu [128.119.245.12] melewati sekitar 29 hop, sedangkan menuju youtube.com [74.125.130.91] melewati sekitar 23 hop sebelum mencapai tujuan. Beberapa hop menampilkan tanda * atau Request timed out yang menandakan router tidak merespons permintaan ICMP, namun hal tersebut normal terjadi karena beberapa router dikonfigurasi untuk membatasi respons demi keamanan jaringan.

## 3. Apa itu ICMP, MTU, TTL
### ICMP (Internet Control Message Protocol)
ICMP adalah protokol jaringan yang digunakan untuk mengirim pesan kontrol dan informasi kesalahan dalam komunikasi data, contohnya pada perintah ping dan traceroute.

### MTU (Maximum Transmission Unit) 
MTU adalah ukuran maksimum paket data yang dapat dikirim melalui jaringan dalam satu kali transmisi tanpa perlu fragmentasi. Semakin besar nilai MTU, semakin banyak data yang dapat dikirim sekaligus.

### TTL (Time To Live) 
TTL adalah batas jumlah hop atau router yang dapat dilewati paket data di jaringan. Nilai TTL akan berkurang setiap kali paket melewati router, dan jika nilainya habis maka paket akan dibuang untuk mencegah terjadinya looping pada jaringan.

## Percobaan Pada Wireshark
Buka file abc.pcapng yang telah disediakan, buka di Wireshark, kemudian lakukan filter dengan memasukkan "ICMP"

![hasil](../assests/image/Week10(4).png)

Pilih salah satu packet yang berisi pesan Time-to-live exceeded, analisis pada Internet Control Message Protocol, terdapat Type: Time-to-live exceeded (11) yang berarti paket data gagal mencapai tujuan karena nilai TTL telah habis saat melewati router di jaringan. Pada packet tersebut terlihat alamat IP asal (Source) adalah 192.168.100.1 dan alamat IP tujuan (Destination) adalah 192.168.100.133. Hal ini menunjukkan router mengirimkan pesan ICMP kembali ke pengirim karena paket sebelumnya tidak dapat diteruskan akibat nilai TTL mencapai 0.

## 4. Cari contoh fragmentasi di wireshark kalian   

Melakukan fragmentasi pada percobaan sebelumnya, ketik di filter dengan memasukkan perintah :
```
ip.frag_offset > 0
```
![hasil](../assests/image/Week10(5).png)

Pada percobaan file sebelumnya tidak terdapat fragmentasi yang offset, maka dari itu melakukan percobaan ke website lain, sebelum ke langkah selanjutnya, lakukan capturing ulang di wireshark, memilih jaringan wifi, kemudian buka cmd dengan ketik perintah :

```
ping youtube -l 4000
```

![hasil](../assests/image/Week10(6).png)

Pada pengujian sebelumnya fragmentasi tidak muncul karena ukuran paket masih sesuai dengan batas MTU jaringan. Setelah ukuran paket diperbesar menjadi 4000 byte, paket dipecah menjadi beberapa bagian agar dapat dikirim melalui jaringan. Hal ini terlihat dari adanya informasi Fragmented IP protocol, nilai off=1480, dan status Reassembled in yang menunjukkan paket berhasil disusun kembali oleh Wireshark.

## 5. Carilah IPv6 di Wireshark kalian lakukan
IPv6 (Internet Protocol Version 6) adalah versi terbaru dari protokol Internet Protocol yang digunakan untuk memberikan alamat pada perangkat di jaringan komputer dan internet. IPv6 dikembangkan sebagai pengganti IPv4 karena jumlah alamat IPv4 semakin terbatas akibat meningkatnya penggunaan perangkat yang terhubung ke internet.

Alamat IPv6 ditulis dalam format heksadesimal yang dipisahkan tanda titik dua (:), contohnya fe80::1 atau 2001:4860:4860::8888.

![hasil](../assests/image/Week10(7).png)

Melakukan analisis pada file sebelumnya yang telah disediakan, berdasarkan hasil capture Wireshark menggunakan filter ipv6, ditemukan beberapa paket IPv6 yang didominasi oleh protokol ICMPv6, mDNS, dan LLMNR dengan alamat lokal seperti fe80::. Pada capture terlihat aktivitas Neighbor Solicitation, Neighbor Advertisement, dan Router Solicitation yang digunakan perangkat untuk komunikasi dalam jaringan IPv6. Paket IPv6 muncul karena adanya aktivitas jaringan pada device, seperti komunikasi sistem operasi dan layanan jaringan otomatis Windows, sehingga Wireshark berhasil menangkap trafik IPv6 meskipun sebelumnya filter ipv6 belum menampilkan hasil.