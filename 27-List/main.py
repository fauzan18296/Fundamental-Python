## --- LIST ---

# Kumpulan data numbers
data_angka = [1, 5, 2, 3]
print(data_angka)

# Kumpulan data string
data_string = ["Ucup", "Otong", "Odah"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1, "bala-bala", 2, "cireng", "ucup", True, "otong", False]
print(data_campuran)

# Cara alternatif membuat list
data_range = range(0, 10, 2) # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop, list comprehension 
list_using_for = [i**2 for i in range(0, 10)]
print(list_using_for)

# Membuat list pake for pake if
list_using_for_if = [i for i in range(0, 10) if i != 5]
print(list_using_for_if)

list_using_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_using_for_if)

list_using_for_if = [i**2 for i in range(0, 10) if i % 2 != 0]
print(list_using_for_if)