#if = do some code if condtn is true
#else do something else 

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
elif age < 0:
    print("you havent been born yet")
else:
    print("not eligible")