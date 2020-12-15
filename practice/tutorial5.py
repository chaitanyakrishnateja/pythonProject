Price_of_Housse = 1000000
Salary = 50000
if Salary > 100000:
    DOWNPAYMENTT = 0.1 * Price_of_Housse
else:
    DOWNPAYMENTT = 0.2 * Price_of_Housse
print(f"DOWN PAYMENT : ${DOWNPAYMENTT} ")
REMAINING_AMOUNT = Price_of_Housse-DOWNPAYMENTT
Salary_Cutoff = Salary*0.6
print(Salary_Cutoff)
MONTHLY_EMI = REMAINING_AMOUNT/Salary_Cutoff
print(MONTHLY_EMI)
