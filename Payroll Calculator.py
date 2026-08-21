name = input("Name: ")

def valid_num (prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number")
                continue
            return value


        except ValueError:
            print("Please enter a numeric value")

rate_hr = valid_num("Hourly rate: ")
work_hr = valid_num("Working hours: ")
ot_hr = valid_num("Overtime hours: ")
bonus = valid_num("Bonus: ")
OT_MULTIPLIER = 1.5

def calc_RP (work_hr, rate_hr):
    regular_pay = rate_hr * work_hr
    return regular_pay

def calc_op (ot_hr, OT_MULTIPLIER, rate_hr):
    ot_pay = ot_hr * OT_MULTIPLIER * rate_hr
    return ot_pay

def calc_gp (regular_pay, ot_pay, bonus):
    gross_pay = regular_pay + ot_pay + bonus
    return gross_pay

regular_pay = calc_RP (work_hr, rate_hr)
ot_pay = calc_op (ot_hr, OT_MULTIPLIER, rate_hr)
gross_pay = calc_gp (regular_pay, ot_pay, bonus)


def calc_tax (gross_pay):
    if gross_pay <= 20000:
        return gross_pay * 0.05

    elif 20000 < gross_pay <= 40000:
        return gross_pay * 0.10

    else:
        return gross_pay * 0.15



tax = calc_tax (gross_pay)

def calc_np (gross_pay, tax):
    net_pay = gross_pay - tax
    return net_pay

net_pay = calc_np (gross_pay, tax)

print("===============================")
print("         Payroll Summary       ")
print("===============================")
print()
print("Employee: " + name)
print()
print(f"Hourly rate: ₱{rate_hr:,.2f}")
print(f"Regular hours:  {work_hr:,.2f}")
print(f"Overtime hours:  {ot_hr:,.2f}")
print(f"Bonus: ₱{bonus:,.2f}")
print("-------------------------------")
print(f"Regular pay: ₱{regular_pay:,.2f}")
print(f"Overtime pay: ₱{ot_pay:,.2f}")
print(f"Gross pay: ₱{gross_pay:,.2f}")
print(f"Tax: ₱{tax:,.2f}")
print(f"Net pay: ₱{net_pay:,.2f}")
