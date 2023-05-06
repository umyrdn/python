class Mahasiswa(object):
    nim = None
    nama = None

data_mahasiswa = []

def tampilkan_mahasiswa():
    print('Daftar Mahasiswa')
    print('-------------------------------')
    print('NO\tNIM\t\tNama')
    print('-------------------------------')
    no = 1

    for mahasiswa in data_mahasiswa:
        print('{}\t{}\t\t{}'.format(no, mahasiswa.nim, mahasiswa.nama))
        no = no + 1

    print()

def tambahkan_mahasiswa():
    print('Tambah Mahasiswa')
    print('--------------------')
    mahasiswa = Mahasiswa()
    mahasiswa.nim = input('Masukkan NIM: ')
    mahasiswa.nama = input('Masukkan Nama: ')

    data_mahasiswa.append(mahasiswa)

def cari_mahasiswa():
    nim_cari = input ('Masukkan NIM Yang Dicari: ')
    index = 0

    for mahasiswa in data_mahasiswa:
        if mahasiswa.nim == nim_cari:
            print('Mahasiswa dengan NIM {} ditemukan!'.format(nim_cari))
            return index
        
        index += 1

    print('Mahasiswa dengan NIM {} tidak ditemukan!'.format(nim_cari))
    return -1

def ubah_mahasiswa():
    index_mahasiswa = cari_mahasiswa()

    if index_mahasiswa == -1:
        return
    
    nama_baru = input('Masukkan Nama Baru: ')
    data_mahasiswa[index_mahasiswa].nama = nama_baru

def hapus_mahasiswa():
    index_mahasiswa = cari_mahasiswa()

    if index_mahasiswa == -1:
        return
    
    del data_mahasiswa[index_mahasiswa]

def menu():
    print('1. Tampilkan Mahasiswa')
    print('2. Tambahkan Mahasiswa')
    print('3. Cari Mahasiswa')
    print('4. Ubah Mahasiswa')
    print('5. Hapus Mahasiswa')
    print('6. Keluar')
    menu_pilih = int(input('Pilih Menu: '))

    if menu_pilih < 1 or menu_pilih > 6:
        return menu()
    
    return menu_pilih

while True:
    pilih_menu = menu()

    if pilih_menu == 1:
        tampilkan_mahasiswa()
    elif pilih_menu == 2:
        tambahkan_mahasiswa()
    elif pilih_menu == 3:
        cari_mahasiswa()
    elif pilih_menu == 4:
        ubah_mahasiswa()
    elif pilih_menu == 5:
        hapus_mahasiswa()
    elif pilih_menu == 6:
        break
