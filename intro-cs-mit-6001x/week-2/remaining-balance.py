balance = 42
annual_interest_rate = 0.2
monthly_payment_rate = 0.04

def remaining_balance(balance, annual_interest_rate, monthly_payment_rate, period = 12):
    if period <= 0:
        return balance
    monthly_interest_rate = annual_interest_rate / 12.0
    while period > 0:
        minimum_monthly_payment = monthly_payment_rate * balance
        balance -= minimum_monthly_payment
        balance = round(balance * (1 + monthly_interest_rate), 2)
        #print(f"Month {13 - period} Remaining balance: {balance}")
        period -= 1
    return balance

print(f"Remaining balance: {remaining_balance(balance, annual_interest_rate, monthly_payment_rate)}")