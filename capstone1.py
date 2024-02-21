# Nama          : Adeline Kartika Tiku Putri
# Kelas         : JCDSOL-013(2)
# Keterangan    : Capstone Project Module 1 dengan Study Case Data Nilai Siswa
# Deskripsi     : Program data nilai siswa kelas 11A di SMA Kartika. Program ini dirancang untuk memudahkan pengguna dalam manajemen data nilai siswa. 
#                 Tujuan utamanya adalah untuk menyediakan antarmuka yang interaktif dan mudah digunakan untuk melakukan empat fungsi utama: 
#                 menampilkan, menambahkan, menghapus, dan mengubah data nilai siswa.

# Library
import os # Untuk clear screen
from tabulate import tabulate # Untuk membantu membuat tabel yang rapi
from colorama import init, Fore, Style # Untuk mengubah warna dan style text
init(autoreset=True) # Agar perubahan text dari colorama langsung berganti kembali ke default

# Fungsi untuk mencari data berdasarkan query tertentu
def filter_data(data, search_query):
    filtered_data = [] # Variabel untuk menyimpan data siswa yang terdapat query yang diminta
    lowQuery = search_query.lower()
    for row in data: 
        # Check if any value in the row contains the search query
        # Cek jika pencarian yang diminta ada di salah satu value di row
        found = False
        for value in row.values():
            # Query yang dicari dan value dibuat menjadi lower case agar tidak case-sensitive
            # Cek apakah ada Query yang dicari di dalam value
            if lowQuery in str(value).lower():
                found = True
                break # Langsung ke tahapan selanjutnya tanpa mengecek sisa value di row
        
        # Jika sama, maka row ditambahkan
        if found:
            filtered_data.append(row)

    return filtered_data

# Fungsi untuk melakukan validasi terhadap input nilai
def validate_input(prompt):
    while(True):
        try:
            user_input = int(input(prompt)) # Input nilai sehingga perlu integer
            # Periksa apakah input nilai berada di antara 0 dan 100
            if 0 <= user_input <= 100:
                return user_input
            else:
                # Jika nilai tidak valid, print pesan kesalahan
                print(Fore.RED + "Angka harus antara 0 sampai 100!")
        except ValueError:
            # Jika pengguna memasukkan nilai yang tidak dapat diubah menjadi integer, print pesan kesalahan
            print(Fore.RED + "Input harus berupa angka!")

# Fungsi untuk melakukan validasi terhadap input gender 
def validateGender(prompt):
     while(True):
        gender = input(prompt) 
        gender = gender.lower()  # Ubah ke lowercase agar tidak case-sensitive

        # Memeriksa jika gender merupakan salah satu dari opsi yang valid
        if gender in ["perempuan", "p"]:
            return "Perempuan"
        elif gender in ["laki", "laki-laki", "l"]:
            return "Laki-Laki"
        else:
            # Jika gender tidak valid, cetak pesan kesalahan
            print(Fore.RED + "Input Anda tidak Valid! Masukkan 'perempuan', 'P', 'laki', 'laki-laki', atau 'L'!")

# Fungsi untuk mencari nilai akhir siswa
def averageNilai(mat, bio, fis):
    # Nilai akhir adalah rata-rata dari nilai matematika, biologi, dan fisika
    nilaiAkhir = (mat+bio+fis)/3

    # Hasil nilai akhir dibulatkan ke dua angka desimal
    return round(nilaiAkhir, 2)

# Fungsi untuk menentukan status kelulusan siswa
# Siswa dinyatakan lulus jika nilai akhir (rata-rata) >= 75 dan terdapat minimal 2 subjek yang nilainya >= 70
def statusKeterangan(mat, bio, fis, rata):
    # Mengecek syarat nilai akhir >= 75
    if rata >= 75:
        # Mengecek syarat minimal 2 subjek yang nilainya >= 70
        if ((mat >= 70 and bio >= 70) or (mat >= 70 and fis >= 70) or (bio >= 70 and fis >= 70)):
            return "Lulus"
    else:
        return "Tidak Lulus"

# Fungsi untuk menampilkan data nilai siswa
def tampilDataNilai(dataSiswa, dataSiswaHapus):
    while(True):
        # print menu tampil data dan menerima input pilihan tampilan data
        print(listTampilData)
        menuTampilData = input("Silahkan pilih menu menampilkan data [1-5]: ")

        # Clear Screen
        os.system('cls')

        # Menampilkan seluruh data siswa
        if menuTampilData == '1':
            if (len(dataSiswa) > 0): # Jika ada data siswa
                print("DAFTAR SELURUH SISWA: \n")
                print(tabulate(dataSiswa, headers="keys", tablefmt='pretty'))
            else: # Jika tidak ada data siswa
                print("Tidak ada data siswa.")

        # Menampilkan data siswa berdasarkan pencarian tertentu
        elif menuTampilData == '2':
            # Menerima query yang ingin dicari
            searchData = input("Masukkan data yang ingin dicari: ")

            # Mencari data yang berisi query yang ingin dicari
            filteredData = filter_data(dataSiswa, searchData)

            # Jika ada semua data siswa di print
            if filteredData:
                print("DATA SISWA BEDASARKAN HASIL PENCARIAN: \n")
                print(tabulate(filteredData, headers="keys", tablefmt='pretty'))
            else:
                print(Fore.RED + "Tidak ada siswa dengan data {} yang ditemukan.".format(searchData))
        
        # Menampilkan data siswa yang telah dihapus
        elif menuTampilData == '3':
            if (len(dataSiswaHapus) > 0): # Jika ada data siswa yang pernah dihapus
                print("DAFTAR SELURUH SISWA YANG TELAH DIHAPUS: \n")
                print(tabulate(dataSiswaHapus, headers="keys", tablefmt='pretty'))
            else: # Jika tidak ada
                print("Tidak ada data siswa yang pernah dihapus.")

        # Menampilkan seluruh data siswa berdasarkan sorting kolom tertentu
        elif menuTampilData == '4':
            # print menu sorting data dan menerima input pilihan sorting data
            print(listSortingData)
            inputSort = input("Pilih menu sorting data berdasarkan [1-7]: ")

            # Berdasarkan nama siswa
            if (inputSort == '1'):
                sorted_list = sorted(listSiswa, key=lambda x: x['Nama'])
                print(tabulate(sorted_list, headers="keys", tablefmt="pretty"))
            # Berdasarkan gender siswa
            elif (inputSort == '2'):
                sorted_list = sorted(listSiswa, key=lambda x: x['Gender'])
                print(tabulate(sorted_list, headers="keys", tablefmt="pretty"))
            # Berdasarkan nilai matematika (Tertinggi ke terendah)
            elif (inputSort == '3'):
                sorted_list = sorted(listSiswa, key=lambda x: x['Nilai Matematika'], reverse=True)
                print(tabulate(sorted_list, headers="keys", tablefmt="pretty"))
            # Berdasarkan nilai biologi (Tertinggi ke terendah)
            elif (inputSort == '4'):
                sorted_list = sorted(listSiswa, key=lambda x: x['Nilai Biologi'], reverse=True)
                print(tabulate(sorted_list, headers="keys", tablefmt="pretty"))
            # Berdasarkan nilai fisika (Tertinggi ke terendah)
            elif (inputSort == '5'):
                sorted_list = sorted(listSiswa, key=lambda x: x['Nilai Fisika'], reverse=True)
                print(tabulate(sorted_list, headers="keys", tablefmt="pretty"))
            # Berdasarkan nilai akhir (Tertinggi ke terendah)
            elif (inputSort == '6'):
                sorted_list = sorted(listSiswa, key=lambda x: x['Nilai Akhir'], reverse=True)
                print(tabulate(sorted_list, headers="keys", tablefmt="pretty"))
            # Berdasarkan keterangan
            elif (inputSort == '7'):
                sorted_list = sorted(listSiswa, key=lambda x: x['Keterangan'])
                print(tabulate(sorted_list, headers="keys", tablefmt="pretty"))
            else:
                print(Fore.RED + "Input anda tidak valid! Masukkan angka antara 1 sampai 7!")

        # Keluar dari menu menampilkan data
        elif menuTampilData == '5':
            break
        
        # Input menu tampil data tidak valid
        else:
            print(Fore.RED + "Input tidak valid! Masukkan angka antara 1 sampai 5!")

    return

# Menambahkan sebuah data nilai siswa
def tambahDataNilai(dataSiswa):
    global jumlahSiswa # Untuk pembuatan NIS

    while(True):
        # print menu tambah data dan menerima input pilihan menambahkan data
        print(listTambahData)
        menuTambahData = input("Silahkan pilih menu menambahkan data [1-2]: ")
        
        # Clear Screen
        os.system('cls')

        # Menambahkan satu data siswa baru
        if menuTambahData == '1':
            if jumlahSiswa < 999:
                # NIS akan secara otomatis langsung dibuat oleh sistem, tidak manual
                tambahNIS = f"11A{(jumlahSiswa+1):03}"
                tambahNama = input("Masukkan nama siswa: ") # Menerima data nama siswa baru
                tambahGender = validateGender("Masukkan gender siswa [L/P]: ") # Menerima data gender siswa baru (sudah divalidasi)
                tambahNilaiMat = validate_input("Masukkan nilai matematika [0-100]: ") # Menerima data nilai matematika siswa baru (sudah divalidasi)
                tambahNilaiBio = validate_input("Masukkan nilai biologi [0-100]: ") # Menerima data nilai biologi siswa baru (sudah divalidasi)
                tambahNilaiFis = validate_input("Masukkan nilai fisika [0-100]: ") # Menerima data nilai fisika siswa baru (sudah divalidasi)

                # Nilai Akhir secara otomatis akan dihitung oleh sistem, tidak manual
                # Nilai akhir adalah rata-rata nilai matematika, biologi, dan fisika siswa
                tambahNilaiAkhir = averageNilai(tambahNilaiMat,tambahNilaiBio,tambahNilaiFis)

                # Keterangan secara otomatis akan ditentukan oleh sistem berdasarkan nilai akhir >= 75 dan minimal 2 nilai subjek >= 70
                tambahKeterangan = statusKeterangan(tambahNilaiMat,tambahNilaiBio,tambahNilaiFis,tambahNilaiAkhir)

                # temp data siswa baru
                tambahSiswa = {
                        'NIS': tambahNIS,
                        'Nama': tambahNama,
                        'Gender': tambahGender,
                        'Nilai Matematika': tambahNilaiMat,
                        'Nilai Biologi': tambahNilaiBio,
                        'Nilai Fisika': tambahNilaiFis,
                        'Nilai Akhir': tambahNilaiAkhir,
                        'Keterangan': tambahKeterangan
                    }
                
                print("CALON DATA BARU SISWA: \n")
                print(tabulate([tambahSiswa], headers="keys", tablefmt='pretty')) # Menampilkan calon data siswa

                # Simpan data 
                while(True):
                    validTambah = input("Simpan data siswa? [Y/N]: ")
                    if validTambah == "Y" or validTambah == "y": # Ya ditambahkan
                        dataSiswa.append(tambahSiswa) # Menambahkan data baru ke list data siswa (Aktif)
                        jumlahSiswa += 1 # Menambahkan jumlah siswa yang pernah terdaftar
                        print(Fore.GREEN + "Data siswa berhasil ditambahkan!")
                        break
                    elif validTambah == "N" or validTambah == "n": # Tidak jadi ditambahkan
                        print(Fore.RED + "Data siswa tidak disimpan.")
                        break
                    else: # Invalid input kepastian save data siswa
                        print(Fore.RED + "Input anda tidak valid! Masukkan antara 'Y', 'y', 'N', atau 'n'!")

            else:
                print(Fore.RED + "Kuota siswa di kelas 11A sudah penuh!!")
        
        # Keluar dari menu tambah data siswa 
        elif menuTambahData == '2':
            break

        else:
            print(Fore.RED + "Input anda tidak valid!")

    return

# Menghapus sebuah data nilai siswa
def hapusDataNilai(dataSiswa, dataSiswaHapus):
    while(True):
        # Menampilkan menu menghapus data siswa dan menerima pilihan menu menghapuskan data
        print(listHapusData)
        menuHapusData = input("Silahkan pilih menu menghapuskan data [1-2]: ")

        # Clear Screen
        os.system('cls')

        # Menghapus sebuah data siswa berdasarkan NIS
        if menuHapusData == '1':
            print(tabulate(dataSiswa, headers="keys", tablefmt='pretty'))
            hapusSiswa = input("Masukkan NIS dari data yang ingin dihapus: ")

            validNIS = False # variabel penanda NIS yang dimasukkan valid atau tidak
            for i in range(len(dataSiswa)):
                if hapusSiswa == dataSiswa[i]['NIS']:
                    validNIS = True # Tandai NIS valid

                    print("CALON DATA SISWA YANG AKAN DIHAPUS: \n")
                    print(tabulate([dataSiswa[i]], headers="keys", tablefmt='pretty'))
                    
                    # Validasi apakah data siswa benar-benar ingin dihapus
                    while(True):
                        validHapus = input("Hapus data siswa? [Y/N]: ")
                        if validHapus == "Y" or validHapus == "y": # Jika pengguna benar-benar ingin menghapus data
                            dataSiswaHapus.append(dataSiswa[i]) # Menambahkan data siswa yang akan dihapus ke variabel yang menyimpan data siswa lama
                            del dataSiswa[i] # Menghapus data siswa
                            print(Fore.GREEN + "Data siswa berhasil dihapus!")
                            break
                        
                        elif validHapus == "N" or validHapus == "n": # Jika pengguna tidak jadi menghapus data
                            print(Fore.RED + "Data siswa tidak dihapus.")
                            break

                        else:
                            print(Fore.RED + "Input anda tidak valid! Masukkan antara 'Y', 'y', 'N', atau 'n'!")

                    break # keluar dari loop for

            if not validNIS:
                print(Fore.RED + "Tidak ada siswa dengan NIS {} yang ditemukan.".format(hapusSiswa))

        # Keluar dari menu menghapus data
        elif menuHapusData == '2':
            break

        else:
            print(Fore.RED + "Input anda tidak valid! Masukkan angka antara 1 atau 2!")

    return

# Mengubah sebuah data nilai siswa
def ubahDataNilai(dataSiswa):
    while(True):
        # Menampilkan menu pengubahan data dan menerima input pilihan menu mengubah data
        print(listUbahData)
        menuUbahData = input("Silahkan pilih menu mengubah data [1-2]: ")

        # Clear Screen
        os.system('cls')

        # Jika ingin mengubah sebuah data siswa
        if menuUbahData == '1':
            print(tabulate(dataSiswa, headers="keys", tablefmt='pretty'))
            ubahSiswa = input("Masukkan NIS yang ingin diubah: ")

            validNIS = False # Variabel validasi NIS
            # Cek apakah NIS ada dalam data siswa
            for i in range(len(dataSiswa)):
                if ubahSiswa == dataSiswa[i]['NIS']:
                    validNIS = True # Jika NIS dari input valid

                    # Menyimpan data siswa yang akan diubah dalam variabel sementara
                    tempDataNama = dataSiswa[i]['Nama']
                    tempDataGender = dataSiswa[i]['Gender']
                    tempDataNilaiMat = dataSiswa[i]['Nilai Matematika']
                    tempDataNilaiBio = dataSiswa[i]['Nilai Biologi']
                    tempDataNilaiFis = dataSiswa[i]['Nilai Fisika']
                    tempDataNilaiAkhir = dataSiswa[i]['Nilai Akhir']
                    tempDataKeterangan = dataSiswa[i]['Keterangan']

                    # Loop agar dapat mengubah data sesuai kolom yang diinginkan
                    while(True):
                        tempUbahSiswa = { # dict data pengubahan siswa sementara
                            'NIS': dataSiswa[i]['NIS'],
                            'Nama': tempDataNama,
                            'Gender': tempDataGender,
                            'Nilai Matematika': tempDataNilaiMat,
                            'Nilai Biologi': tempDataNilaiBio,
                            'Nilai Fisika': tempDataNilaiFis,
                            'Nilai Akhir': tempDataNilaiAkhir,
                            'Keterangan': tempDataKeterangan
                        }

                        # Menampilkan data pengubahan sementara
                        print("DATA SISWA YANG INGIN DIUBAH DENGAN PENGUBAHAN SEMENTARA: \n")
                        print(tabulate([tempUbahSiswa], headers="keys", tablefmt='pretty')) 

                        # Menampilkan menu pilihan kolom data yang ingin diubah
                        print(listDataSiswa)
                        ubahDataSiswa = input("Masukkan menu kolom data yang ingin diubah [1-6]: ")
                        
                        # Clear Screen
                        os.system('cls')

                        # Ubah data
                        if ubahDataSiswa == '1': # Ubah nama
                            tempDataNama = input("Masukkan pembaharuan nama siswa: ")
                        elif ubahDataSiswa == '2': # Ubah gender
                            tempDataGender = validateGender("Masukkan gender siswa [L/P]: ")
                        elif ubahDataSiswa == '3': # Ubah nilai matematika
                            tempDataNilaiMat = validate_input("Masukkan nilai matematika [0-100]: ")
                            # langsung mengubah nilai akhir dan juga keterangan kelulusan siswa
                            tempDataNilaiAkhir = averageNilai(tempDataNilaiMat,tempDataNilaiBio,tempDataNilaiFis)
                            tempDataKeterangan = statusKeterangan(tempDataNilaiMat,tempDataNilaiBio,tempDataNilaiFis,tempDataNilaiAkhir)
                        elif ubahDataSiswa == '4': # Ubah nilai biologi
                            tempDataNilaiBio = validate_input("Masukkan nilai biologi [0-100]: ")
                            tempDataNilaiAkhir = averageNilai(tempDataNilaiMat,tempDataNilaiBio,tempDataNilaiFis)
                            tempDataKeterangan = statusKeterangan(tempDataNilaiMat,tempDataNilaiBio,tempDataNilaiFis,tempDataNilaiAkhir)
                        elif ubahDataSiswa == '5': # Ubah nilai fisika
                            tempDataNilaiFis = validate_input("Masukkan nilai fisika [0-100]: ")
                            tempDataNilaiAkhir = averageNilai(tempDataNilaiMat,tempDataNilaiBio,tempDataNilaiFis)
                            tempDataKeterangan = statusKeterangan(tempDataNilaiMat,tempDataNilaiBio,tempDataNilaiFis,tempDataNilaiAkhir)

                        # selesai mengubah data
                        elif ubahDataSiswa == '6':
                            break

                        else:
                            print(Fore.RED + "Input anda tidak valid! Masukkan angka antara 1 sampai 6!")
                    
                    print("Data Siswa yang ingin Diubah: \n")
                    print(tabulate([tempUbahSiswa], headers="keys", tablefmt='pretty'))

                    # Konfirmasi pengubahan data siswa untuk disimpan
                    while(True):
                        validUbah = input("Ubah data siswa? [Y/N]: ")
                        if validUbah == "Y" or validUbah == "y": # Jika benar-benar ingin mengubah data
                            dataSiswa[i] = tempUbahSiswa.copy() # Menyimpan perubahan
                            print(Fore.GREEN + "Data siswa sudah berhasil diubah!")
                            break
                        
                        elif validUbah == "N" or validUbah == "n": # Tidak jadi mengubah data
                            print(Fore.RED + "Perubahan data siswa tidak disimpan!")
                            break

                        else:
                            print(Fore.RED + "Input Anda tidak valid! Masukkan antara 'Y', 'y', 'N', atau 'n'!")
                    break

            if not validNIS:
                print(Fore.RED +"Tidak ada siswa dengan NIS {} yang ditemukan.".format(ubahSiswa))
                
        # Keluar dari program pengubahan data
        elif menuUbahData == '2':
            break

        else:
            print(Fore.RED + "Input tidak valid! Masukkan angka antara 1 atau 2!")

    return

# Data nilai siswa yang telah terdaftar
listSiswa = [{'NIS': '11A001','Nama': 'Putri Cahaya','Gender': 'Perempuan','Nilai Matematika': 71,'Nilai Biologi': 98,'Nilai Fisika': 87,'Nilai Akhir': 85.33,'Keterangan': 'Lulus'},
             {'NIS': '11A002','Nama': 'Budi Santoso','Gender': 'Laki-Laki','Nilai Matematika': 72,'Nilai Biologi': 88,'Nilai Fisika': 90,'Nilai Akhir': 83.33,'Keterangan': 'Lulus'},
             {'NIS': '11A003','Nama': 'Siti Rahayu','Gender': 'Perempuan','Nilai Matematika': 58,'Nilai Biologi': 72,'Nilai Fisika': 55,'Nilai Akhir': 61.67,'Keterangan': 'Tidak Lulus'},
             {'NIS': '11A004','Nama': 'Nisa Fitriani','Gender': 'Perempuan','Nilai Matematika': 81,'Nilai Biologi': 76,'Nilai Fisika': 83,'Nilai Akhir': 80.00,'Keterangan': 'Lulus'},
             {'NIS': '11A005','Nama': 'Agus Setiawan','Gender': 'Laki-Laki','Nilai Matematika': 78,'Nilai Biologi': 54,'Nilai Fisika': 92,'Nilai Akhir': 74.67,'Keterangan': 'Tidak Lulus'},
             {'NIS': '11A006','Nama': 'Joko Susanto','Gender': 'Laki-Laki','Nilai Matematika': 95,'Nilai Biologi': 88,'Nilai Fisika': 98,'Nilai Akhir': 93.67,'Keterangan': 'Lulus'},
             {'NIS': '11A007','Nama': 'Anisa Sari','Gender': 'Perempuan','Nilai Matematika': 58,'Nilai Biologi': 90,'Nilai Fisika': 83,'Nilai Akhir': 77.00,'Keterangan': 'Lulus'},
             {'NIS': '11A008','Nama': 'Adi Nugroho','Gender': 'Laki-Laki','Nilai Matematika': 85,'Nilai Biologi': 85,'Nilai Fisika': 90,'Nilai Akhir': 86.67,'Keterangan': 'Lulus'},
             {'NIS': '11A009','Nama': 'Rini Indah','Gender': 'Perempuan','Nilai Matematika': 56,'Nilai Biologi': 87,'Nilai Fisika': 68,'Nilai Akhir': 70.33,'Keterangan': 'Tidak Lulus'},
             {'NIS': '11A010','Nama': 'Irfan Saputra','Gender': 'Laki-Laki','Nilai Matematika': 67,'Nilai Biologi': 66,'Nilai Fisika': 99,'Nilai Akhir': 77.33,'Keterangan': 'Tidak Lulus'}]

# Data nilai siswa yang sudah dihapus
listSiswaHapus = []

# Daftar menu program utama
listMenu = '''
===== Program Data Nilai Siswa Kelas 11A di SMA Kartika =====

Pilihan Menu:
1. Menampilkan Data Nilai Siswa
2. Menambahkan Data Nilai Siswa
3. Mengubah Data Nilai Siswa
4. Menghapus Data Nilai Siswa
5. Keluar Program
'''

# Daftar menu menampilkan data
listTampilData = '''
+++++++++++++++ Menampilkan Data Nilai Siswa +++++++++++++++

1. Tampilkan Seluruh Data Siswa (Aktif)
2. Tampilkan Data Siswa Berdasarkan Pencarian Tertentu
3. Tampilkan Seluruh Data Siswa yang Telah Dihapus
4. Tampilkan Data Siswa Berdasarkan Urutan Kolom Tertentu
5. Kembali ke Menu Utama
'''

# Daftar menu menambahkan data
listTambahData = '''
+++++++++++++++ Menambahkan Data Nilai Siswa +++++++++++++++

1. Tambah Data Siswa
2. Kembali ke Menu Utama
'''

# Daftar menu menghapuskan data
listHapusData = '''
+++++++++++++++ Menghapuskan Data Nilai Siswa +++++++++++++++

1. Hapus Data Siswa
2. Kembali ke Menu Utama
'''

# Daftar menu mengubah data
listUbahData = '''
+++++++++++++++++ Mengubah Data Nilai Siswa +++++++++++++++++

1. Ubah Data Siswa
2. Kembali ke Menu Utama
'''

# Daftar menu data siswa yang bisa diubah
listDataSiswa = '''
Pilih kolom yang ingin diubah:
1. Nama Siswa
2. Gender
3. Nilai Matematika
4. Nilai Biologi
5. Nilai Fisika
6. Selesai
'''

# Daftar menu untuk sorting data
listSortingData = '''
Pilih sorting berdasarkan kolom: 
1. Nama Siswa
2. Gender
3. Nilai Matematika (Tertinggi ke Terendah)
4. Nilai Biologi (Tertinggi ke Terendah)
5. Nilai Fisika (Tertinggi ke Terendah)
6. Nilai Akhir (Tertinggi ke Terendah)
7. Keterangan
'''

# Variabel untuk menyimpan total jumlah siswa baik yang sudah terdaftar maupun dihapus
jumlahSiswa = len(listSiswa) # Untuk pembuatan NIS

# Main program
while(True):
    # Print dan menerima input menu utama
    print(listMenu)
    pilihanMenu = input("Silahkan pilih menu yang ingin dijalankan [1-5]: ")
    
    # Clear Screen
    os.system('cls')

    # Menampilkan Data Nilai Siswa
    if(pilihanMenu == '1'):
        tampilDataNilai(listSiswa,listSiswaHapus)

    # Menambahkan Data Nilai Siswa
    elif(pilihanMenu == '2'):
        tambahDataNilai(listSiswa)

    # Mengubah Data Nilai Siswa
    elif(pilihanMenu == '3'):
        ubahDataNilai(listSiswa)

    # Menghapus Data Nilai Siswa
    elif(pilihanMenu == '4'):
        hapusDataNilai(listSiswa, listSiswaHapus)

    # Keluar dari program            
    elif(pilihanMenu == '5'):
        print(Style.BRIGHT + "Terima kasih. Sampai jumpa! Program telah selesai.") # Tulisan bold
        break
    
    # Jika input menu utama invalid
    else:
        print(Fore.RED + "Input Anda tidak valid! Masukkan angka antara 1 sampai 5!") # Tulisan warna merah