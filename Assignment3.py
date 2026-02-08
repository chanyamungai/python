grossincome = int(input("Enter Gross Income: "))

if grossincome <= 0:
    print("Invalid input")   
elif grossincome <= 5999:
    print("Monthly contribution is:", 150.00)
elif grossincome <= 7999:
    print("Monthly contribution is:", 300.00)
elif grossincome <= 11999:
    print("Monthly contribution is:", 400.00)
elif grossincome <= 14999:
    print("Monthly contribution is:", 500.00)
elif grossincome <= 19999:
    print("Monthly contribution is:", 600.00)
elif grossincome <= 24999:
    print("Monthly contribution is:", 750.00)
elif grossincome <= 49999:
    print("Monthly contribution is:", 1000.00)
elif grossincome <= 99999:
    print("Monthly contribution is:", 1500.00)
else:
    print("Monthly contribution is:", 2000.00)
