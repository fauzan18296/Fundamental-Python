# Module matematika dengan import

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as p
# from matematika import * # * <- Untuk mengambil semua yang ada di module matematika

import matematika as math #

hasil_tambah = add(1, 2, 3, 4, 5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1, 2, 3, 4, 5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = p(3)
print(f"Hasil pangkat3 = {pangkat_3(3)}")