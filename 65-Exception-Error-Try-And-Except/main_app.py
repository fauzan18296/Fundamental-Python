# Exception akan terjadi saat program 
# mengalami error saat runtime

# Contoh sederhana untuk menangkap exception
from math import nan

## Contoh sederhana
# input_user = int(input("Masukan angka: "))
# hasil = nan

# try:
#   hasil = 10 / input_user
# except:
#   print("Input tidak boleh 0!")
# print(f"hasil = {hasil}")

# Contoh di aplikasi
while True:
  angka = int(input("Masukan angka pembagi: "))
  try:
    hasil = 10 / angka
    print(f"hasil = {hasil}")
    is_done = input("lanjutkan (y/n)? ")
    if is_done == 'n':
      break
  except:
    print("Pembagi nol, Silahkan masukan input lagi")
print("Akhir dari program 1")

try:
  with open("data.txt", 'r') as file:
    print(file.read())
except:
  print("file data.txt tidak ditemukan, membuat file baru")
  with open("data.txt", "w", encoding='utf-8') as file:
    file.write("file baru")
print("Akhir dari program 2")