# Operasi Aritmatika

a = 10
b = 3
# Operasi Tambah +
result = a + b
print(a, ' + ', b, ' = ', result)

# Operasi Pengurangan -
result = a - b
print(a, ' - ', b, ' = ', result)

# Operasi Perkalian *
result = a * b
print(a, ' * ', b, ' = ', result)

# Operasi Pembagian /
result = a / b
print(a, ' / ', b, ' = ', result)

# Operasi Eksponen(pangkat) **
result = a ** b
print(a, ' ** ', b, ' = ', result)

# Operasi Modulus(sisa pembagian) %
result = a % b
print(a, ' % ', b, ' = ', result)

# Operasi Floor Division(pembagian dibulat ke bawah) //
result = a // b
print(a, ' // ', b, ' = ', result)

# Prioritas Operasi, Operational Precedence
'''
  1. ()
  2. exponen **
  3. perkalian dan teman-teman *, /, **, //, %
  4. pertambahan dan pengurangan +, -
'''
x = 3
y = 2
z = 4
results = x ** y * (z + x) / y - y % z // x
print(x, ' ** ', y,' * ', z,' + ', x, ' / ', y,' - ',y, ' % ', z, ' // ', x, ' = ', results)
# Jika ada tanda kurung maka akan di operasikan dahulu atau di hitung dahulu
results = ( x + y ) * z
print('(',x, ' + ', y, ') * ', z, ' = ', results)