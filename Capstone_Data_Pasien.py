pasien = { 
    1122 :{'kode':1122,'nama':'Abdul Rozak', 'umur': 12,'gender':'L','keluhan':'Gigi'},
    2233 :{'kode':2233,'nama':'Langit Bulan','umur': 23,'gender':'P','keluhan':'Gigi'},
    3344 :{'kode':3344,'nama':'Dedi Suwandi','umur': 34,'gender':'L','keluhan':'Telinga'},
    4455 :{'kode':4455,'nama':'Adi Sopyan','umur': 45,'gender':'L','keluhan':'Telinga'},
    5566:{'kode':5566,'nama':'Herman Abanda','umur': 56,'gender':'L','keluhan':'Mata'},
    6677 :{'kode':6677,'nama':'Suci Julianti','umur': 67,'gender':'P','keluhan':'Mata'}
}

def semuapasien():
    print('\tData Pasien Rumah Sakit Purwadhika\n')
    print('|Kode Pasien\t| Nama Pasien\t | Umur\t | Gender| Keluhan\t')
    for p in pasien.keys():
        print('|    {}\t| {}\t | {}\t |   {}\t | {}\t'.format(pasien[p]['kode'],pasien[p]['nama'],pasien[p]['umur'],pasien[p]['gender'],pasien[p]['keluhan']))

def pasiengigi():
    print('\tData Pasien Poliklinik Gigi\n')
    print('|Kode Pasien\t| Nama Pasien\t | Umur\t | Gender| Keluhan\t')
    for g in pasien.values():
        for i in g.values():
            if i == 'Gigi':
                 print('|     {}\t| {}\t | {}\t |   {}\t | {}\t'.format(g['kode'],g['nama'],g['umur'],g['gender'],g['keluhan']))

def pasientht():
    print('\tData Pasien Poliklinik Gigi\n')
    print('|Kode Pasien\t| Nama Pasien\t | Umur\t | Gender| Keluhan\t')
    for t in pasien.values():
        for i in t.values():
            if i == 'Telinga':
                 print('|     {}\t| {}\t | {}\t |   {}\t | {}\t'.format(t['kode'],t['nama'],t['umur'],t['gender'],t['keluhan']))

def pasienmata():
    print('\tData Pasien Poliklinik Gigi\n')
    print('|Kode Pasien\t| Nama Pasien\t | Umur\t | Gender| Keluhan\t')
    for m in pasien.values():
        for i in m.values():
            if i == 'Mata':
                 print('|     {}\t| {}\t | {}\t |   {}\t | {}\t'.format(m['kode'],m['nama'],m['umur'],m['gender'],m['keluhan']))

   
def tambahpasien():
    while True:
        kodepasien = int(input('Masukkan Kode Pasien (4 digit Angka): '))
        if kodepasien in pasien.keys():
            print('Maaf Kode Pasien Telah Digunakan')
            continue
        namapasien = input('Masukkan Nama Pasien (minimal 6 karakter): ')
        while len(namapasien) < 6 :
            print('Maaf Nama Pasien (Min:6, Max:15 Karakter), Silahkan Tambah Spasi jika Nama kurang dari 6 Karakter')
            namapasien=input('Masukkan Nama Pasien (minimal 6 karakter): ')
        umurpasien = int(input('Masukkan Umur Pasien:'))
        genderpasien = input('Masukkan Gender Pasien (L/P): ').upper()
        while genderpasien !='L' and genderpasien !='P':
            print('Mohon Periksa Kembali Gender Pasien, Cukup Masukkan L/P')
            genderpasien = input('Masukkan Gender Pasien (L/P): ').upper()
            if genderpasien == 'L' or genderpasien=='P':
                break
        keluhanpasien = input('Masukkan Keluhan Pasien: ').capitalize()
        while True:
                if keluhanpasien == 'Gigi':
                    break
                if keluhanpasien == 'Mata':
                    break
                if keluhanpasien == 'Telinga':
                    break
                if  keluhanpasien != 'Gigi':
                    print('Maaf Hanya Tersedia Klinik Untuk Keluhan (Gigi/Mata/Telinga) ')
                    keluhanpasien = input('Masukkan Keluhan Pasien: ').capitalize()
                elif keluhanpasien != 'Mata':
                    print('Maaf Hanya Tersedia Klinik Untuk Keluhan (Gigi/Mata/Telinga) ')
                    keluhanpasien = input('Masukkan Keluhan Pasien: ').capitalize()
                elif keluhanpasien!= 'Telinga':
                    print('Maaf Hanya Tersedia Klinik Untuk Keluhan (Gigi/Mata/Telinga) ')
                    keluhanpasien = input('Masukkan Keluhan Pasien: ').capitalize()
        cek_tambah = input('Lanjutkan Proses Tambah Pasien? (Y/N): ')
        if cek_tambah == 'Y' and cek_tambah == 'y':
            break
        break
    print('\nTerimakasih Data Pasien Telah Tersimpan')
    pasien[kodepasien]={'kode':kodepasien,'nama':namapasien,'umur':umurpasien,'gender':genderpasien,'keluhan':keluhanpasien}
    
def kliniktambah():
    while True:
        halamantambah = input('''
        Daftar Klinik :

        1. Seluruh Pasien
        2. Pasien Klinik Gigi
        3. Pasien Klinik THT
        4. Pasien Klinik Mata
        5. Kembali ke Menu Utama
        
        Ketik Angka Klinik yang Ingin Ditambah Datanya : ''')

        if(halamantambah == '1'):
            tambahpasien()
        elif(halamantambah == '2'):
            tambahpasien()
        elif (halamantambah == '3'):
            tambahpasien()
        elif (halamantambah == '4'):
            tambahpasien() 
        elif (halamantambah == '5'):
            print(hospital())
            break

def klinikupdate():
    update_pasien = int(input('Masukkan Kode Pasien (4 Digit): '))
    while update_pasien in pasien.keys():
        halamanupdate = input('''
        Daftar Update :

        1. Update Kode 
        2. Update Nama
        3. Update Umur
        4. Update Gender
        5. Update Keluhan
        6. Kembali Ke Halaman Utama
        
        Ketik Angka Untuk Update Data dari Kode Pasien {} : '''.format(update_pasien))
        if (halamanupdate == '1'):
            kode_update = int(input('Masukkan Kode Pasien Baru: '))
            while True:
                cek_update = input('Lanjutkan Update Kode Pasien? (Y/N): ')
                if cek_update != 'Y' and cek_update!= 'y':
                    break
                else:
                    pasien[kode_update] = pasien[update_pasien]
                    del pasien[update_pasien]
                    pasien[kode_update]['kode'] = kode_update
                    semuapasien()
                    break
        elif (halamanupdate == '2'):
            nama_update = input('Masukkan Nama Pasien Baru: ')
            while True:
                if len(nama_update) < 6 :
                    print('\nMaaf Nama Pasien (Min:6 Karakter), Silahkan Tambah Spasi jika Nama kurang dari 6 Karakter')
                    nama_update = input('Masukkan Kode Pasien Baru: ')
                cek_update = input('Lanjutkan Update Nama Pasien? (Y/N): ')
                if cek_update != 'Y' and cek_update!= 'y':
                    break
                else:
                    pasien[update_pasien]['nama'] = nama_update.capitalize()
                    semuapasien()
                    break
        elif (halamanupdate == '3'):
            umur_update = int(input('Masukkan Umur Pasien Baru: '))
            while True:
                cek_update = input('Lanjutkan Update Umur Pasien? (Y/N)')
                if cek_update != 'Y' and cek_update!='y':
                    break
                else:
                    pasien[update_pasien]['umur'] = umur_update
                    semuapasien()
                    break
        elif(halamanupdate == '4'):
            gender_update = input('Masukkan Gender Pasien Baru (L/P): ').upper()
            while True:
                if gender_update != 'L' and gender_update!='P':
                    print('\nMaaf Periksa Kembali Gender Pasien, Cukup Input L(Laki-Laki) dan P(Perempuan)')
                    gender_update = input('Masukkan Gender Pasien Baru: ').upper()
                elif gender_update=='L' or gender_update=='P':
                    break
            cek_update = input('Lanjutkan Update Gender Pasien? (Y/N): ')
            if cek_update != 'Y' and cek_update!='y':
                break
            else:
                pasien[update_pasien]['gender'] = gender_update.capitalize()
                semuapasien()
        elif (halamanupdate == '5'):
            keluhan_update = input('Masukkan Keluhan Pasien Baru (Gigi/Mata/Telinga): ')
            while True:
                if keluhan_update == 'Gigi':
                    break
                if keluhan_update == 'Mata':
                    break
                if keluhan_update == 'Telinga':
                    break
                if  keluhan_update != 'Gigi':
                    print('Maaf Klinik Untuk Keluhan Penyakit Anda Tidak Tersedia')
                    keluhan_update = input('Masukkan Keluhan Pasien: ').capitalize()
                elif keluhan_update != 'Mata':
                    print('Maaf Klinik Untuk Keluhan Penyakit Anda Tidak Tersedia')
                    keluhan_update = input('Masukkan Keluhan Pasien: ').capitalize()
                elif keluhan_update != 'Telinga':
                    print('Maaf Klinik Untuk Keluhan Penyakit Anda Tidak Tersedia')
                    keluhan_update = input('Masukkan Keluhan Pasien: ').capitalize()
            cek_update = input('Lanjutkan Update Keluhan Pasien? (Y/N): ')
            if cek_update != 'Y' and cek_update!= 'y':
                break
            else:
                pasien[update_pasien]['keluhan'] = keluhan_update.capitalize()
                semuapasien()
                break
        elif (halamanupdate == '6'):
            hospital()
        else: 
            print('Menu yang Anda Pilih Tidak Tersedia')
    else:
        print('\nKode Pasien Tidak Tersedia')

def hapuspasien():
    semuapasien()
    kodepasien=int(input('Masukkan Kode Pasien Untuk Menghapus Data Pasien (4 digit Angka): '))
    while True:
        if kodepasien in pasien.keys():
            print('\nTerimakasih Data Telah Terhapus')
            del pasien[kodepasien]
            break
        else:
            print('\nMaaf Data Pasien Tidak Ada')
            break
    semuapasien()

def hapuspasiengigi():
    pasiengigi()
    kodepasien=pasien.keys()
    kodepasien=int(input('Masukkan Kode Pasien Untuk Menghapus Data Pasien (4 digit Angka): '))
    while True:
        if kodepasien in pasien.keys():
            print('\nTerimakasih Data Telah Terhapus')
            del pasien[kodepasien]
            break
        else:
            print('\nMaaf Data Pasien Tidak Ada')
            break
    pasiengigi()

def hapuspasientht():
    pasientht()
    kodepasien=pasien.keys()
    kodepasien=int(input('Masukkan Kode Pasien Untuk Menghapus Data Pasien (4 digit Angka): '))
    while True:
        if kodepasien in pasien.keys():
            print('\nTerimakasih Data Telah Terhapus')
            del pasien[kodepasien]
            break
        else:
            print('\nMaaf Data Pasien Tidak Ada')
            break
    pasientht()

def hapuspasienmata():
    pasienmata()
    kodepasien=pasien.keys()
    kodepasien=int(input('Masukkan Kode Pasien Untuk Menghapus Data Pasien (4 digit Angka): '))
    while True:
        if kodepasien in pasien.keys():
            print('\nTerimakasih Data Telah Terhapus')
            del pasien[kodepasien]
            break
        else:
            print('\nMaaf Data Pasien Tidak Ada')
            break
    pasienmata()

def klinik():
    while True:
        halamanklinik = input('''
        Daftar Klinik :

        1. Seluruh Pasien
        2. Pasien Klinik Gigi
        3. Pasien Klinik THT
        4. Pasien Klinik Mata
        5. Kembali ke Menu Utama
        
        Ketik Angka Klinik yang Ingin Dituju : ''')

        if(halamanklinik == '1'):
            semuapasien()
        elif(halamanklinik == '2'):
            pasiengigi()
        elif (halamanklinik == '3'):
            pasientht()
        elif (halamanklinik == '4'):
            pasienmata()
        elif(halamanklinik == '5'):
            hospital()
            break
        else:
            print('\nMaaf Klinik yang Anda Tuju Tidak Tersedia, Mohon Cek Kembali Klinik Tujuan Anda ')



def klinikhapus():
    while True:
        halamanhapus = input('''
        Daftar Klinik :

        1. Seluruh Pasien
        2. Pasien Klinik Gigi
        3. Pasien Klinik THT
        4. Pasien Klinik Mata
        5. Kembali ke Menu Utama
        
        Ketik Angka Klinik yang Ingin Dituju : ''')

        if(halamanhapus == '1'):
            hapuspasien()
        elif(halamanhapus == '2'):
            hapuspasiengigi()
        elif (halamanhapus == '3'):
            hapuspasientht()
        elif (halamanhapus== '4'):
            hapuspasienmata()
        elif (halamanhapus == '5'):
            print(hospital())
            break

def hospital ():
    while True:
        halamanutama = input('''
        Selamat Datang di Rumah Sakit Purwadhika :

        Halaman Utama
        1. Data Pasien
        2. Memasukkan Data Pasien Baru
        3. Memperbarui Data Pasien
        4. Hapus Data Pasien
        5. Keluar Halaman
        
        Ketik Angka Menu yang Ingin Dijalankan : ''')

        if(halamanutama == '1'):
            klinik()
        elif(halamanutama == '2'):
            kliniktambah()
        elif (halamanutama == '3'):
            klinikupdate()
        elif (halamanutama == '4'):
            klinikhapus()
        elif (halamanutama == '5'):
            print('Terimakasih, Semoga Lekas Sembuh')
        else:
            print('\nMaaf Menu yang Anda Pilih Tidak Tersedia, Mohon Cek Kembali Menu yang Anda Pilih')
        break

hospital()