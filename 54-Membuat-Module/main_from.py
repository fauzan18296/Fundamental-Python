# Module matematika dengan import

from matematika import tambah, kali, pangkat
# from matematika import * # * <- Untuk mengambil semua yang ada di module matematika

hasil_tambah = tambah(1, 2, 3, 4, 5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = kali(1, 2, 3, 4, 5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"Hasil pangkat3 = {pangkat_3(3)}")