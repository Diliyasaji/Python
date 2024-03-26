tax_rate=0.20
standard_deduction=10000.0
dependent_deduction=3000.0

grossIncome=float(input("enter the gross income"))
num=int(input("enter the no.of depenents:"))
#taxableIncome-portion of gross income subject to taxes
taxableIncome=grossIncome-standard_deduction-\
               dependent_deduction*num
incomeTax=taxableIncome*tax_rate
print("income tax is $"+str(incomeTax))
