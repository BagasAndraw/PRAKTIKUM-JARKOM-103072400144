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
![hasil](../assests/image/Week6(14).png)

    Berdasarkan hasil pengamatan dengan filter tcp.stream eq 0, ACK mengakui data secara kumulatif. Sebagai contoh, segmen dengan sequence number 1 dan panjang data 565 byte diakui oleh ACK dengan nilai acknowledgment number 566. Selain itu, pada segmen dengan panjang 1460 byte, nilai ACK meningkat sebesar 1460 byte. Hal ini menunjukkan bahwa ACK dapat mengakui satu atau beberapa segmen sekaligus, sehingga tidak selalu dikirim untuk setiap segmen.

9. Berapa throughput (byte yang ditransfer per satuan waktu) untuk sambungan TCP? 
Jelaskan bagaimana Anda menghitung nilai ini.
![hasil](../assests/image/Week6(15).png)

    Throughput diperoleh menggunakan fitur TCP Stream Graph -> Throughput pada Wireshark. Dari grafik terlihat bahwa throughput berada pada kisaran sekitar 200–270 kbps selama proses transmisi. Nilai throughput dihitung sebagai jumlah data yang ditransfer dibagi dengan waktu transmisi. Grafik menunjukkan bahwa throughput relatif stabil selama koneksi berlangsung.

## 6.5 Congestion Control pada TCP
## Langkah Percobaan
 
Pilih segmen TCP yang dikirim klien di jendela "daftar paket yang diambil" Wireshark. 
Kemudian pilih menu: Statistics->TCP Stream Graph-> Time-Sequence-Graph(Stevens). 
Anda akan melihat plot yang terlihat mirip dengan plot di bawah. Plot tersebut dibuat dari 
paket yang ditangkap trace tcp-ethereal-trace-1 pada http://gaia.cs.umass.edu/wiresharklabs/wireshark-traces.zip 
![hasil](../assests/image/Week6(16).png)

## Uji Pengamatan
1. Gunakan alat plotting Time-Sequence-Graph (Stevens) untuk melihat grafik nomor urut 
berbanding waktu dari segmen yang dikirim oleh klien ke server gaia.cs.umass.edu. 
Dapatkah Anda mengidentifikasi di mana fase “slow start” TCP dimulai dan berakhir, dan 
pada bagian mana algoritma ”congestion avoidance” mengambil alih? Berikan komentar 
tentang bagaimana data yang diukur berbeda dari perilaku ideal TCP yang telah kita pelajari.

    Jawab :

    Gambar dapat dilihat dari Langkah Percobaan, Berdasarkan grafik Time-Sequence (Stevens), fase slow start terjadi pada awal koneksi, yaitu sekitar 0 hingga ±1 detik, yang ditunjukkan oleh peningkatan sequence number yang semakin cepat. Setelah itu, grafik berubah menjadi lebih linear, menandakan bahwa TCP memasuki fase congestion avoidance, di mana pertambahan data berlangsung secara bertahap. Pola ini sesuai dengan teori TCP, meskipun pada hasil pengukuran terdapat sedikit variasi yang disebabkan oleh kondisi jaringan nyata seperti delay dan mekanisme pengendalian aliran.

2. Jawablah kedua pertanyaan di atas untuk trace yang Anda dapatkan ketika Anda 
mengirimkan file dari komputer ke gaia.cs.umass.edu.
![hasil](../assests/image/Week6(17).png)

    Pada bagian ini sama seperti step yang sudah pernah di lakukan yaitu upload file "alice.txt" ke web http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html. 
    
    Berdasarkan grafik Time-Sequence (Stevens) dari proses upload file ke gaia.cs.umass.edu, terlihat bahwa tidak terdapat fase slow start yang jelas seperti pada teori TCP. Hal ini ditunjukkan oleh grafik yang relatif datar pada awal waktu, kemudian terjadi lonjakan sequence number secara tiba-tiba di akhir transmisi. Kondisi ini menunjukkan bahwa data tidak dikirim secara bertahap (eksponensial maupun linear), melainkan dalam jumlah kecil terlebih dahulu sebelum akhirnya dikirim sekaligus. Oleh karena itu, fase congestion avoidance juga tidak tampak secara signifikan. Perbedaan ini dapat disebabkan oleh ukuran file yang kecil atau mekanisme buffering pada aplikasi, sehingga perilaku TCP tidak sepenuhnya mengikuti pola ideal yang telah dipelajari.


