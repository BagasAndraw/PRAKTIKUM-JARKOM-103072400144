# Modul 6 - TCP
TCP (Transmission Control Protocol) adalah protokol komunikasi pada layer transport yang digunakan untuk mengirimkan data secara andal, terurut, dan bebas kesalahan antar perangkat dalam jaringan.

## 6.2 Menangkap Tansfer TCP dalam Jumlah Besar dari Komputer Pribadi ke Remote Server  
## Langkah Percobaan
1. Buka wireshark terlebih dahulu sebelum masuk langkah berikutnya agar agar aktivitas jaringan dapat terekam pada Wireshark, lalu buka browser, masuk ke link http://gaia.cs.umass.edu/wireshark-labs/alice.txt, lalu save ke file
![hasil](../assests/image/Week6(1).png)  

2. Selanjutnya buka http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html, Uploud yang sudah di save tadi ke dalam link ini  
![hasil](../assests/image/Week6(2).png)
    Jika berhasil akan muncul pesan sukses seperti gambar berikut
![hasil](../assests/image/Week6(3).png)

3. Buka wireshark cari HTTP/1.1 200 OK. Pesan ini menunjukkan bahwa file telah berhasil diterima dan diproses oleh server. Setelah itu, halaman web menampilkan pesan “Congratulations” sebagai tanda proses upload berhasil.
![hasil](../assests/image/Week6(4).png)

## 6.3Tampilan Awal pada Captured Trace 
Unduh file berisi trace penangkapan paket UDP yang telah disediakan, buka link http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip kemudian buka zip, cari yang bernama "tcp-ethereal-trace-1" lalu buka di wireshark

## Uji Pengamatan 
1. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien (sumber) untuk 
mentransfer file ke gaia.cs.umass.edu? Cara paling mudah menjawab pertanyaan ini adalah 
dengan memilih sebuah pesan HTTP dan meneliti detail paket TCP yang digunakan untuk 
membawa pesan HTTP tersebut. 
![hasil](../assests/image/Week6(5).png)

    Alamat IP yang digunakan oleh komputer klien adalah 192.168.1.102 dengan nomor port TCP 1161, yang terlihat pada field Source Address dan Source Port pada paket TCP di Wireshark.

2. Apa alamat IP dari gaia.cs.umass.edu? Pada nomor port berapa ia mengirim dan menerima 
segmen TCP untuk koneksi ini?
![hasil](../assests/image/Week6(6).png) 

    Alamat IP dari gaia.cs.umass.edu adalah 128.119.245.12. Server tersebut menggunakan port 80 untuk mengirim dan menerima segmen TCP, yang merupakan port standar untuk HTTP.

## 6.4 Dasar TCP
## Uji Pengamatan 
1. Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara 
komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga 
teridentifikasi sebagai segmen SYN? 
![hasil](../assests/image/Week6(7).png)

     Nomor urut (sequence number) segmen TCP SYN adalah 0 (relative sequence number). Segmen tersebut dapat diidentifikasi sebagai segmen SYN karena memiliki flag SYN yang aktif (Flags: SYN) dan tidak disertai flag ACK.

2. Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien 
sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK? 
Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen  
sehingga teridentifikasi sebagai segmen SYNACK? 
![hasil](../assests/image/Week6(8).png)

    Filter dengan tcp.flags.syn == 1 && tcp.flags.ack == 1, amati nomor urut (sequence number) segmen SYN-ACK adalah 0 (relative sequence number), sedangkan nilai acknowledgement adalah 1. Nilai acknowledgement diperoleh dari sequence number segmen SYN sebelumnya ditambah 1. Segmen ini diidentifikasi sebagai segmen SYN-ACK karena memiliki flag SYN dan ACK yang aktif secara bersamaan.

3. Berapa nomor urut segmen TCP yang berisi perintah HTTP POST? Perhatikan bahwa untuk 
menemukan perintah POST, Anda harus menelusuri content field milik paket di bagian 
bawah jendela Wireshark, kemudian cari segmen yang berisi "POST" di bagian field DATA
nya. 
![hasil](../assests/image/Week6(9).png)

    Nomor urut segmen TCP yang berisi perintah HTTP POST adalah 164041, yang diperoleh dari field “Sequence Number” pada paket yang mengandung data POST.

4. Anggap segmen TCP yang berisi HTTP POST sebagai segmen pertama dalam koneksi TCP. 
Berapa nomor urut dari enam segmen pertama dalam TCP (termasuk segmen yang berisi 
HTTP POST)? Pada jam berapa setiap segmen dikirim? Kapan ACK untuk setiap segmen 
diterima? Dengan adanya perbedaan antara kapan setiap segmen TCP dikirim dan kapan 
acknowledgement-nya diterima, berapakah nilai RTT untuk keenam segmen tersebut? 
Berapa nilai EstimatedRTT setelah penerimaan setiap ACK? (Catatan: Wireshark memiliki 
fitur yang memungkinkan Anda untuk memplot RTT untuk setiap segmen TCP yang dikirim. 
Pilih segmen TCP yang dikirim dari klien ke server gaia.cs.umass.edu pada jendela "daftar
paket yang ditangkap". Kemudian pilih: Statistics->TCP Stream Graph- >Round Trip Time 
Graph).
![hasil](../assests/image/Week6(10).png)

    Nilai RTT diperoleh dari grafik Round Trip Time pada Wireshark dengan mengambil enam segmen pertama. RTT dihitung berdasarkan selisih waktu antara pengiriman segmen dan penerimaan ACK. Nilai EstimatedRTT dihitung menggunakan rumus EstimatedRTT = (1 – 0.125) × EstimatedRTT sebelumnya + 0.125 × SampleRTT.

5. Berapa panjang setiap enam segmen TCP pertama? 
![hasil](../assests/image/Week6(11).png)

    Dengan menggunakan filter tcp.stream eq 0 && tcp.len > 0, diperoleh enam segmen TCP pertama yang membawa data. Panjang masing-masing segmen berdasarkan field “TCP Segment Len” adalah 565 byte, 1460 byte, 1460 byte, 1460 byte, 1147 byte, dan 1460 byte.

6. Berapa jumlah minimum ruang buffer tersedia yang disarankan kepada penerima dan 
diterima untuk seluruh trace? Apakah kurangnya ruang buffer penerima pernah 
menghambat pengiriman?
![hasil](../assests/image/Week6(12).png)

    Nilai buffer receiver dapat dilihat pada field “Window” pada header TCP. Berdasarkan hasil pengamatan, nilai window size adalah sebesar 17520 byte, yang menunjukkan kapasitas buffer penerima.

7. Apakah ada segmen yang ditransmisikan ulang dalam file trace? Apa yang anda periksa (di 
dalam file trace) untuk menjawab pertanyaan ini?
![hasil](../assests/image/Week6(13).png)

    Tidak terdapat segmen TCP yang ditransmisikan ulang pada file trace. Hal ini dapat diketahui dengan menggunakan filter tcp.analysis.retransmission pada Wireshark, yang tidak menampilkan paket apa pun. 

8. Berapa banyak data yang biasanya diakui oleh penerima dalam ACK? Dapatkah anda 
mengidentifikasi kasus-kasus di mana penerima melakukan ACK untuk setiap segmen yang 
diterima? 

9. Berapa throughput (byte yang ditransfer per satuan waktu) untuk sambungan TCP? 
Jelaskan bagaimana Anda menghitung nilai ini.

