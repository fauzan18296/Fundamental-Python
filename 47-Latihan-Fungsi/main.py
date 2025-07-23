'''Latihan Fungsi'''
import os
# Program menghitung luas dan keliling persegi panjang

# # Membuat header
# os.system('clear')
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user
# LEBAR = int(input("Masukan nilai lebar: "))
# PANJANG = int(input("Masukan nilai panjang: "))

# # Program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG + LEBAR)

# # Tampilkan hasilnya
# print(f"Hasil perhitungan luas = {LUAS}")
# print(f"Hasil perhitungan keliling = {KELILING}")

def header():
  '''Fungsi header'''
  os.system('clear')
  print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
  print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
  print(f"{'-'*40:^40}")

def input_user():
  '''Fungsi input user'''
  # Mengambil input user
  lebar = int(input("Masukan nilai lebar: "))
  panjang = int(input("Masukan nilai panjang: "))
  return lebar, panjang

def hitung_luas(lebar, panjang):
  '''Fungsi luas'''
  return lebar*panjang

def hitung_keliling(lebar, panjang):
  '''Fungsi keliling'''
  return 2*(lebar + panjang)

def display(message, value):
  '''Fungsi display'''
  print(f"Hasil perhitungan {message} = {value}")

def opsi_hitung_luas_atau_keliling(luas, keliling):
  '''Fungsi opsi'''
  opsi = input("Pilih opsi menghitung (luas atau keliling)? ")
  if opsi == 'luas':
    return display("luas", luas)
  elif opsi == 'keliling':
    return display("keliling", keliling)

# Program utamanya
while True:
  header()
  LEBAR, PANJANG = input_user()
  LUAS = hitung_luas(LEBAR, PANJANG)
  KELILING = hitung_keliling(LEBAR, PANJANG)
  opsi_hitung_luas_atau_keliling(LUAS, KELILING)
  
  is_continue = input("Apakah lanjut (y/n)? ")
  if is_continue == 'n':
    break

print("Program selesai, terimakasih!🙏🙏")