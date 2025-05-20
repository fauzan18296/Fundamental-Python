# Episode input user

# Data yang dimasukkan pasti bertipe string
data = input("Masukkan data : ")
print('data = ', data, ', type = ', type(data))

# Jika kita ingin mengambil data dengan bertipe integer, maka
numbers = int(input("Masukkan angka : "))
print('data = ', numbers, ', type = ', type(numbers))
numbers = float(input("Masukkan angka : "))
print('data = ', numbers, ', type = ', type(numbers))

# Bagaimana dengan tipe data boolean
biner = bool(int(input("Masukkan nilai boolean : ")))
print('data = ', biner, ', type = ', type(biner))