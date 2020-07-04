num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("{} is an even number".format(num))
    else:
        print("{} is an odd number".format(num))
else:
    print("Number is less than or equal to zero. please try again")
