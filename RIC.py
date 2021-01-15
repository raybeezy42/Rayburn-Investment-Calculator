!/usr/bin/python

principal = float(input("Enter the intial investment amount "))

interest = float(input("Enter the annual interest rate as a decimal "))

balance = principal

year = 0

while balance < 2 * principal:
	balance = balance * (1 + interest)
	year += 1

print ('It will take {0} years to double your investment'.format(year))