#-----------------------------------------------------------------------
# Neina Cichon
# Name: Calculate Pay
# Date: June 13, 2020
#-----------------------------------------------------------------------

# ask for input and declare variables
dblPayRate = float(input("Please enter hourly pay rate: "))
dblHoursWorked = float(input("Please enter hours worked: "))
dblNetPay = float()
dblGrossPay = float()
dblTax = float()

# Make sure both pay rate and hours worked are not negative
if dblPayRate > 0:
	if dblHoursWorked > 0:
		dblGrossPay = dblPayRate * dblHoursWorked #Calculate Gross Pay

	if dblGrossPay <= 300: #check if pay is less than $300 and calc taxes
		dblTax = dblGrossPay * .15

	elif dblGrossPay <= 450: #check if pay is less than $450 and calc taxes
		dblTax = ((dblGrossPay - 300) * .20) + 45
		
	else:
		dblTax = ((dblGrossPay - 450) * .25) + 75 # Calc taxes for pay above $450

	dblNetPay = dblGrossPay - dblTax # Calculate Net Pay
	# Print Results
	print("Pay Rate: ", dblPayRate, "\nHoursWorked", dblHoursWorked, "\nGross Pay: ", dblGrossPay, "\nNet Pay: ", dblNetPay, "\nTaxes: ", dblTax)
else:
	print("Invalid entry. Pay rate and hours worked cannot be negative.") #Return Error if negative values are entered

