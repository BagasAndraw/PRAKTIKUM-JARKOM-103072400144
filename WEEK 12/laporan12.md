# Modul 12 - ICMP dan Asistensi Tugas Besar

## Pengantar

Pada modul ini, akan dilakukan eksplorasi terhadap beberapa aspek penting dari protokol Internet Control Message Protocol (ICMP), meliputi analisis pesan ICMP yang dihasilkan oleh program Ping, pesan ICMP yang dihasilkan oleh program Traceroute, serta format dan isi dari pesan-pesan ICMP tersebut. Praktikum ini disajikan dengan menggunakan sistem operasi Microsoft Windows sebagai lingkungan utama, namun konsep dan langkah-langkah yang dibahas dapat dengan mudah diadaptasi dan diterapkan pada sistem operasi berbasis Unix maupun Linux.

Internet Control Message Protocol (ICMP) adalah protokol pada lapisan jaringan yang digunakan untuk mengirimkan pesan kontrol, informasi status, dan laporan kesalahan dalam komunikasi data pada jaringan IP. ICMP membantu perangkat jaringan dalam mendeteksi dan melaporkan masalah, seperti tujuan yang tidak dapat dijangkau, waktu transmisi yang habis, serta melakukan pengujian konektivitas melalui utilitas seperti Ping dan Traceroute.

## Langkah Percobaan
## ICMP dan Ping
### 1. Melakukan Ping 

Buka Command Prompot (cmd) pada device, lalu jalankan packet pada Wireshark, dan mulai pengambilan paket Wireshark, kemudian lakukan perintah berikut pada cmd;
```
C:\Users\Victus> ping –n 10 www.ust.hk
```

Yang mana untuk mengakses server Web di Universitas Sains dan 
Teknologi Hong Kong. Argumen “-n 10” menunjukkan bahwa 10 pesan ping harus dikirim.  

Berikut hasil output dari pengujian ping:

![hasil](../assests/image/Week12(1).png)

Hasil pengujian menunjukkan bahwa koneksi ke www.ust.hk (143.89.209.9) berjalan dengan baik. Dari 10 paket yang dikirim, 9 paket diterima dan 1 paket hilang (packet loss 10%). Waktu respons rata-rata sebesar 108 ms dengan rentang 107–114 ms, yang menunjukkan koneksi cukup stabil meskipun terjadi satu kali request timed out.

### 2. Analisis Paket Ping HK ke Wireshark
Kembali ke wireshark, yang sudah dijalankan sebelumnya, kemudian lakukan filtering dengan perintah "icmp" pada wireshark

![hasil](../assests/image/Week12(2).png)

Pada packet-listing window terlihat pasangan paket ICMP yang muncul secara bergantian. Paket ICMP Echo Request dikirim dari 192.168.1.6 menuju 143.89.209.9, sedangkan paket ICMP Echo Reply merupakan balasan dari server tujuan ke komputer pengirim. Setiap pasangan request-reply memiliki sequence number (seq) yang sama, sehingga dapat digunakan untuk mencocokkan paket permintaan dengan paket balasannya. Terlihat pula satu paket request yang tidak memperoleh reply (no response found), yang menunjukkan terjadinya kehilangan paket (packet loss).

### 3. Ping ke youtube.com

Lakukan hal yang sama dengan sebelumnya, dengan jalankan wireshark sebelum melakukan pengujian ping melalui cmd, namun perintah pada cmd berbeda, lakukan perintah berikut;

```
C:\Users\Victus> ping -n 10 www.youtube.com
```

Beikut hasil pengujian ping dari youtube.com :

![hasil](../assests/image/Week12(3).png)

### 4.  Analisis Paket di Wireshark

Sesudah melakukan pengujian, kembali ke wireshark, kemudian lakukan filtering dengan perintah "icmp"

Berikut hasil output dari filtering pada wireshark :

![hasil](../assests/image/Week12(4).png)

Pada pengujian ke youtube.com, paket ICMP dikirim dari 192.168.1.6 ke 74.125.130.190 dan sebagian besar memperoleh balasan (Echo Reply) dengan TTL = 109. Nilai TTL yang lebih tinggi dibandingkan ping ke www.ust.hk (TTL = 45) menunjukkan bahwa server YouTube secara logis berada lebih dekat atau melewati lebih sedikit hop dari sudut pandang jaringan. Namun, sama seperti pengujian sebelumnya, terdapat satu paket Echo Request yang tidak memperoleh balasan (no response found), yang mengindikasikan adanya packet loss. Secara keseluruhan, mekanisme ICMP yang terjadi tetap sama, hanya berbeda pada alamat tujuan dan karakteristik jalur jaringan yang dilalui.

##  ICMP dan Traceroute 

### 1.  Traceroute ke www.inria.fr
Sebelum melakukan traceout, **jalankan Wireshark** terlebih dahulu untuk pengambilan paket, lalu buka cmd, kemudian lakukan traceout ke server INRIA yang berada di Prancis dengan perintah sebagai berikut :
```
C:\Users\Victus> tracert www.inria.fr
```

Berikut hasil dari traceout dari server INRIA :

![hasil](../assests/image/Week12(5).png)

Hasil menunjukkan bahwa paket mencapai tujuan 128.93.162.83 dalam 15 hop. Waktu tempuh (round-trip time) meningkat dari sekitar 1–2 ms pada jaringan lokal menjadi sekitar 180 ms saat mencapai server tujuan di Prancis. Beberapa hop menampilkan tanda * atau Request timed out, yang menunjukkan router tersebut tidak merespons paket ICMP traceroute, namun tetap meneruskan paket ke tujuan. Secara keseluruhan, traceroute berhasil mengidentifikasi jalur yang dilalui paket dari jaringan lokal hingga server tujuan dengan latensi akhir sekitar 180 ms.

### 2. Analisis Paket TTL Exceeded Server INRIA pada Wireshark
Untuk melihat hasil pengambilan pake TTL Exceeded pada server INRIA, gunakan perintah berikut pada filtering wireshark:
```
icmp
```
Berikut hasil penangkapan paket ICMP TTL Exceeded server INRIA :

![hasil](../assests/image/Week12(6).png)

Berdasarkan hasil tangkapan Wireshark, terlihat paket ICMP Time-to-Live Exceeded (Type 11, Code 0) yang dikirim oleh router 193.51.184.177 ke host 192.168.1.6. Pesan ini muncul karena nilai TTL pada paket ICMP Echo Request yang dikirim menuju 128.93.162.83 (INRIA) telah habis sebelum mencapai tujuan.

Pada detail paket terlihat bahwa router mengembalikan informasi paket asli, termasuk ICMP Echo Request (Type 8) dengan Sequence Number 39, sehingga pengirim dapat mengetahui hop mana yang menyebabkan TTL berakhir. Mekanisme inilah yang dimanfaatkan oleh traceroute untuk mengidentifikasi setiap router yang dilalui paket dalam perjalanan menuju tujuan.

Dengan demikian, paket TTL Exceeded tersebut menandakan bahwa router 193.51.184.177 merupakan salah satu hop pada jalur menuju server INRIA dan berhasil terdeteksi oleh proses traceroute.






