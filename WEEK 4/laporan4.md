# Modul 4 - DNS #
Domain Name System (DNS) memiliki peran penting dalam infrastruktur internet, ia 
mentranslasikan nama host ke bentuk alamat IP. Pada modul ini, kita akan mempelajari lebih lanjut 
sisi klien DNS. Perlu diingat bahwa peran klien dalam DNS relatif sederhana - klien hanya 
mengirimkan permintaan ke server DNS lokal dan menerima respons balik. Banyak hal "di balik 
layar" yang tidak terlihat oleh klien DNS karena server DNS hirarkis berkomunikasi satu sama lain 
untuk menyelesaikan permintaan klien secara rekursif atau berulang-ulang.

## 4.2 Nslookup ##
## Langkah Percobaan ##

Buka command prompt atau cmd pada device kalian, lalu ketik "nslookup www.mit.edu". Berfungsi untuk melihat IP untuk host www.mit.edu

![hasil](../assests/image/Week4(1).png)

Lalu ketik "nslookup -type=NS mit.edu", untuk mengirimkan permintaan untuk record tipe-NS ke default server DNS lokal

![hasil](../assests/image/Week4(2).png)

Lalu ketik "nslookup www.aiit.or.kr bitsy.mit.edu", untuk mengirim permintaan ke server DNS bitsy.mit.edu

![hasil](../assests/image/Week4(3).png)

## Uji Pengamatan ##
1. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP 
server tersebut? 

    Ketik "nslookup www.nus.edu.sg" untuk mencari melihat IP Singapura. Dan terlihat IP address server Singapura pada berikut.  

    ![hasil](../assests/image/Week4(4).png)

2. Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa. 

    Ketik "nslookup -type=NS ox.ac.uk", untuk mengetahui server DNS otoritatif untuk Universitas Oxford

    ![hasil](../assests/image/Week4(5).png)

3. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! Mail 
melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya? 

    Melakukan menggunakan pengujian dengan perintah nslookup pada cmd. DNS server diatur ke 8.8.8.8, kemudian tipe query diubah menjadi MX untuk mencari mail server dari domain yahoo.com. Hasil menunjukkan beberapa mail server Yahoo 

![hasil](../assests/image/Week4(6).png)

Selanjutnya melakukan query dan memilih server mta5.am0.yahoodns.net. untuk mendapatkan alamat IP server tersebut, lalu hasilnya ada dibawah ini 

![hasil](../assests/image/Week4(7).png)

## 4.3 Ipconfig
## Langkah Percobaan ##
Ketik pada cmd "ipconfig/all" untuk menampilkan seluruh jaringan pada device kita, termasuk IP dan DNS.

![hasil](../assests/image/Week4(8).png)

Ketik "ipconfig/all > networkinfo.txt" di cmd, fungsinya sama seperti sebelumnya, tetapi akan menyimpan hasil jaringan keseluruhan di file pada device masing masing

![hasil](../assests/image/Week4(9).png)

![hasil](../assests/image/Week4(10).png)

Lalu ketik "ipconfig/displaydns" pada cmd. Berfungsi untuk menampilkan cache DNS pada device

![hasil](../assests/image/Week4(11).png)

Dan untuk menghapus DNS yang sudah dibuka atau digunakan dalam device, ketik "ipconfig/flushdns" pada cmd.

![hasil](../assests/image/Week4(12).png)

## 4.4 Tracing DNS dengan Wireshark
## Langkah Percobaan ##
Setelah mengenal nslookup dan ipconfig, kita siap untuk menyelesaikan permasalahan yang lebih 
serius. Pertama-tama, mari kita tangkap paket DNS yang dihasilkan oleh aktivitas penjelajahan web 
biasa.  
1. Buka cmd lalu ketik "IPCONFIG" untuk melihat IP pada laptop kita, lalu copy 

    ![hasil](../assests/image/Week4(13).png)

2. Buka wireshark, pilih jaringan wifi lalu filter dengan ketik  "ip.addr == <your_IP_address>" 
berisi ip yang telah dicari sebelumnya di cmd
![hasil](../assests/image/Week4(14).png)

3. Buka browser http://www.ietf.org, hentikan pemgambilan paket pada wireshark 

    ![hasil](../assests/image/Week4(15).png)

4. Untuk mencari domain ietf, tambahkan pada filter 'ip.addr == 192.168.1.10 && dns.qry.name 
contains "ietf"' 

    ![hasil](../assests/image/Week4(16).png)

## A. http://www.ietf.org ##
1. Cari pesan permintaan DNS dan balasannya. Apakah pesan tersebut dikirimkan melalui UDP 
atau TCP? 
![hasil](../assests/image/Week4(17).png)
    
    Dari hasil percobaan yang dilakukan, terdapat DNS menggunakan User Datagram Protocol (UDP)

2. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasannya?
![hasil](../assests/image/Week4(17).png)

    Destination Port : 53
    
    Source Port : 56419

3. Pada pesan permintaan DNS, apa alamat IP tujuannya? Apa alamat IP server DNS lokal anda 
(gunakan ipconfig untuk mencari tahu)? Apakah kedua alamat IP tersebut sama?
![hasil](../assests/image/Week4(18).png)
![hasil](../assests/image/Week4(19).png)

    Alamat IP tujuan pada pesan DNS adalah 172.25.16.1. Alamat IP DNS lokal (berdasarkan ipconfig) adalah 192.168.1.1. Keduanya tidak sama.

4. Periksa pesan permintaan DNS. Apa “jenis” atau ”type” dari pesan tersebut? Apakah pesan 
permintaan tersebut mengandung ”jawaban” atau ”answers”?

![hasil](../assests/image/Week4(20).png)

Jenis (type) dari pesan permintaan DNS adalah A (Host Address), dan pesan tersebut tidak mengandung jawaban karena nilai Answer RRs = 0.
 
5. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau ”answers” yang terdapat di 
dalamnya? Apa saja isi yang terkandung dalam setiap jawaban tersebut?

![hasil](../assests/image/Week4(21).png)

Jumlah jawaban (answers) pada pesan balasan DNS adalah 2. Setiap jawaban berisi alamat IP dari domain www.ietf.org, yaitu 104.16.45.99 dan 104.16.44.99.

6. Perhatikan paket TCP SYN yang selanjutnya dikirimkan oleh host Anda. Apakah alamat IP 
pada paket tersebut sesuai dengan alamat IP yang tertera pada pesan balasan DNS? 
![hasil](../assests/image/Week4(22).png)

    Ya, alamat IP pada paket TCP SYN sesuai dengan alamat IP yang tertera pada pesan balasan DNS,dapat dilihat dari nomor sebelumnya, yaitu 104.16.44.99.

7. Halaman web yang sebelumnya anda akses (http://www.ietf.org) memuat beberapa 
gambar. Apakah host Anda perlu mengirimkan pesan permintaan DNS baru setiap kali ingin 
mengakses suatu gambar?  
![hasil](../assests/image/Week4(23).png)

    Tidak, host tidak perlu mengirimkan permintaan DNS baru setiap kali mengakses gambar. Hal ini dapat dilihat dari jumlah DNS query yang sedikit pada Wireshark, yang menunjukkan bahwa hasil DNS disimpan dan digunakan kembali (cache).

## B. www.mit.edu
## Langkah Percobaan ##
Ketik nslookup www.mit.edu pada cmd

![hasil](../assests/image/Week4(24).png)

Lalu buka wireshark, pilih jaringan yang digunakan, lalu filter dengan mengetik "DNS"

![hasil](../assests/image/Week4(25).png)

## Uji Pengamatan ##
1. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasan DNS?
![hasil](../assests/image/Week4(26).png) 
![hasil](../assests/image/Week4(27).png) 

    Port tujuan pada permintaan DNS adalah 53, sedangkan port sumber pada pesan balasan DNS adalah 53.

2. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut 
merupakan default alamat IP server DNS lokal Anda? 
![hasil](../assests/image/Week4(27).png) 

    Pesan permintaan DNS dikirimkan ke alamat IP 192.168.43.121. Alamat IP tersebut merupakan alamat IP server DNS lokal saya.

3. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan 
tersebut mengandung ”jawaban” atau ”answers”?
![hasil](../assests/image/Week4(28).png)

    Jenis (type) dari pesan permintaan DNS adalah A (Host Address), dan pesan tersebut tidak mengandung jawaban karena nilai Answer RRs = 0.

4. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di 
dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut?
![hasil](../assests/image/Week4(29).png)

    Jumlah jawaban (answers) pada pesan balasan DNS adalah 3. Jawaban tersebut terdiri dari dua record CNAME, yaitu www.mit.edu yang diarahkan ke www.mit.edu.edgekey.net dan kemudian ke e9566.dscb.akamaiedge.net, serta satu record A yang berisi alamat IP yaitu 23.15.150.186.

## C. nslookup -type=NS mit.edu
## Uji Pengamatan 
1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut 
merupakan default alamat IP server DNS lokal Anda?
![hasil](../assests/image/Week4(32).png)

    Pesan permintaan DNS dikirimkan ke alamat IP 192.168.43.1. Alamat IP tersebut merupakan alamat IP server DNS lokal saya.

2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan 
tersebut mengandung ”jawaban” ?
![hasil](../assests/image/Week4(33).png)

    Jenis (type) dari pesan permintaan DNS adalah NS, dan pesan tersebut tidak mengandung jawaban karena nilai Answer RRs = 0.

3. Periksa pesan balasan DNS. Apa nama server MIT yang diberikan oleh pesan balasan? 
Apakah pesan balasan ini juga memberikan alamat IP untuk server MIT tersebut?
![hasil](../assests/image/Week4(34).png)

    Nama server MIT yang diberikan oleh pesan balasan DNS adalah bitsy.mit.edu. Ya, pesan balasan tersebut juga memberikan alamat IP untuk server tersebut, yaitu 18.0.72.3.

## D. nslookup www.aiit.or.kr bitsy.mit.edu
## Uji Pengamatan  
1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut 
merupakan default alamat IP server DNS lokal Anda?
![hasil](../assests/image/Week4(35).png)

    Pesan permintaan DNS dikirimkan ke alamat IP 192.168.43.1. Alamat IP tersebut merupakan alamat IP server DNS lokal saya.

2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan 
tersebut mengandung ”jawaban” ?

![hasil](../assests/image/Week4(36).png)

Jenis (type) dari pesan permintaan DNS adalah A , dan pesan tersebut tidak mengandung jawaban karena nilai Answer RRs = 0.

3. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di 
dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut?

![hasil](../assests/image/Week4(37).png)
    
Pesan permintaan DNS tidak mendapatkan balasan (timeout), sehingga tidak terdapat jawaban di dalamnya.




