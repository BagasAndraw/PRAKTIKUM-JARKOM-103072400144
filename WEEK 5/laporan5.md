# Modul 5 - UDP ##
UDP (User Datagram Protocol) adalah protokol komunikasi pada layer transport yang digunakan untuk mengirimkan data secara cepat tanpa perlu membuat koneksi terlebih dahulu.

## Langkah Percobaan 
Unduh file berisi trace penangkapan paket UDP yang telah disediakan, buka link http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip kemudian buka zip, cari yang bernama "http-ethereal-trace-5" lalu buka di wireshark

## Uji Pengamatan
1. Pilih satu paket UDP yang terdapat pada trace Anda. Dari paket tersebut, berapa banyak 
“field” yang terdapat pada header UDP? Sebutkan nama-nama field yang Anda temukan! 
![hasil](../assests/image/Week5(1).png)

    Pada header UDP terdapat 4 field, yaitu Source Port, Destination Port, Length, dan Checksum.

2. Perhatikan informasi “content field” pada paket yang Anda pilih di pertanyaan 1. Berapa 
panjang (dalam satuan byte) masing-masing “field” yang terdapat pada header UDP? 
![hasil](../assests/image/Week5(02).png)
    
    Setiap field pada header UDP memiliki panjang 2 byte, yaitu Source Port, Destination Port, Length, dan Checksum, sehingga total panjang header UDP adalah 8 byte.

3. Nilai yang tertera pada ”Length” menyatakan nilai apa? Verfikasi jawaban Anda melalui 
paket UDP pada trace. 

    Jawab :

    Nilai pada field “Length” pada gambar nomor 1 menunjukkan total panjang paket UDP yang terdiri dari header (8 byte) dan payload. Berdasarkan hasil pengamatan pada Wireshark, nilai Length sebesar 58 byte terdiri dari 8 byte header dan 50 byte payload.
    
4. Berapa jumlah maksimum byte yang dapat disertakan dalam payload UDP? (Petunjuk: 
jawaban untuk pertanyaan ini dapat ditentukan dari jawaban Anda untuk pertanyaan 2) 

    Jawab :

    Jumlah maksimum byte yang dapat disertakan dalam payload UDP adalah 65527 byte, nilai maksimum ukuran paket UDP adalah 65535 byte, yang berasal dari ukuran field Length pada header UDP yang menggunakan 16 bit, lalu dikurangi panjang header UDP sebesar 8 byte.

5. Berapa nomor port terbesar yang dapat menjadi port sumber? (Petunjuk: lihat petunjuk 
pada pertanyaan 4) 

    Jawab :

    Nomor port terbesar yang dapat menjadi port sumber adalah 65535, karena field Source Port pada UDP memiliki ukuran 16 bit.

6. Berapa nomor protokol untuk UDP? Berikan jawaban Anda dalam notasi heksadesimal dan 
desimal. Untuk menjawab pertanyaan ini, Anda harus melihat ke bagian ”Protocol” pada 
datagram IP yang mengandung segmen UDP. 
![hasil](../assests/image/Week5(3).png)

    Nomor protokol untuk UDP terdapat 17 dalam desimal dan 0x11 dalam notasi heksadesimal, yang dapat dilihat pada field “Protocol” di header IP pada Wireshark.      

7. Periksa pasangan paket UDP di mana host Anda mengirimkan paket UDP pertama dan paket 
UDP kedua merupakan balasan dari paket UDP yang pertama. (Petunjuk: agar paket kedua merupakan balasan dari paket pertama, pengirim paket pertama harus menjadi tujuan dari 
paket kedua). Jelaskan hubungan antara nomor port pada kedua paket tersebut!
![hasil](../assests/image/Week5(4).png)
![hasil](../assests/image/Week5(5).png)

    paket pertama merupakan request dari 192.168.1.102 ke 192.168.1.104 dengan source port 4334 dan destination port 161. Paket kedua merupakan response dari 192.168.1.104 ke 192.168.1.102 dengan source port 161 dan destination port 4334.Hal ini menunjukkan bahwa pada paket balasan,nomor port saling bertukar, yaitu source port pada paket pertama menjadi destination port pada paket kedua, dan sebaliknya.
