gross_salary=float(input("Enter the gross salary (in INR):"))
allowance=gross_salary/10
deduction=gross_salary*(3/100)
net_salary=gross_salary+allowance-deduction
print("Your net salary is",net_salary,"INR")