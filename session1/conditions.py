name1 = "aravinth"
name2 = "rakesh"
num1 = int(input('Enter first number: '))
num2 = int(input('Enter 2nd number: '))


# writing a function to determine largest of two numbers
def find_largest(n1, n2):
    bool12 = True if n1 > n2 else False
    return bool12


bool1 = find_largest(num1, num2)
if bool1:
    print("{} greater than {}".format(num1, num2))
else:
    print("{} greater than {}".format(num2, num1))

var1 = 1+2j
if type(var1) == int:
    print("variable is an integer")
elif type(var1) == float:
    print("var1 is a float")
else:
    print("variable type unknown")

age = 61
if age >= 11:
    print("You are eligible to see the Football match.")
    if age <= 20 or age >= 60:
        print("Ticket price is $12")
    else:
        print("Ticekit price is $20")
else:
    print("You're not eligible to buy a ticket.")

# create two boolean objects
x = True
y = True
print(type(x))
# The validation will be True only if all the expressions generate a value True
if x and y:
    print('Both x and y are True')
else:
    print('x is False or y is False or both x and y are False')


#create a integer
n = 150
print(n)
#if n is greater than 500, n is multiplied by 7, otherwise n is divided by 7
result = n * 7 if n > 500 else n / 7
print(result)
