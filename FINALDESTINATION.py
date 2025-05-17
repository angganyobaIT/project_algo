# LIBRARY
import csv
import os
import pandas as pd
from datetime import datetime
from pyfiglet import Figlet
from tabulate import tabulate

#-------------------------TAMPILAN -------------------------

def bersih():
    os.system('cls' if os.name == 'nt' else 'clear')

def dashboard():

    f = Figlet(font='standard')
    print("=" * 109)
    header = f.renderText("DISTRILINK")
    header_lines = header.split("\n")

    for line in header_lines:
        print(line.center(109))
    print("APLIKASI KAMI YANG PALING KEREN !".center(109))
    
    print("=" * 109)

dashboard()

#------------------------ Tampilan pembuka end ----------------------------------
    

#------------------------- Halaman login/register start -------------------------
# MELAKUKAN REGISTRASI
def register():
    dashboard()
    print("-" * 109)
    print("HALAMAN REGISTRASI".center(109))
    print("-" * 109)
    
    email_reg = input_email()
    username_reg = input_username()
    password_reg = input_password()
    
    pencatatan(email_reg, username_reg, password_reg)

# MEMINTA USER INPUT EMAIL
def input_email():
    bersih()
    dashboard()
    email_reg = input("Masukkan Email anda dengan benar !!!, guna dihubungi saat ada kendala: ")
    email_validation = input(f"Apakah email {email_reg} sudah sesuai? (y/n): ")
    
    if email_validation.lower() =='y':
        bersih()
        dashboard()
        print("EMAIL BERHASIL DI INPUT !")
        input("\nTekan ENTER untuk melanjutkan...")

        return email_reg

    else:
        print("Silahkan Masukkan Email Yang Benar !".center(109))
        return input_email()  # Akan kembali meminta input jika email belum benar

def input_username():
    bersih()
    dashboard()

    username_reg = input("Buat username dengan maksimal 7 karakter: ")

    # Cek panjang username
    if len(username_reg) > 7:
        print("Username yang dibuat terlalu panjang. Silakan coba lagi.")
        input("\nTekan ENTER untuk mencoba kembali...")
        return input_username()  # Panggil fungsi lagi untuk meminta input baru

    # Baca data dari file CSV
    try:
        with open('datauser.csv', mode='r') as file:
            find_data = csv.reader(file)
            for row in find_data:
                if row: 
                    check = row[1]  # data username ada di kolom kedua
                    #Kondisi jika username ada
                    if username_reg == check:
                        bersih()
                        dashboard()
                        print("Username telah terpakai. Silakan coba lagi.")
                        input("\nTekan ENTER untuk mencoba kembali..")
                        return input_username()  # Panggil fungsi lagi untuk meminta input baru  # Panggil fungsi lagi untuk meminta input baru
    except FileNotFoundError:
        print("File datauser.csv tidak ditemukan.")

    # Jika tidak ada username yang terpakai, maka username dianggap berhasil dibuat
    bersih()
    dashboard()
    print("USERNAME BERHASIL DIBUAT !")
    input("\nTekan ENTER untuk kembali...")
    return username_reg

# MEMINTA USER MEMBUAT PASSWORD
def input_password():
    bersih()
    dashboard()
    password_reg = input("Masukkan password dengan minimal 7 karakter berbeda: ")
    pass_sama = 0
    kurang = 0

    for i in password_reg:
        if password_reg.count(i) > 1:
            pass_sama += 1
            break

    if len(password_reg) < 7:
        kurang += 1
        
    if pass_sama != 0:
        print("Error: Terdapat karakter yang sama.")
        input("\nTekan ENTER untuk mencoba kembali...")
        return input_password()
    
    if kurang != 0:
        print("Jumlah karakter password tidak sesuai")
        input("\nTekan ENTER untuk mencoba kembali...")
        return input_password()
    
    if kurang == 0 and pass_sama == 0:
        password_validation = input("Masukkan password kembali: ")
        if password_validation != password_reg:
            print("Password yang diinput tidak sesuai")
            input("\nTekan ENTER untuk mencoba kembali...")
            return input_password()
        
        else:
            print("\nPASSWORD TERCATAT !")
            return password_reg

# MENCATAT EMAIL, USERNAME, DAN PASSWORD YANG TELAH MEMENUHI SYARAT 
def pencatatan(email_reg, username_reg, password_reg):
    with open('datauser.csv','a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email_reg, username_reg, password_reg])
    return berhasil()

# SETELAH REGIS
def berhasil():
    print("AKUN BERHASIL DI BUAT !")
    print("="*109)
    input("\nTekan ENTER untuk kembali...")
    return opening()


# HALAMAN UNTUK LOGIN
def login():
    bersih()
    dashboard()
    print("-" * 109)
    print("HALAMAN LOGIN".center(109))
    print("-" * 109)
    username_log = input("Masukkan username: ")
    password_log = input("Masukkan Password: ")

    # Mengakses file csv kolom 2 dan 3
    try:
        with open('datauser.csv', mode='r', newline='') as file:
            baca_data = csv.reader(file)

            for row in baca_data:
                username_match = username_log == row[1] #username ada di kolom ke 1
                password_match = password_log == row[2] #password ada di kolom ke 2

                if username_match and password_match:
                    print("LOGIN BERHASIL")
                    print("SELAMAT DATANG USER !")
                    input("Tekan ENTER untuk melanjutkan...")
                    return tampilkan_menu()  # Panggil menu untuk user

            # Cek untuk login admin
            if username_log == "DISTRILINK" and password_log == "ilhamangga":
                print("LOGIN BERHASIL")
                print("SELAMAT DATANG ADMIN !")
                input("Tekan ENTER untuk melanjutkan...")
                return main()  # Panggil halaman admin

            # Jika tidak ada kecocokan setelah loop
            else:
                print("LOGIN GAGAL".center(109))
                print("=" * 109)
                input("Tekan ENTER untuk mencoba kembali...")
                bantuan = input("Butuh bantuan? (y/n): ")
                if bantuan.lower() == "y":
                    print("Silahkan Hubungi Customer Care Kami: +888 999 1234")
                    kembali = input("Ingin Kembali? (y/n): ")
                    if kembali.lower() == "y":
                        return opening()  # Kembali ke halaman opening
                    elif kembali.lower() == "n":
                        return login()  # Kembali ke halaman login
                    else:
                        return opening()  # Kembali ke halaman opening

                elif bantuan.lower() == "n":
                    kembali = input("Ingin Mencoba Lagi (y/n): ")
                    if kembali.lower() == "y":
                        return login()  # Kembali ke halaman login
                    elif kembali.lower() == "n":
                        return opening()  # Kembali ke halaman opening
                    else:
                        return login()  # Kembali ke halaman login

    except FileNotFoundError:
        print("File tidak ditemukan")



#------------------------- Halaman login/register end -------------------------


#------------------------- Cara masuk user start -------------------------

# DASHBOARD OPENING
def opening():
    bersih()
    dashboard()
    print("-" * 109)
    print("|                      1. Register                      |                      2. Login                     |".center(100))
    print("-" * 109)
    print("=" * 109)
    
    print("[1]. Register")
    print("[2]. Login")
    var = str(input("Untuk melanjutkan silakan pilih menu (1/2): "))
    if var == "1":
        register()
    elif var == "2":
        login()
    else:
        print("Input tidak sesuai!!!")
        return opening()
    
    print("=" * 109)

#------------------------ Cara masuk user end ----------------------------------

def kelola_barang():
    bersih()
    dashboard() #Untuk mengelola barang
    print('\n[1]. Tambah barang \n[2]. Check barang \n[3]. Hapus barang \n[4]. Kembali')
    try:
        user_input = int(input('Pilih menu (1,2,3,4): '))
        if user_input == 1:
            bersih()
            dashboard()
            tambah_barang()
            input("\nTekan ENTER untuk kembali...")
        elif user_input == 2:
            bersih()
            dashboard()
            check_barang()
            input("\nTekan ENTER untuk kembali...")
            return kelola_barang()

        elif user_input == 3:
            bersih()
            dashboard()
            hapus_barang()
            input("\nTekan ENTER untuk kembali...")
            return kelola_barang()

        elif user_input == 4:
            main()
            
        else:
            print('Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.')

    except ValueError:
        print('Maaf, input yang anda ketik kurang benar.')

def mitra(): 
    #Untuk memilih mitra pada saat menambahkan barang
    while True:

        try:
            print ('\n1.PT SADBOR ABADI(A00) \n2. PT BAROKAH JAYA(B00) \n3. PT SURYA ELEKTRONIK PERKASA JAYA(C00)')
            user_input = int(input('Pilih mitra anda (1/2/3): '))
            if user_input == 1:
                bersih()
                dashboard()
                return 'PT SADBOR ABADI'
            elif user_input == 2:
                bersih()
                dashboard()
                return 'PT BAROKAH JAYA'
            elif user_input == 3:
                bersih()
                dashboard()
                return 'PT SURYA ELEKTRONIK PERKASA JAYA'

            else:
                print('Pilihan tidak valid. Silakan pilih 1, 2, atau 3')
                
        except ValueError:
            print ('Maaf, input yang anda ketik kurang benar')
            return mitra()

def question():
    bersih()
    dashboard() #Untuk memastikan user ingin melanjutkan atau tidak

    while True:

        try:
            user_input = input('\nApakah anda ingin menambah barang lagi? \n(Y/N)').upper()
            if user_input == 'Y':
                bersih()
                dashboard()
                return tambah_barang()
            if user_input == 'N':
                bersih()
                dashboard()
                return kelola_barang()

            else:
                print('Maaf, input hanya berupa huruf Y atau N')
                
        except ValueError:
            print ('Maaf, input yang anda ketik kurang benar')
            return mitra()

def tambah_barang(): #Untuk menambahkan barang pada data barang
    mitra_dict = {
        'PT SADBOR ABADI': 'A',
        'PT BAROKAH JAYA': 'B',
        'PT SURYA ELEKTRONIK PERKASA JAYA': 'C'
        }
    mitra_value = mitra() #Memanggil fungsi mitra
    kode_prefix = mitra_dict[mitra_value] #Mengambil kode prefix berdasarkan mitra, untuk memudahkan pengelompokan
    try:
        barang = pd.read_csv('data_barang.csv') #untuk membaca data csv
    except FileNotFoundError:
        print ('data _barang.csv tidak ditemukan')
        barang = pd.DataFrame(columns=['kode','nama','harga','stok','mitra']) #Untuk membuat data frame baru jika csv tidak ada
        return tambah_barang()
    
    last_code = barang[barang['mitra'] == mitra_value] #Mendapatkan kode terakhir untuk mitra yang dipilih
    if not last_code.empty:
        last_code = last_code['kode'].max() #Untuk menemukan kode terakhir pada tiap mitra
        next_code = kode_prefix + str(int(last_code[1:]) + 1).zfill(3) #Menghitung kode selanjutnya
        #last_code[1:] Untuk melihat index 1 dan selanjutnya
        #int(last_code[1:]) + 1 Untuk menambahkan +1 pada kode terakhir
        #zfill(3) Untuk mengisi angka 0  didepan hingga panjangnya 3 digit (Contoh: Pemjumlahannya 4, maka akan menjadi 004)
    else:
        next_code = kode_prefix + '001' #Jika belum ada kode sebelumnya
    
    nama_barang = input('Masukkan nama barang: ')   

    while True:

        try:
            harga_barang = int(input('Masukkan harga barang: '))
            if harga_barang < 0:
                print('Harga tidak boleh negatif, silakan masukkan harga dengan benar')
                continue
            break        
        except ValueError:
            print('Masukkan harga dengan benar')

    while True:

        try:
            stock_barang = int(input('Masukkan stok barang: '))    
            if stock_barang < 0:
                print('Jumlah tidak boleh negatif, silakan masukkan jumlah dengan benar')
                continue #Kembali ke awal loop untuk input ulang
            break #Keluar dari loop jika input valid
        except ValueError:
            print('Masukkan jumlah dalam angka')

    barang = barang._append({
        'kode': next_code,
        'nama': nama_barang,
        'harga': harga_barang,
        'stok': stock_barang,
        'mitra': mitra_value
    }, ignore_index=True) #Command append untuk menambahkan ke file csv    
    barang.to_csv('data_barang.csv', index=False) #Untuk menyimpan data ke csv, Index=False digunakan untuk mencegah menambah index baru pada csv
    
    print ("\nBarang berhasil ditambahkan")
    input("Tekan ENTER untuk kembali...")
    return question()

def tampilkan_barang(data): #Untuk menampilkan data barang
    print("-" * 109)
    print(f"{'kode':<10}{'nama':<20}{'harga':<20}{'stock':<20}{'mitra':<20}") #Angka untuk membuat jarak
    print("-" * 109)

    for index,item in data.iterrows(): #Menggunakan iterrows untuk Iterasi DataFrame
        print(f"{item['kode']:<10}{item['nama']:<20}Rp {int(item['harga']):<18}{item['stok']:<13}{item['mitra']:<20}")
    print("-" * 109)

def check_barang(): #Untuk mengecek barang yang sudah ada
    print ("DAFTAR SEMUA BARANG".center(109))
    try:
        barang = pd.read_csv('data_barang.csv')
        tampilkan_barang(barang) #Memanggil fungsi untuk menampilkan barang

    except FileNotFoundError:
        print ('Data barang tidak ditemukan')

def pilihan_hapus(barang):

    while True:

        try:
            print('Kode yang diketik akan menghapus barang tersebut')
            kode_input = input('Masukkan kode pada barang: ').upper()
            if kode_input in barang['kode'].values: #Menggunakan values untuk mengambil nilai dari kolom kode
                barang = barang[barang['kode'] != kode_input]  # Menghapus barang dengan kode yang diberikan
                barang.to_csv('data_barang.csv', index=False)  # Menyimpan data yang telah diperbarui ke CSV
                print(f'Barang dengan kode {kode_input} berhasil dihapus.')
                break

            else:
                print(f'Barang dengan kode {kode_input} tidak ditemukan.')

        except ValueError:
            print('print, maaf input yang anda ketik kurang sesuai')

def hapus_barang(): #Fungsi untuk menghapus barang
    try:
        barang = pd.read_csv('data_barang.csv') #Membaca file csv data_barang
        tampilkan_barang(barang)  # Menampilkan daftar barang yang ada
        pilihan_hapus(barang) #Memanggil def baru

    except FileNotFoundError:
        print('Data barang tidak ditemukan')

def riwayat_pembayaran():
    bersih()
    dashboard()
    print("=" *109)
    print("RIWAYAT PEMBAYARAN".center(109))
    print("=" *109)
    try:
        # Membaca data dari CSV ke dalam DataFrame
        data_pembayaran = pd.read_csv('riwayat_pesanan.csv')
        
        #mereset indexnya
        data_pembayaran = data_pembayaran.reset_index(drop=True)
        data_pembayaran.index += 1  # Membuat index dimulai dari 1
        
        # Menampilkan DataFrame dengan format yang teratur dan terpusat
        print(tabulate(data_pembayaran, headers='keys', tablefmt='pretty', stralign='center'))

        # Menanyakan apakah pembayaran telah diterima
        payment_quest = input("Telah menerima pembayaran? (y/n): ")
        if payment_quest.lower() == "y":  # Supaya mencakup kondisi "y" atau "Y"
            payment_validation = int(input("Barang mana yang telah dibayar? (Masukkan Nomor Barang): "))
            
            # Validasi input dan memperbarui status jika valid
            if payment_validation >= 1 and payment_validation <= len(data_pembayaran):
                
                # mengakses kolom status pembayaran file di csv'
                kolom_akses = 'status pembayaran'

                # Mengupdate status barang menggunakan .at
                data_pembayaran.at[payment_validation, kolom_akses] = 'DITERIMA'
                
                # Menyimpan data kembali ke csv
                data_pembayaran.to_csv('riwayat_pesanan.csv', index=False)  
                print("Barang Telah Dibayar. Barang akan segera diantar")
            
            # Kondisi jika input dari user diluar data di csv
            else:
                print("Nomor barang tidak valid.")  
        
        # Mengulangi fungsi jika diperlukan
        kembali = input("Untuk kembali tekan enter...")
        if kembali == "":
            main()  # Memanggil kembali fungsi untuk melihat riwayat pesanan

    except FileNotFoundError:
        print("File riwayat_pesanan.csv tidak ditemukan!")

# Memanggil fungsi untuk menampilkan riwayat pesanan
def laporan():
    bersih()
    dashboard()
    print("LAPORAN PENJUALAN FINAL".center(109))

    try:
        # Membaca data dari CSV
        data_penjualan = pd.read_csv('riwayat_pesanan.csv')
        
        data_penjualan = data_penjualan.reset_index(drop=True)
        data_penjualan.index += 1  # Membuat index dimulai dari 1
            
        # Filter data yang telah dibayar dan diterima
        pembayaran_diterima=(data_penjualan['status pembayaran']== "DITERIMA")
        barang_diterima=(data_penjualan['status penerimaan']== "DITERIMA")
        
        laporan_final=data_penjualan[pembayaran_diterima&barang_diterima]
        laporan_final.to_csv('laporan_penjualan.csv', index=False)
        
        # Hitung total penjualan
        total_penjualan = laporan_final['subtotal'].sum()
        total_barang = laporan_final['jumlah'].sum()
            
        # Tampilkan laporan
            
        # Gunakan tabulate untuk tampilan yang rapi
        print(tabulate(laporan_final, headers='keys', tablefmt='pretty'))
            
        # Tampilkan ringkasan
        print("\nRingkasan Penjualan:")
        print(f"Total Barang Terjual: {total_barang}")
        print(f"Total Pendapatan: Rp {total_penjualan:,}")

    except FileNotFoundError:
        print("File riwayat_pesanan.csv tidak ditemukan!")

def exit_admin():
    bersih()
    dashboard() #Untuk keluar dari admin
    print("TERIMAKASIH TELAH MENGGUNAKAN APLIKASI KAMI !".center(109))
    print("=" * 109)

#------------------------ Login sebagai admin start ----------------------------------

def main(): #Menu utama admin
    bersih()
    dashboard()

    while True:

        print('\nSilahkan pilih menu \n[1]. Kelola Barang \n[2]. Riwayat Pembayaran \n[3]. Laporan Penjualan \n[4]. Exit')
        try:
            user_input = int(input('Pilih menu (1,2,3,4): '))
            if user_input == 1:
                bersih()
                dashboard()
                kelola_barang()
                # input("\nTekan ENTER untuk kembali...")
            elif user_input == 2:
                bersih()
                dashboard()
                riwayat_pembayaran()
                input("\nTekan ENTER untuk kembali...")
            elif user_input == 3:
                laporan()
                input("\nTekan ENTER untuk kembali...")
                bersih()
                dashboard()
            elif user_input == 4:
                exit_admin()
                break

            else:
                print('Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.')

        except ValueError:
            print('Maaf, input yang anda ketik kurang benar.')

#------------------------ Login sebagai admin end ----------------------------------

#------------------------ Login sebagai user start ----------------------------------

def load_data():
    data = [] # MEMBACA DATA DARI FILE CSV

    try:
        with open('data_barang.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data
    
    except FileNotFoundError:
        print("File data_barang.csv tidak ditemukan!")
        return load_data()
    
# FUNGSI UNTUK MENCARI ITEM ATAU BARANG
def cari_barang(data, search_term):
    results = []

    for item in data:
        # Mencari dalam kolom kode dan nama
        if (search_term.lower() in item['kode'].lower() or 
            search_term.lower() in item['nama'].lower()):
            results.append(item)
    return results

# MENAMPILKAN HASIL DALAM FORMAT TABEL
def display_results(results):
    if not results:
        print("\nMohon maaf, barang tidak tersedia.")
        return
    
    print("\nHasil Pencarian:")
    print("-" * 109)
    print(f"{'KODE':<10}{'NAMA':<20}{'HARGA':<20}{'STOK':<20}{'MITRA':<20}")
    print("-" * 109)
    
    for item in results:
        print(f"{item['kode']:<10}{item['nama']:<20}Rp {int(item['harga']):<18}{item['stok']:<13}{item['mitra']:<20}")
    print("-" * 109)

# FUNGSI UNTUK MENAMPILKAN MENU BELI BARANG
def distribusikan_barang():
    barang_list = []

    with open('data_barang.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        barang_list = list(reader)
    
    total_pembelian = 0
    keranjang = []

    while True:
        print("=" * 109)
        print("Menu Pembelian".center(109))
        print("=" * 109)
        print("[1]. Distribusikan barang")
        print("[2]. Tampilkan daftar distribusi")
        print("[3]. Keluar")

        pilihan = input("Pilihan Anda (1/2/3): ")

        if pilihan == '1':
            bersih()
            dashboard()
            kode_barang = input("Masukkan KODE barang: ")
            jumlah = int(input("Masukkan jumlah yang ingin didistribusikan: "))

            # Mencari barang berdasarkan KODE
            barang = None
            for item in barang_list:
                if item[0] == kode_barang:
                    barang = item
                    break  # Jika barang ditemukan, keluar dari loop
            

            if barang:
                if int(float(barang[3])) >= jumlah:
                    harga = int(barang[2])
                    subtotal = harga * jumlah
                    keranjang.append({
                        'kode': barang[0],  # Menyimpan kode barang
                        'nama': barang[1],
                        'harga': harga,
                        'jumlah': jumlah,
                        'subtotal': subtotal
                    })
                    total_pembelian += subtotal

                    #TAMBAHAN FITUR
                    with open('riwayat_pesanan.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([barang[0], barang[1], jumlah, subtotal, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

                    print(f"\nBerhasil mendistribusikan {jumlah} {barang[1]}")
                    input("\nTekan ENTER untuk kembali...")
                    bersih()
                    dashboard()
                    check_barang()
                
                else:
                    print("\nMaaf, stok tidak mencukupi!")
            else:
                print("\nKODE barang tidak ditemukan!")

        elif pilihan == '2':
            bersih()
            dashboard()
            if keranjang:
                print("Daftar Distribusi".center(109))
                print(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".center(109))
                print("="*109)

                for item in keranjang:
                    print(f"{item['nama']}")
                    print(f"{item['jumlah']} x Rp {item['harga']} = Rp {item['subtotal']}")

                print("-"*109)
                print(f"Total Pembelian: Rp {total_pembelian}")
                print("Terima kasih telah menjadi agen distribusi kami!")
                input("\nTekan ENTER untuk kembali...")
                bersih()
                dashboard()
                check_barang()

                # Update stok di CSV
                for item in keranjang:
                    for barang in barang_list:
                        if barang[1] == item['nama']:
                            barang[3] = (int(float(barang[3])) - item['jumlah'])
                
                # Tulis kembali ke file CSV
                with open('data_barang.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['kode', 'nama', 'harga', 'stok', 'mitra'])
                    writer.writerows(barang_list)

            else:
                print("\nBelum ada barang yang didistribusikan!")

        elif pilihan == '3':
            bersih()
            dashboard()
            print("TERIMA KASIH!".center(109))
            print("="*109)
            break
       
        else:
            print("\nPilihan tidak valid!")

# FUNGSI UNTUK MENAMPILKAN MENU LACAK PESANAN (tambahan fitur)

def lacak_pesanan():
    print("RIWAYAT PESANAN".center(109))
    print("=" * 109)

    try:
        # Membaca data dari CSV ke dalam DataFrame
        databarang = pd.read_csv('riwayat_pesanan.csv')

        # Reset index dan tambahkan kolom nomor urut
        databarang = databarang.reset_index(drop=True)  # Mereset indexnya
        databarang.index += 1  # Membuat ulang index dari 1

        # Menampilkan kolom tertentu saja
        columns_to_display = ['kode', 'nama', 'jumlah', 'subtotal', 'waktu pembelian', 'status penerimaan']
        selected_data = databarang[columns_to_display]  # Mengatur apa saja yang mau ditampilkan

        # Menampilkan DataFrame dengan format yang teratur dan terpusat
        print(tabulate(selected_data, headers='keys', tablefmt='pretty', stralign='center'))

        # Menanyakan apakah barang telah diterima
        request = input("Barang sudah diterima? (y/n): ")
        if request.lower() == "y":
            request_validation = int(input("Barang mana yang telah diterima? (Masukkan Nomor Barang): "))
                
            # Validasi input 
            if request_validation >= 1 and request_validation <= len(databarang):
                # Mengakses status pembayaran menggunakan at
                status_pembayaran = databarang.at[request_validation, 'status pembayaran']
                
                # memeriksa apakah kolom status pembayaran kosong 
                kolom_kosong = pd.isna(status_pembayaran)
                
                if kolom_kosong:
                    print("Tidak bisa memperbarui status penerimaan. Silahkan melakukan pembayaran terlebih dahulu")
                    input("\nTekan ENTER untuk kembali...")
                    bersih()
                    dashboard()
                    
                else:
                    # Update status penerimaan
                    databarang.at[request_validation, 'status penerimaan'] = 'DITERIMA'  # Mengupdate status barang
                        
                    # Simpan perubahan ke CSV
                    databarang.to_csv('riwayat_pesanan.csv', index=False)
                    print(f"Barang dengan nomor {request_validation} telah diterima.")
                    input("\nTekan ENTER untuk kembali...")
                    bersih()
                    dashboard()

        elif request.lower() == "n":
            return tampilkan_menu()
        else:
            print("Nomor barang tidak valid.")
            
    except FileNotFoundError:
        print("File riwayat_pesanan.csv tidak ditemukan!")
        
# FUNGSI UNTUK MENAMPILKAN MENU UTAMA USER
def tampilkan_menu():

    while True:

        bersih()
        dashboard()
        print("\n[1]. TAMPILKAN SEMUA BARANG")
        print("[2]. CARI BARANG")
        print("[3]. DISTRIBUSIKAN BARANG")
        print("[4]. LACAK PESANAN")
        print("[5]. KELUAR")
        
        pilihan = input("\nMasukkan pilihan (1-5): ")
        
        if pilihan == "1":
            bersih()
            dashboard()
            check_barang()
            input("\nTekan Enter untuk kembali...")
        
        elif pilihan == "2":
            bersih()
            dashboard()
            data = load_data()
            search_term = input("\nMasukkan kata kunci pencarian (kode/nama): ")
            results = cari_barang(data, search_term)
            display_results(results)
            input("\nTekan Enter untuk kembali...")
        
        elif pilihan == "3":
            bersih()
            dashboard()
            data = load_data()
            check_barang()
            distribusikan_barang()
            input("\nTekan Enter untuk kembali...")
        
        elif pilihan == "4":
            bersih()
            dashboard()
            lacak_pesanan()
            tampilkan_menu()

        elif pilihan == "5":
            # bersih()
            # dashboard()
            print("TERIMA KASIH TELAH MENGGUNAKAN APLIKASI KAMI ! ".center(109))
            break
        
        else:
            print("\nPilihan tidak valid!")
            input("\nTekan Enter untuk kembali...")

opening()
#------------------------ Login sebagai user end ----------------------------------