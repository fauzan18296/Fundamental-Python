## Global dan Local Scope

nama_global = "Otong" # <- Ini variabel global
def fungsi():
  print(f"fungsi menampilkan {nama_global}")
fungsi()

# Akses variabel global dalam loop
for i in range(0, 5):
  print(f"loop {i} - {nama_global}")

# Percabangan
if True:
  print(f"if menampilkan {nama_global}")

## Variabel Local Scope
def fungsi_2():
  nama_local = "Ucup" # <- variabel local scope

fungsi_2()
# print(nama_local) # tidak bisa dilakukan bos

# Contoh 1: penggunaan akses variabel
def say_otong():
  print(f"Hello {nama}")
nama = "Otong"
say_otong()

## Contoh 2: merubah variabel global
angka = 0
name = "Ucup"

def ubah_angka(nilai_baru, nama_baru):
  global angka # fungsi ini mendapat akses merubah angka
  global name
  angka = nilai_baru
  name = nama_baru

print(f"Sebelum {angka, name}")
ubah_angka(10, "Otong")
print(f"Sesudah {angka, name}")

## Contoh 3:
angka = 0

for i in range(0, 5):
  angka += i
  angka_dummy = 0
print(angka)
print(angka_dummy)

if True:
  angka = 10
  angka_dummy = 10
print(angka)
print(angka_dummy)