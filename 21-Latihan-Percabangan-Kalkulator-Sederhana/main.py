# Latihan

# Kalkulator sederhana
import operator


print(10*"=")
print("Kalkulator Sederhana")
print(10*"=" + "\n")

number_1 = float(input("masukan angka 1 = "))
operator = input("operator (+, -, X, /) : ")
number_2 = float(input("masukan angka 2 = "))
# Percabangannya 

if operator == '+':
  result = number_1 + number_2
  print(f"hasilnya adalah {result}")
elif operator == "-":
  result = number_1 - number_2
  print(f"hasilnya adalah {result}")
elif operator == "X" or operator == "*":
  result = number_1 * number_2
  print(f"hasilnya adalah {result}")
elif operator == "/":
  result = number_1 / number_2
  print(f"hasilnya adalah {result}")
else:
  print("masukan yang bener dong!, aku pusying")
  
print("Akhir dari program, terima gajih!")