def computepay(h,r):
    if h > 40:
        normal_pay = 40 * r
        ot_pay = (h - 40) * (1.5 * r)
        pay = normal_pay + ot_pay
    else:
        pay = 40 * r
    return str(pay)

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs,rate)
print("Pay",p)
