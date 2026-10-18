#Python calculator
operator = input("Enter operator: ")
if operator == '+':
    a = int(input("Enter a integer: "))
    b = int(input("Enter b integer: "))
    print(a+b)
elif operator == '-':
    a = int(input("Enter big integer: "))
    b = int(input("Enter small integer: "))
    print(a+b)
elif operator == '*':
     a = int(input("Enter a integer: "))
     b = int(input("Enter b integer: "))
     print(a*b)
elif operator == '/':
     a = float(input("Enter big integer: "))
     b = float(input("Enter small integer: "))
     print(a/b)
else:
     print("Invalid operator")