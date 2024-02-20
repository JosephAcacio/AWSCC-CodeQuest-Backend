from module import divide_numbers

try:
    a = int(input("Enter the dividend: "));
    b = int(input("Enter the divisor: "));
    quotient = "{:.2f}".format(divide_numbers(a,b));
except Exception as e:
    print(f"Invalid input: {e}")
else:
    print(f"the quotient is: {quotient}")
