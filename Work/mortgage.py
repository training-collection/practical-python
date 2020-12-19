# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_term = 0.0

extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:

    if payment_term >= extra_payment_start_month and payment_term <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    else:
        principal = principal
        total_paid = total_paid

    if principal > payment * (1+rate/12):
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        payment_term = payment_term + 1
    else:
        final_payment = principal * (1+rate/12)
        principal = principal * (1+rate/12) - final_payment
        total_paid = total_paid + final_payment
        payment_term = payment_term + 1

    print(payment_term, total_paid, principal)

print(f'The total paid is ${total_paid:0.2f} over {payment_term:0.0f} months')
print(f'Monthly payments were ${payment} with a final payment of ${final_payment:0.2f}')
