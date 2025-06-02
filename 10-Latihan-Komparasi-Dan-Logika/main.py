# Episode latihan komparasi dan logika

# Membuat gabungan area rentang dari angka 

# +++++3---------10+++++

input_user = float(input("Masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# +++++3-----------
# Memeriksa ngka kurang dari 3
is_kurang_dari = (input_user < 3)
print("Kurang dari 3 = ", is_kurang_dari)

# ---------------10+++++
# Memeriksa angka lebih dari 10
is_lebih_dari = (input_user > 10)
print("Lebih dari 10 = ", is_lebih_dari)

# +++++3--------------10+++++
is_correct = is_kurang_dari or is_lebih_dari
print("Angka yang anda masukan : ", is_correct)

# ------3++++++++++10-------
# Kasus irisan
print("\n", 10*"=", "\n")
input_user = float(input("Masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))
# ------3+++++++++++++
# lebih dari 3
is_lebih_dari = input_user > 3
print("Lebih dari 3 = ", is_lebih_dari)

# ++++++++++10-------
# kurang dari 10
is_kurang_dari = input_user < 10
print("Kurang dari 10 = ", is_kurang_dari)

# ------3++++++++++10-------
is_correct = is_kurang_dari and is_lebih_dari
print("Angka yang anda masukan : ", is_correct)

# Tugas 1
print('\n====Tugas 1====')
# -------0++++++5------8++++++11-------
input_number = float(input("\nMasukan angka yang bernilai\nlebih dari 0 \ndan kurang dari 5 \ndan lebih dari 8 \ndan kurang dari 11 : "))

is_lebih_dari_0 =  input_number > 0
print("Lebih dari 0 = ", is_lebih_dari_0)
is_kurang_dari_5 = input_number < 5
print("Kurang dari 5 = ", is_kurang_dari_5)
is_lebih_dari_8 = input_number > 8
print("Lebih dari 8 = ", is_lebih_dari_8)
is_kurang_dari_11 = input_number < 11
print("Kurang dari 11 = ", is_kurang_dari_11)

isCorrect = is_lebih_dari_0 and is_kurang_dari_5 or is_lebih_dari_8 and is_kurang_dari_11
print("Angka yang anda masukan : ", isCorrect)

# Tugas 2
print('\n====Tugas 2====')
# ++++++0------5++++++8------11++++++
input_number = float(input("\nMasukan angka yang bernilai\nkurang dari 0 \natau lebih dari 5 \natau kurang dari 8 \natau lebih dari 11 : "))

is_kurang_dari_0 =  input_number < 0
print("Kurang dari 0 = ", is_kurang_dari_0)
is_lebih_dari_5 = input_number > 5
print("Lebih dari 5 = ", is_lebih_dari_5)
is_kurang_dari_8 = input_number < 8
print("Kurang dari 8 = ", is_kurang_dari_8)
is_lebih_dari_11 = input_number > 11
print("Lebih dari 11 = ", is_lebih_dari_11)

isCorrect = is_kurang_dari_0 or is_lebih_dari_5 and is_kurang_dari_8 or is_lebih_dari_11
print("Angka yang anda masukan : ", isCorrect)