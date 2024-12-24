def main():
    balance = 9999999
    annual_interest_rate = 0.18

    # Calculate the monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12.0

    # Define lower bound and upper bound
    lo = balance / 12.0
    hi = balance * ((1 + monthly_interest_rate) ** 12) / 12.0

    # Handle the case where the lower bound is the result
    if remaining_balance(balance, monthly_interest_rate, round(lo, 2)) <= 0:
        result = round(lo, 2)

    # A recursive function is called to handle other cases
    else:
        result = lowest_payment(balance, monthly_interest_rate, lo, hi)

    # Print the result
    print(f"Lowest Payment: {result}")


def lowest_payment(balance, monthly_interest_rate, lo, hi):
    # Define a small number to avoid floating point errors
    eps = 0.01

    # Initiate a payment value
    payment = (lo + hi) / 2.0

    # Base case: payment is sufficient AND upper bound and lower bound converges to ensure smallest
    if remaining_balance(balance, monthly_interest_rate, payment) < 0 and abs(hi - lo) <= eps:
        return round(payment, 2)
    
    # Recursive case: if payment is not sufficient then adjust the lower bound to payment
    if remaining_balance(balance, monthly_interest_rate, payment) > 0:
        return lowest_payment(balance, monthly_interest_rate, payment, hi)
    
    # Recursive case: if payment is sufficient then adjust the upper bound to payment to find a smaller payment
    if remaining_balance(balance, monthly_interest_rate, payment) < 0:
        return lowest_payment(balance, monthly_interest_rate, lo, payment)


def remaining_balance(balance, monthly_interest_rate, payment):
    for i in range(12):
        balance -= payment
        balance = balance * (1 + monthly_interest_rate)
    return balance


main()



