# Modul 11 - DHCP

## Pengantar 
Pada modul ini membahas tentang Dynamic Host Configuration Protocol (DHCP), yaitu protokol jaringan yang digunakan untuk memberikan alamat IP secara otomatis kepada perangkat yang terhubung dalam suatu jaringan. Pada praktikum ini, mahasiswa mempelajari konsep dasar DHCP serta cara kerja proses pertukaran pesan DHCP menggunakan aplikasi Wireshark.

Melalui modul ini, mahasiswa melakukan pengamatan terhadap proses komunikasi DHCP yang terjadi ketika sebuah host meminta konfigurasi jaringan dari server DHCP. Proses tersebut meliputi tahapan DHCP Discover, Offer, Request, dan Acknowledgement (DORA). Dengan menggunakan Wireshark, mahasiswa dapat menangkap, menganalisis, dan menelusuri paket-paket DHCP yang dikirimkan dalam jaringan.

## Cara Kerja DHCP

DHCP bekerja dengan mekanisme pertukaran pesan antara DHCP Client (perangkat yang meminta alamat IP) dan DHCP Server (perangkat yang menyediakan alamat IP). Proses ini dikenal sebagai **DORA (Discover, Offer, Request, Acknowledge).**

1. DHCP Discover

    Ketika sebuah perangkat terhubung ke jaringan, perangkat tersebut mengirimkan pesan DHCP Discover secara broadcast untuk mencari DHCP Server yang tersedia.

2. DHCP Offer

    DHCP Server yang menerima pesan Discover akan membalas dengan DHCP Offer, yang berisi penawaran alamat IP beserta informasi konfigurasi jaringan lainnya, seperti subnet mask, gateway, dan DNS.

3. DHCP Request

    Setelah menerima penawaran, client memilih salah satu alamat IP yang ditawarkan dan mengirimkan pesan DHCP Request kepada server sebagai tanda bahwa alamat IP tersebut ingin digunakan.

4. DHCP Acknowledge (ACK)

    DHCP Server kemudian mengirimkan pesan DHCP ACK untuk mengonfirmasi bahwa alamat IP tersebut telah diberikan kepada client. Setelah menerima ACK, client dapat menggunakan alamat IP tersebut untuk berkomunikasi di jaringan.

## Langkah Percobaan

### 1. Cek Konfigurasi IP

Sebelum melakukan analisis DHCP, cek IP pada device yang kalian gunakan, dengan menggunakan perintah berikut pada cmd.
```
ipconfig
```

Berikut hasil pencarian IP pada cmd :

![hasil](../assests/image/Week11(1).png)

Berdasarkan hasil perintah ipconfig, perangkat terhubung ke jaringan melalui adapter Wi-Fi dengan alamat IPv4 192.168.1.6, subnet mask 255.255.255.0, dan default gateway 192.168.1.1. Konfigurasi ini menunjukkan bahwa perangkat berada pada jaringan 192.168.1.0/24 dan kemungkinan memperoleh alamat IP secara otomatis dari DHCP Server yang terdapat pada router dengan alamat 192.168.1.1.

### 2. Konfigurasi DHCP Melalui Network Properties
Untuk memastikan komputer menggunakan DHCP, dapat dicek melalui pengaturan jaringan Windows. Buka Network Connections → Wi-Fi Properties → Internet Protocol Version 4 (TCP/IPv4) → Properties.

Berikut tampilan pengaturan IPv4 yang menunjukkan komputer dikonfigurasi untuk mendapatkan IP secara otomatis:

![hasil](../assests/image/Week11(2).png)

Opsi "Obtain an IP address automatically" dan "Obtain DNS server address automatically" menunjukkan bahwa komputer dikonfigurasi untuk memperoleh alamat IP dan informasi DNS secara dinamis dari DHCP Server setiap kali terhubung ke jaringan. Dengan konfigurasi ini, pengguna tidak perlu mengatur alamat IP secara manual karena seluruh parameter jaringan akan diberikan secara otomatis oleh server DHCP.

### 3. Analisis paket DHCP pada Wireshark

Buka file yang telah diberikan yang bernama berikut ini pada wireshark:
```
dhcp-ethereal-trace-1
```
Kemudian lakukan filtering dengan perintah "dhcp" pada wireshark, berikut hasilnya :

![hasil](../assests/image/Week11(3).png)

Berdasarkan hasil tangkapan paket pada Wireshark, terlihat bahwa proses DHCP berlangsung sesuai mekanisme DORA (Discover, Offer, Request, Acknowledge). Pada paket nomor 2, client dengan alamat sumber 0.0.0.0 mengirimkan DHCP Discover ke alamat broadcast 255.255.255.255 untuk mencari DHCP Server. Selanjutnya, DHCP Server dengan alamat 192.168.1.1 merespons melalui DHCP Offer pada paket nomor 4 dengan menawarkan alamat IP kepada client. Pada paket nomor 5, client mengirimkan DHCP Request sebagai permintaan untuk menggunakan alamat IP yang ditawarkan, dan proses diakhiri dengan DHCP ACK pada paket nomor 6 sebagai konfirmasi dari server bahwa alamat IP telah diberikan. Urutan paket tersebut menunjukkan bahwa proses alokasi alamat IP secara dinamis oleh DHCP Server berhasil dilakukan sesuai prosedur standar DHCP.


 