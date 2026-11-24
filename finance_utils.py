# finance_utils.py

def simple_interest(p, r, t):
    """Return the simple interest for principal p, annual rate r (%), and time t (years)."""
    if p <= 0 or r < 0 or t <= 0:
        raise ValueError("Principal and time must be positive; interest rate cannot be negative.")
    return round((p * r * t) / 100, 2)


def emi(p, r, n):
    """Return the Equated Monthly Installment (EMI) for principal p, rate r (%), and n months."""
    if p <= 0 or r < 0 or n <= 0:
        raise ValueError("Principal and tenure must be positive; interest rate cannot be negative.")
    if r == 0:
        return round(p / n, 2)
    monthly_rate = r / (12 * 100)
    factor = (1 + monthly_rate) ** n
    return round((p * monthly_rate * factor) / (factor - 1), 2)


def total_amount(p, r, t):
    """Return the total amount payable (Principal + Simple Interest)."""
    return round(p + simple_interest(p, r, t), 2)


if __name__ == "__main__":
    print("simple_interest(10000, 5, 2):", simple_interest(10000, 5, 2))
    print("simple_interest(50000, 8.5, 3):", simple_interest(50000, 8.5, 3))
    print("emi(100000, 12, 12):", emi(100000, 12, 12))
    print("emi(500000, 10, 60):", emi(500000, 10, 60))
    print("total_amount(10000, 5, 2):", total_amount(10000, 5, 2))
    print("total_amount(50000, 8.5, 3):", total_amount(50000, 8.5, 3))
