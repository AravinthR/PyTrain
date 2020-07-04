count = int(input("Enter the count of fibonacci number expected: "))
a = 0
b = 1
if count == 0:
    print("NULL")
elif count == 1:
    print("0")
elif count == 2:
    print("0,1")
elif count > 2:
    print("0,1, ")
    for i in range(2, count):
        c = a + b
        a = b
        b = c
        print(",", c)

