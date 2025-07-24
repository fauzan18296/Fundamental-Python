# Import

# Fungsi nya adalah untuk mengambil
# program dari file external .py

# 1. Untuk menyambung program dari external
import program_print
import program_ucup

# 2. Import dengan data
import variable
import kucuy
# data ada di namespace variable
print(variable.data)
print(kucuy.data)

# 3. Import dengan fungsi
import matematika
hasil = matematika.tambah(4, 5)
print(hasil)