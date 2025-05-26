# Latihan konversi satuan temperature
# Program konversi celcius ke satuan lain
print('\nPROGRAM KONVERSI TEMPERATUR\n')
celcius = float(input('Masukan suhu dalam celcius : '))
print('Suhu adalah ', celcius, 'Celcius')

print('\n===KONVERSI SUHU TEMPERATURE SATUAN CELCIUS KE SATUAN TEMPERATURE YANG LAIN===\n')
# Celcius To Reamur
celcius_to_reamur = (4/5) * celcius
print('Suhu dalam reamur adalah ', celcius_to_reamur, 'Reamur')
# Celcius To Fahrenheit
celcius_to_fahrenheit = ((9/5) * celcius) + 32
print('Suhu dalam fahrenheit adalah ', celcius_to_fahrenheit, 'Fahrenheit')
# Celcius To Kelvin
celcius_to_kelvin = celcius + 273
print('Suhu dalam kelvin adalah ', celcius_to_kelvin, 'Kelvin')

print('\n===KONVERSI SUHU TEMPERATURE FAHRENHEIT KE KELVIN DAN KELVIN KE FAHRENHEIT===\n')
fahrenheit = float(input('Masukan suhu dalam fahrenheit : '))
print('Suhu adalah ', fahrenheit, 'Fahrenheit')
# Fahrenheit To Kelvin
fahrenheit_to_kelvin = ((fahrenheit - 32) * (5/9)) + 273.15
print('Suhu dalam fahrenheit ke kelvin  adalah ', fahrenheit_to_kelvin, 'Kelvin')

kelvin = float(input('Masukan suhu dalam kelvin : '))
print('Suhu adalah ', kelvin, 'Kelvin')
# Kelvin To Fahrenheit
kelvin_to_fahrenheit = ((kelvin - 273.15) * (9/5)) + 32
print('Suhu dalam kelvin ke fahrenheit adalah ', kelvin_to_fahrenheit, 'Fahrenheit')