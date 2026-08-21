name = input("Employee name: ")
rate_hr = float(input("Hourly rate: ").replace(",", ""))
work_hr = float(input("Regular Hours Worked: ").replace(",", ""))
ot_hr = float(input("Overtime Hours: ").replace(",", ""))
bonus = float(input("Bonus: ").replace(",", ""))
regular_pay = float(rate_hr * work_hr)
ot_pay = float(ot_hr * 1.5 * rate_hr)
gross_pay = float(regular_pay + ot_pay + bonus)


if gross_pay <= 20000:
    tax = gross_pay * 0.05

elif gross_pay > 20000 and gross_pay <= 40000:
    tax = gross_pay * 0.1

elif gross_pay > 40000:
    tax = gross_pay * 0.15

net_pay = (gross_pay - tax)



print("=============================")
print("       PAYROLL SUMMARY       ")
print("=============================")
print("")
print("Employee: " + name)
print("")
print(f"Hourly rate: ₱{rate_hr:,}")
print(f"Regular Hours: {work_hr:,}")
print(f"Overtime Hours: {ot_hr:,}")
print(f"Bonus: ₱{bonus:,}")
print('')
print(f"Regular pay: ₱{regular_pay:,}")
print(f"Overtime pay: ₱{ot_pay:,}")
print(f"Gross pay: ₱{gross_pay:,}")
print('')
print(f"Tax: ₱{tax:,}")
print(f"Net pay: ₱{net_pay:,}")







