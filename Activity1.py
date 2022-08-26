
num = int(input("Enter a number "))
var = num % 4
cen = num % 400
var1 = num % 100

if var > 0:
	print(num + " is not a leap year.")
else:
	if var1 == 0:
		if cen > 0:
			print(num , " is not a leap year.")
		else:
			print(num , "is a leap year.")
	else:
		print(num , "is a leap year.")