# __main__ adalah top level environment

# __name == "__main__" NOTE: Akan terjadi jika ada di file program utama

##__name__ pada file program utama
print(f"nilai __name__ pada main.py = '{__name__}'")

## __name__ pada file program eksternal
import fungsi

# Contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a: int, b: int) -> int:
  return a + b

# fungsi utama
if __name__ == "__main__":
  angka1 = 5
  angka2 = 10
  hasil = fungsi_tambah(angka1, angka2)
  print(f"Hasil tambah = {hasil}")

## import package
import package