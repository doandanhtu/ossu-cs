def main():
    balance = 2400
    annual_interest_rate = 0.1
    print(f"Lowest Payment: {lowest_payment(balance, annual_interest_rate)}")


def lowest_payment(balance, annual_interest_rate):
    payment = (balance // 120) * 10
    while remaining_balance(balance, annual_interest_rate, payment) > 0:
        payment += 10
    return payment


def remaining_balance(balance, annual_interest_rate, payment):
    monthly_interest_rate = annual_interest_rate / 12
    for i in range(12):
        balance -= payment
        balance = balance * (1 + monthly_interest_rate)
    return balance


main()