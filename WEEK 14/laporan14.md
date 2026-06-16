# Modul 14 - 802.11 WiFi

## Pengantar 

Pada modul ini, praktikan akan mempelajari dan menganalisis protokol jaringan nirkabel menggunakan perangkat lunak Wireshark. Berbeda dengan praktikum sebelumnya yang berfokus pada jaringan Ethernet berkabel, praktikum ini menitikberatkan pada pengamatan lalu lintas data yang ditransmisikan melalui jaringan nirkabel (wireless). Praktikan akan melakukan analisis terhadap frame yang telah direkam sebelumnya untuk memahami proses komunikasi pada jaringan Wi-Fi, mengidentifikasi berbagai jenis frame, serta mempelajari informasi yang terkandung di dalamnya. Penggunaan file hasil tangkapan (capture file) dilakukan karena tidak semua perangkat dan driver kartu jaringan nirkabel mendukung penangkapan frame 802.11 secara langsung.

IEEE 802.11 merupakan standar yang dikembangkan oleh Institute of Electrical and Electronics Engineers (IEEE) untuk mengatur komunikasi pada jaringan area lokal nirkabel atau Wireless Local Area Network (WLAN). Standar ini mendefinisikan mekanisme akses media, format frame, serta prosedur komunikasi yang memungkinkan perangkat dapat saling bertukar data melalui media udara. Dalam standar 802.11 terdapat beberapa jenis frame, yaitu frame manajemen (management frame), frame kontrol (control frame), dan frame data (data frame), yang masing-masing memiliki fungsi berbeda dalam mendukung proses koneksi, pengendalian komunikasi, dan pengiriman data pada jaringan nirkabel.

## Langkah Percobaan

## 1. Analisis Beacon Frame
Beacon frame merupakan salah satu jenis management frame pada standar IEEE 802.11 yang secara berkala dikirimkan oleh Access Point (AP) untuk mengumumkan keberadaan jaringan Wi-Fi kepada perangkat di sekitarnya. Frame ini berisi informasi penting mengenai jaringan, seperti SSID (nama jaringan), alamat MAC AP, kanal yang digunakan, interval beacon, serta kemampuan dan konfigurasi jaringan.  

### Pemfilteran dan Analisis Beacon Frame
Sebelum melakukan analisis pada wireshark, download file zip dengan link berikut

 ```
http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip 
```
Lalu pilih file **Wireshark_802_11** dan buka melalui wireshark, kemudian lakukan filtering dengan melakukan perintah 
```
wlan.fc.subtype == 8 && wlan.fc.type == 0
```

![hasil](../assests/image/Week14(1).png)

Hasil pemeriksaan pada Beacon Frame menunjukkan bahwa Access Point menggunakan standar fisik IEEE 802.11b (HR/DSSS) yang beroperasi pada frekuensi 2437 MHz atau Channel 6 pada pita 2,4 GHz. Nilai Beacon Interval sebesar 102,4 ms menunjukkan bahwa AP mengirimkan informasi keberadaan jaringan secara periodik sekitar 10 kali per detik. Selain itu, nilai signal strength sebesar -29 dBm mengindikasikan kualitas sinyal yang sangat kuat, sedangkan noise level sebesar -100 dBm menunjukkan tingkat gangguan yang rendah sehingga komunikasi nirkabel dapat berlangsung dengan baik.

Pada bagian Tagged Parameters, teridentifikasi nama jaringan (SSID) yaitu "30 Munroe St". Informasi Supported Rates menunjukkan bahwa AP mendukung kecepatan transmisi dasar 1, 2, 5,5, dan 11 Mbps, sementara Extended Supported Rates menambahkan dukungan kecepatan hingga 54 Mbps. Selain itu, terdapat informasi Country Code (US), Traffic Indication Map (TIM), serta parameter WMM/WME yang digunakan untuk mendukung manajemen lalu lintas dan peningkatan kualitas layanan (Quality of Service). Informasi-informasi ini disiarkan melalui Beacon Frame agar perangkat klien dapat mengenali karakteristik jaringan sebelum melakukan proses koneksi.

## 2. Analisis Data Transfer
Untuk menganalisis data, diterapkan filter alamat IP, dengan melakukan perintah pada filter sebagai berikut:
```
ip.addr ==  128.119.245.12
```
![hasil](../assests/image/Week14(2).png)    

Hasil pengamatan menunjukkan terjadinya proses **TCP Three-Way Handshake** yang terdiri dari pertukaran paket **SYN, SYN-ACK, dan ACK** sebelum koneksi berhasil dibangun. Setelah koneksi TCP terbentuk, paket **HTTP GET** pada **Frame 480** dikirimkan oleh klien untuk meminta berkas teks **/wireshark-labs/alice.txt** dari server.

Dari sisi protokol, data terlebih dahulu dikemas menggunakan **Logical Link Control (LLC)** pada lapisan data link, kemudian diteruskan melalui **Internet Protocol Version 4 (IPv4)**. Paket tersebut dikirim dari host klien dengan alamat IP **192.168.1.109** menuju server yang memiliki alamat IP **128.119.245.12**.

### 3. Analisis Proses Association & Disassociation

Untuk menganalisis frame manajemen pada jaringan nirkabel IEEE 802.11, digunakan filter Wireshark untuk menampilkan paket-paket yang termasuk ke dalam kategori Management Frame. Frame ini berfungsi dalam proses pembentukan, pemeliharaan, dan penghentian koneksi antara klien dan Access Point (AP).

Beberapa jenis Management Frame yang diamati antara lain:
* Association: Merupakan proses ketika klien mengajukan permintaan untuk bergabung dengan Access Point sehingga koneksi nirkabel dapat dibentuk.
* Disassociation: Merupakan proses penghentian hubungan antara klien dan Access Point, baik atas permintaan klien maupun dari sisi AP.

Untuk menampilkan Management Frame, digunakan filter berikut:
```
wlan.fc.type_subtype == 0
```
Filter tersebut digunakan untuk menampilkan frame asosiasi yang terlibat dalam proses pembentukan koneksi pada jaringan nirkabel IEEE 802.11.  

### Melakukan expand paket awal

![hasil](../assests/image/Week14(3).png)

### Melakukan expand paket akhir

![hasil](../assests/image/Week14(4).png)

Berdasarkan hasil analisis, terdapat perubahan pada parameter SSID antara Frame 1750 dan Frame 2162. Pada Frame 1750, klien mengirim Association Request ke Access Point dengan SSID "linksys_SES_24086". Sementara itu, pada Frame 2162, klien mengirim Association Request ke Access Point dengan SSID "30 Munroe St", yang menunjukkan bahwa klien mencoba terhubung ke jaringan yang berbeda.

Analisis Association Response dilakukan menggunakan filter:
```
wlan.fc.type_subtype == 1
```
Filter tersebut digunakan untuk menampilkan paket Association Response, yaitu frame yang dikirim oleh Access Point sebagai tanggapan terhadap permintaan asosiasi dari klien. Melalui frame ini dapat diketahui status penerimaan atau penolakan koneksi serta informasi yang diberikan AP setelah proses asosiasi dilakukan.

![hasil](../assests/image/Week14(4).png)

Hasil analisis menunjukkan bahwa **Frame 2166** merupakan paket **Association Response** yang dikirim oleh *Access Point* sebagai balasan terhadap permintaan asosiasi dari klien. Pada frame tersebut, **Transmitter Address** berisi alamat MAC **CiscoLinksys_f7:1d:51**, yang mengidentifikasi perangkat *Access Point* sebagai pengirim respons. Paket ini menandakan bahwa permintaan koneksi yang diajukan oleh klien **Intel_d1:6b:4f** telah diterima, sehingga proses asosiasi berhasil dilakukan dan klien dapat melanjutkan tahapan komunikasi berikutnya pada jaringan nirkabel.

