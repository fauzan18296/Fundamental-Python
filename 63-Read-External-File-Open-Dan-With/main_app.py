## Tutorial membaca file external
print(3*"=", " Membaca file txt ", 3*"=")
file = open("data.txt", mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

## baca seluruh file 
print(file.read())

## baca per baris 
# print(file.readline(), end="") # baca baris pertama
# print(file.readline(), end="") # baca baris kedua

## baca semua baris sebagai list
# print(file.readlines())

print(f"Apakah file sudah diclose : {file.closed}")
file.close()
print(f"Apakah file sudah diclose : {file.closed}")

## Salah satu teknik membuka file di python

print("\n", 3*"=", " Membaca file txt dengan with ", 3*"=")

# keyword with adalah salah satu teknik untuk membuka file di python secara mudah tanpa adanya method file.close() atau close secara manual
with open("data.txt", mode="r") as file:
  content = file.readline()
  print(content, end="")
  print(f"Apakah file sudah diclose : {file.closed}")
print(f"Apakah file sudah diclose : {file.closed}")