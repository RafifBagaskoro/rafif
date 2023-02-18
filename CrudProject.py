karyawan = [
    {
        'id': 'K01',
        'nama': 'Rafif',
        'umur': 25,
        'department': 'Data',
        'status' : 'Menikah'
    },
    {
        'id': 'K02',
        'nama': 'Donald',
        'umur': 30,
        'department': 'Purchasing',
        'status' : 'Menikah'
    },
    {
        'id': 'K03',
        'nama': 'Budi',
        'umur': 29,
        'department': 'Warehouse',
        'status' : 'Belum Menikah'
    }
]

def melihat_karyawan():
    while True:
            pilihan_menu1 = input('''
===============Pilih Sub-Menu di Bawah===============

1. Daftar seluruh karyawan
2. Detail karyawan 
3. Kembali ke menu utama
            
Menu berapa yang mau anda pilih? : ''')
            if (pilihan_menu1 == '1'):
                print('''
===============Data Karyawan:===============''')
                for a in range(len(karyawan)):
                    print('{}. \t{} = {}\n\t{} = {}\n\t{} = {}\n\t{} = {}\n\t{} = {}\n'.format
                    (a+1,'ID',karyawan[a]['id'],'Nama',karyawan[a]['nama'],'Umur',karyawan[a]['umur'],'Department',karyawan[a]['department'],'Status',karyawan[a]['status'])) 

            elif (pilihan_menu1 == '2'):
                search_karyawan = input('\nID karyawan: ')
                penanda = False
                for a in karyawan:
                    if search_karyawan.upper() in a['id']:
                        penanda = True
                        print('\n{} = {}\n{} = {}\n{} = {}\n{} = {}\n{} = {}\n'.format
                        ('ID',a['id'],'Nama',a['nama'],'Umur',a['umur'],'Department',a['department'],'Status',a['status']))

                if penanda == False:
                        print('''
\nINVALID INPUT :
+++++++++++ ID KARYAWAN TIDAK TERDAFTAR !!!! +++++++++++
                    ''')

            elif (pilihan_menu1 == '3'):
                break
            else:
                print('''
\nINVALID INPUT:
+++++++++++ Pilihan anda tidak ada! Pilihlah 1 - 3 !!! +++++++++++
                    ''')

def menambah_karyawan():
    while True:
        pilihan_menu2 = input('''
===============Pilih Sub-Menu di Bawah===============

1. Menambah Karyawan Baru
2. Kembali ke menu utama
            
Menu berapa yang mau anda pilih? : ''')
        if (pilihan_menu2 == '1'):
            tambah_karyawan = input('\ntambahkan ID karyawan disini: ')
            penanda = False
            for a in karyawan:
                if tambah_karyawan.upper() in a['id']:
                    penanda = True
                    print('''
\nINVALID INPUT :
+++++++++++ ID SUDAH ADA !!! +++++++++++

                    ''')
            
            if penanda == False:
                tambah_nama = input('input nama disini: ')
                while True:
                    tambah_umur = input('input umur disini: ')
                    angka1 = list(range(101))
                    if tambah_umur in [str(x) for x in angka1]:
                        break
                    else:
                        print('''
INVALID INPUT:                   
MASUKKAN ANGKA YANG BENAR! (TIDAK MENERIMA HURUF "ATAU" UMUR LEBIH DARI 100!)
                        ''')
                tambah_department = input('input department disini: ')
                while True:
                    tambah_status = input('sudah menikah atau belum? [Y/N]: ')
                    if tambah_status.lower() == 'y':
                        karyawan.append(
                            {
                            'id': tambah_karyawan.upper(),
                            'nama': tambah_nama.capitalize(),
                            'umur': tambah_umur,
                            'department': tambah_department.capitalize(),
                            'status': 'Menikah'
                            }
                        )
                        break
                    elif tambah_status.lower() == 'n':
                        karyawan.append(
                            {
                            'id': tambah_karyawan.upper(),
                            'nama': tambah_nama.capitalize(),
                            'umur': tambah_umur,
                            'department': tambah_department.capitalize(),
                            'status': 'Belum Menikah'
                            }
                        )
                        break
                while True:
                    fix_or_not = input('apakah karyawan baru sudah bisa di tambahkan? [Y/N]:')
                    if fix_or_not.lower() == 'y':
                        print('''
\n*********** DATA SUDAH DITAMBAH ! ***********
                            ''')
                        break
                    elif fix_or_not.lower() == 'n':
                        print('''
\n******** DATA TIDAK JADI DI TAMBAH ! ********
                        ''')
                        karyawan.pop()
                        break
        elif (pilihan_menu2 == '2'):
            break
        else:
                print('''
\nINVALID INPUT:
+++++++++++ Pilihan anda tidak ada! Pilihlah 1 atau 2 !!! +++++++++++
                    ''')       

def mengupdate_data_karyawan():
    while True:
            pilihan_menu3 = input('''
===============Pilih Sub-Menu di Bawah===============

1. Update Data Karyawan
2. Kembali ke menu utama
            
Menu berapa yang mau anda pilih? : ''')    

            if (pilihan_menu3 == '1'):
                search_karyawan = input('\nID karyawan: ')
                penanda = False
                for a in karyawan:
                    if search_karyawan.upper() in a['id']:
                        penanda = True
                        print('\n{} = {}\n{} = {}\n{} = {}\n{} = {}\n{} = {}\n'.format
                        ('ID',a['id'],'Nama',a['nama'],'Umur',a['umur'],'Department',a['department'],'Status',a['status']))
                        while True:
                            validasi = input('jadi update data karyawana dengan ID : {} ? Y/N:'.format(search_karyawan.upper()))
                            if validasi.lower() == 'y':
                                while True:
                                    input_key = input('Masukkan data apa yang mau di ubah:  ')
                                    if input_key.lower() in a.keys() and input_key.lower() == 'umur':
                                        while True:
                                            input_value = input('Masukkan umur baru: ')
                                            angka1 = list(range(101))
                                            if input_value in [str(x) for x in angka1]:
                                                a[input_key.lower()] = input_value.capitalize()
                                                print('''
\n*********** DATA SUDAH TERUPDATE ! ***********
                                        ''')
                                                break
                                            else:
                                                print('''
INVALID INPUT:                   
MASUKKAN ANGKA YANG BENAR! (TIDAK MENERIMA HURUF "ATAU" UMUR LEBIH DARI 100!)
                        ''')
                                        break
                                    elif input_key.lower() in a.keys() and input_key.lower() == 'status':
                                        while True:
                                            input_value = input('Perubahan status, pilihlah M untuk "Menikah" dan B untuk "Belum Menikah" [M/B]: ')
                                            if input_value.lower() == 'm':
                                                a[input_key.lower()] = 'Menikah'
                                                print('''
\n*********** DATA SUDAH TERUPDATE ! ***********
                                        ''')
                                                break
                                            elif input_value.lower() == 'b':
                                                a[input_key.lower()] = 'Belum Menikah'
                                                print('''
\n*********** DATA SUDAH TERUPDATE ! ***********
                                        ''')
                                                break
                                        break
                                    elif input_key.lower() in a.keys() and input_key.lower() == 'id':
                                        input_value = input('Masukkan isi data baru: ')
                                        a[input_key.lower()] = input_value.upper()
                                        print('''
\n*********** DATA SUDAH TERUPDATE ! ***********
                                        ''')
                                        break
                                    elif input_key.lower() in a.keys():
                                        input_value = input('Masukkan isi data baru: ')
                                        a[input_key.lower()] = input_value.capitalize()
                                        print('''
\n*********** DATA SUDAH TERUPDATE ! ***********
                                        ''')
                                        break
                                    else:
                                        print('''
INVALID INPUT:
DATA YANG DIMASUKKAN SALAH! pilihlah antara ID/Nama/Umur/Department/Status!
                                        ''')
                                break
                            elif validasi.lower() == 'n':
                                print('''
\n******** DATA TIDAK JADI DI UPDATE ! ********
                                ''')
                                break
                if penanda == False:
                    print('''
\nINVALID INPUT:           
+++++++++++ ID KARYAWAN TIDAK ADA ! +++++++++++
                    ''')
            elif(pilihan_menu3 == '2'):
                break
            else:
                print('''
\nINVALID INPUT:
+++++++++++ Pilihan anda tidak ada! Pilihlah 1 atau 2 !!! +++++++++++
                    ''')

def menghapus_data_karyawan():
    while True:
            pilihan_menu4 = input('''
===============Pilih Sub-Menu di Bawah===============

1. Hapus Data Karyawan
2. Kembali ke menu utama
            
Menu berapa yang mau anda pilih? : ''')
            if(pilihan_menu4 == '1'):
                search_karyawan = input('\nID karyawan: ')
                penanda = False
                for a in karyawan:
                    if search_karyawan.upper() in a['id']:
                        penanda = True
                        print('\n{} = {}\n{} = {}\n{} = {}\n{} = {}\n{} = {}\n'.format
                        ('ID',a['id'],'Nama',a['nama'],'Umur',a['umur'],'Department',a['department'],'Status',a['status']))
                        while True:
                            hapus_karyawan = input('anda yakin menghapus data karyawan ini? [Y/N]:')
                            if hapus_karyawan == 'y':
                                karyawan.remove(a)
                                print('''
\n*********** DATA SUDAH TERHAPUS ! ***********
                                ''')
                                break
                            elif hapus_karyawan == 'n':
                                print('''
\n********* DATA TIDAK JADI DIHAPUS ! *********
                                ''')
                                break
                if penanda == False:
                    print('''
\nINVALID INPUT:           
+++++++++++ ID KARYAWAN TIDAK ADA ! +++++++++++
                    ''')
            elif(pilihan_menu4 == '2'):
                break
            else:
                print('''
\nINVALID INPUT:
+++++++++++ Pilihan anda tidak ada! Pilihlah 1 atau 2 !!! +++++++++++
                    ''')
while True:
    print('''
===============Data Karyawan PT.ADS===============''')
    pilihan = input('''
===============Pilih Menu di Bawah===============

1. Daftar Karyawan
2. Menambah Karyawan Baru
3. Mengupdate Data Karyawan
4. Menghapus Data Karyawan
5. Exit Menu

Menu berapa yang mau anda pilih? : ''')
    if (pilihan == '1'):
        melihat_karyawan()
    elif(pilihan == '2'):
        menambah_karyawan()
    elif(pilihan == '3'): 
        mengupdate_data_karyawan()
    elif(pilihan == '4'):
        menghapus_data_karyawan()
    elif(pilihan == '5'):
        print('''
============================================================
===========Penggunaan Sistem Karyawan Ditutup===============
============================================================
        ''')
        break
    else:
        print('''
\nINVALID INPUT:
+++++++++++ Pilihan anda tidak ada! Pilihlah 1-5 !!! +++++++++++
        ''')
