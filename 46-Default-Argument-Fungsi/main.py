'''Default Argument'''
# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

# Contoh 1
def say_hello(nama = "Ganteng"):
  '''Fungsi dengan default argument'''
  print(f"Hallo {nama}")
say_hello("Ucup")
say_hello()

# Contoh 2
def sapa_dia(nama, pesan = "Apa kabar?"):
  '''Fungsi dengan satu input biasa, dan satu default argument'''
  print(f"hai {nama}, {pesan}")
sapa_dia("Dudung", "Hai Ganteng")
sapa_dia("Otong")

# Contoh 3
def hitung_pangkat(angka, pangkat = 2):
  hasil = angka**pangkat
  return hasil
print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(pangkat = 3, angka = 5)
print(hasil)

# Contoh 4
def fungsi(input_1 = 1, input_2 = 2, input_3 = 3, input_4 = 4):
  hasil = input_1 + input_2 + input_3 + input_4
  return hasil
print(fungsi())
print(fungsi(input_3 = 10)) # Akses default argument yang ingin kita ubah