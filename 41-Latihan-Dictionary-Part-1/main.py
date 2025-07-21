import datetime as dt
import os

# Template dictionary mahasiswa
mahasiswa_template = {
  'nama': 'nama',
  'nim': '00000000',
  'sks_lulus': 0,
  'lahir': dt.datetime(1111, 1, 11),
}

data_mahasiswa = {}

# os.system('cls') # untuk windows
os.system('clear')
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-"*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
TAHUN_LAHIR = int(input("Tahun lahir (YYY): ")) 
BULAN_LAHIR = int(input("Tahun lahir (1-12): ")) 
TANGGAL_LAHIR = int(input("Tahun lahir (1-31): ")) 
mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
print(mahasiswa)