one = 1
two = 2

hello = "Hello, World"

output = one.__str__() + two.__str__() + hello

print(output)

mylist = [1, 2]
print(mylist[0])
print(mylist[1])
mylist.append(3)
print(mylist[2])

# prints out 1,2,3
for x in mylist:
    print(x)

print("length of hello is: %d" % len(hello))
print(hello.upper())
tokens = hello.split(" ")
print(tokens)

# ------------conditions---------
a = 1
b = 2
print(a == 2)
if a == 1 and b == 2:
    print("everything is all set!")

nameArray = ["Johm", "Jane", "Jill"]
str = nameArray[2]
if "Ali" in nameArray:
    print("it exists")
elif str in nameArray:
    print("another yes")
else:
    print("it does not exist!")

if isinstance(a, int):
    print("it is integer")

for name in nameArray:
    print(name)

if 2 in range(1, 5):
    print("2 is in range 5")

# -----------------------------

i = 0
while i <= 20:
    i += 1

    if i % 2 != 0:
        print(i)

    if i >= 10:
        break

# -------------------------------

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % count)

# Prints out 1,2,3,4
for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


#--------------------------------------------
