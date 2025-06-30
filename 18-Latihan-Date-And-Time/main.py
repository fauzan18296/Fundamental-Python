# Date and time (latihan)

import datetime as dt

# day_now = dt.date.today()
# print(day_now)
# print(f"Hari ini adalah hari = {day_now:%A}")

# date = dt.date(2007, 1, 18)
# print(date)
# print(f"Hari ini adalah hari = {date:%A}")

print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
date = int(input("Tanggal  \t:"))
month = int(input("Bulan  \t\t:"))
year = int(input("Tahun  \t\t:"))

date_of_birth = dt.date(year, month, date)
print(f"Tanggal lahir anda adalah: {date_of_birth}")

date_now = dt.date.today()
print(f"Hari ini tanggal: {date_now}")
age_day = date_now - date_of_birth
age_year = age_day.days // 365
age_month_residual = (age_day.days % 365) // 30
print(f"Hari nya adalah: {date_of_birth:%A}")
print(f"Umur anda adalah: {age_year} tahun, {age_month_residual} bulan")