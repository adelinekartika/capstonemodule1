# Capstone Project Module 1
By Adeline Kartika Tiku Putri class of JCDSOL-013(2)

## Deskripsi
Ini adalah program data nilai siswa untuk kelas 11A di SMA Kartika. Program ini dirancang untuk memudahkan pengguna dalam manajemen data nilai siswa. Tujuan utamanya adalah untuk menyediakan antarmuka yang interaktif dan mudah digunakan untuk melakukan empat fungsi utama: menampilkan, menambahkan, menghapus, dan mengubah data nilai siswa.

### Fungsi 1 : Menampilkan data nilai siswa
Tujuan pertama program adalah memberikan pengguna akses cepat dan mudah untuk melihat data nilai siswa yang tersedia. Dengan fitur ini, pengguna dapat melihat seluruh data siswa aktif, mencari data siswa tertentu berdasarkan kriteria tertentu, melihat seluruh data siswa yang telah dihapus, serta menampilkan data berdasarkan sorting dari kolom data tertentu.

### Fungsi 2 : Menambahkan sebuah data nilai siswa
Program ini memungkinkan pengguna untuk menambahkan data nilai siswa baru ke dalam daftar. Dengan fitur ini, pengguna dapat memasukkan informasi seperti NIS, nama, gender, dan nilai-nilai mata pelajaran (Matematika, Biologi, dan Fisika). Proses penambahan data ini dilakukan melalui antarmuka yang interaktif dan memastikan bahwa data yang dimasukkan sesuai dengan format yang diinginkan (Terdapat validasi gender dan nilai-nilai mata pelajaran terlebih dahulu). Untuk NIS akan ditambahkan secara otomatis oleh sistem dan berurutan berdasarkan NIS terakhir. Nilai akhir akan dihitung dan status keterangan siswa baru akan ditentukan secara otomatis oleh program. Terakhir terdapat konfirmasi penambahan data siswa baru.

### Fungsi 3 : Menghapus sebuah data nilai siswa
Salah satu fitur utama program adalah kemampuannya untuk menghapus data nilai siswa yang tidak diperlukan lagi. Pengguna dapat memilih data yang ingin dihapus berdasarkan NIS, dan program akan memastikan bahwa pengguna memberikan konfirmasi sebelum data dihapus dari daftar. Jika data benar-benar akan dihapus maka dari data tersebut akan ditambahkan pada daftar siswa yang telah dihapus dan dihilangkan dari data siswa aktif. (Program tetap menyimpan data lama siswa).

### Fungsi 4 : Mengubah sebuah data nilai siswa
Program ini memungkinkan pengguna untuk mengubah data nilai siswa yang sudah ada. Pengguna dapat memilih data yang ingin diubah berdasarkan NIS, dan kemudian memperbarui informasi seperti nama, gender, atau nilai-nilai mata pelajaran. Untuk nilai akhir dan status keterangan siswa akan diubah secara otomatis jika pengubahannya berupa nilai-nilai mata pelajaran. Untuk NIS tidak bisa diubah. Setelah perubahan dilakukan, program memastikan bahwa pengguna memberikan konfirmasi sebelum benar-benar menyimpan perubahan.

### Fungsi 5 : Filter data berdasarkan query tertentu
Fungsi ini digunakan pada salah satu fitur menampilkan data nilai siswa dan bertujuan untuk memungkinkan pengguna untuk mencari dan menyaring data siswa berdasarkan query tertentu. Pengguna dapat memasukkan query pencarian, dan fungsi akan mengembalikan data siswa yang sesuai dengan query tersebut, sehingga memudahkan pengguna dalam menemukan informasi yang mereka butuhkan. Fungsi ini tidak case-sensitive.

### Fungsi 6 : Validasi input nilai
Fungsi ini dirancang untuk memvalidasi input nilai yang dimasukkan oleh pengguna. Tujuannya adalah untuk memastikan bahwa nilai yang dimasukkan berada dalam rentang yang valid, yaitu antara 0 hingga 100. Fungsi ini digunakan untuk melakukan validasi untuk input nilai matematika, nilai biologi, dan nilai fisika. Jika nilai yang dimasukkan tidak sesuai, fungsi akan memberikan pesan kesalahan dan meminta pengguna untuk memasukkan nilai yang valid.

### Fungsi 7 : Validasi gender
Fungsi ini bertujuan untuk memvalidasi input gender yang dimasukkan oleh pengguna. Tujuannya adalah untuk memastikan bahwa input gender yang dimasukkan sesuai dengan format yang diharapkan, yaitu "Perempuan" atau "Laki-Laki". Jika input tidak sesuai, fungsi akan memberikan pesan kesalahan dan meminta pengguna untuk memasukkan gender yang valid.

### Fungsi 8 : Fungsi menghitung nilai akhir
Fungsi ini memiliki tujuan untuk menghitung nilai akhir yaitu nilai rata-rata dari tiga nilai (biologi, matematika, fisika) dari data nilai siswa. Hasil rata-rata akan dibulatkan menjadi dua angka di belakang koma. Fungsi ini membantu dalam perhitungan nilai akhir siswa tanpa perlu input dari pengguna dan juga akurat. Fungsi ini digunakan ketika pengguna hendak menambahkan data nilai siswa baru atau melakukan pengubahan nilai-nilai mata pelajaran.

### Fungsi 9 : Fungsi menentukan status keterangan siswa (Kelulusan)
Fungsi ini bertujuan untuk menentukan status keterangan kelulusan siswa berdasarkan nilai-nilai yang diperoleh siswa. Siswa akan dinyatakan lulus jika nilai akhirnya sama dengan atau lebih dari 75, dan terdapat minimal terdapat dua nilai subjek yang mencapai nilai 70 atau lebih. Jika kedua syarat tersebut telah terpenuhi, maka siswa akan dinyatakan 'Lulus'. Fungsi ini membantu dalam menentukan apakah seorang siswa lulus atau tidak berdasarkan kriteria yang ditetapkan. Fungsi ini digunakan ketika pengguna hendak menambahkan data nilai siswa baru atau melakukan pengubahan nilai-nilai mata pelajaran.



Copyright 2024 Adeline Kartika
