# variable initialization
name = "aravinth"
number = 10

# printing variables and variations in print statement
print("name = ", name)

print(number)

print("name =" + name + " and number = ", number)

print("name = {n} , number = {n1}".format(n=name, n1=number))

print("name = %s and number = %d " % (name, number))

print("name = %s, number = %d ", name, number)

print("number = %d " % 45)

# print("name = %s, number = %d " % 'rakesh' % 45)

print("Welcome to %%Python %s" % 'language')

# to write print in multiple lines
print("""this is a paragraph example\n 
        for print statement""")
print("this is a paragraph example"
      " for print statement")

# for printing in next line
print("Sunday\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday")

# for giving tabbing in same line
print("Sunday\tMonday\tTuesday\tWednesday\tThursday\tFriday\tSaturday")

# validating and printing boolean
print(bool("hello"))
print(bool(15))
print(bool(name))

# ordered, data changable. duplicate members allowed
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1:9])
#print(thislist[num1:num2]) output count = num2-num1


# ordered. not changable. duplicate allowed
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#unordered. unindexed. duplicate not allowed
thisset = {"apple", "banana", "cherry"}
print(thisset)

#unordered, changeable. data indexed. no duplicates
thisdict = {
  "brand": "Ford",
  "model": "mustang",
  "year": 1964
}
print(thisdict)

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
thislist.append("blackcurrent")
print(thislist)
