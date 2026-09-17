principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
Compound_interest = principal * ((1 + rate / 100) ** time) - principal
print("Compound interest =", Compound_interest)