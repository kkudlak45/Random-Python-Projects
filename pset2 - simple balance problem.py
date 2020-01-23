# Kryzstof Kudlak
# 7/16/18
# 6.00.1x PSET 2 - Paying off Debt

balance = 484
annualInterestRate = .2
monthlyPaymentRate = .04

irate = annualInterestRate/12
prate = monthlyPaymentRate

for i in range(12):
    balance = balance - prate * balance
    balance = balance + balance * irate

print("Remaining balance: " + str(round(balance,2)))
