# Modul 3 - Pengenalan HTTP #
## Deskripsi ##
Pada modul ini, pembahasan difokuskan pada pemahaman protokol HTTP sebagai dasar komunikasi pada jaringan web. Melalui penggunaan Wireshark, akan menganalisis proses pertukaran data antara client dan server, termasuk metode request, struktur response, serta mekanisme keamanan yang diterapkan.
## Langkah Pengerjaan ##
1. Buka wireshark lalu pilih interface wifi untuk melakukan uji capture

    ![hasil](../assests/image/Week3(1).png)

2. Apabila traffic sudah berjalan, capturing pada wifi berhasil di wireshark, sebelum mencari http lakukan langkah berikutnya,

    ![hasil](../assests/image/Week3(2).png)
3. Buka URL berikut http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html pada browser kalian,lalu gunakan incognito mode atau jendela samaran baru dan pastikan not secured seperti berikut  

    ![hasil](../assests/image/Week3(3).png)

4. Pada hasil capture Wireshark, terlihat adanya HTTP GET request ke file HTTP-wireshark-file3.html yang kemudian diikuti oleh HTTP response (200 OK) dari server. Response tersebut berisi data HTML halaman web yang ditampilkan pada browser. Isi HTML ini dapat dilihat pada bagian Raw Data di Wireshark.

    ![hasil](../assests/image/Week3(4).png)

5. Lalu buka URL berikut http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html pada incognito mode atau jendela samaran baru

    ![hasil](../assests/image/Week3(5).png)

6. Lalu amati pada Wireshark

    ![hasil](../assests/image/Week3(6).png)

7. Lalu buka URL berikut http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html pastikan menggunakan incognito mode atau jendela samaran baru pada browser kalian, lalu akan muncul seperti ini, masukan username "wireshark
students" (tanpa tanda kutip), dan password adalah "network" (sekali lagi, tanpa tanda kutip), lalu login

    ![halo](../assests/image/Week3(7).png)

    Jika Username dan Password benar akan muncul seperti ini
    ![hasil](../assests/image/Week3(8).png)

8. Setelah itu, periksa pada Wireshark. Akan terlihat username dan password pada paket yang ditangkap.

    ![hasil](../assests/image/Week3(9).png)

    ![hasil](../assests/image/Week3(10).png)
    
## Kesimpulan ##
Berdasarkan percobaan yang telah dilakukan, dapat disimpulkan bahwa ketika client mengakses suatu URL, terlebih dahulu terjadi proses komunikasi awal dengan server. Server kemudian memberikan respon berupa status 200 OK. Dari hasil capture menggunakan Wireshark, terlihat bahwa protokol HTTP tidak menggunakan enkripsi, sehingga seluruh data yang dikirim oleh client ke server, termasuk informasi sensitif seperti password, dapat terbaca dengan jelas.
