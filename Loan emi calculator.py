def calculate_emi(principal, annual_rate, months):
    monthly_rate = annual_rate / 12 / 100
    emi = (principal * monthly_rate * ((1 + monthly_rate) ** months)) / (((1 + monthly_rate) ** months) - 1)
    return round(emi, 2)

print(calculate_emi(10000, 7.5, 36))