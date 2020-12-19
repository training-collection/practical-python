# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_term = 0.0
extra_payment = 1000.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    payment_term = payment_term + 1
    if payment_term < 13:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    else:
        principal = principal
        total_paid = total_paid


print('Total paid', total_paid)
print('Payment term', payment_term)
