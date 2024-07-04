#declaring a string
a=" Summer time sadness "
print(a)

#To access sting element by index number
print(a[0])

#to print every element in a string  using for loop
for x in "banana":
    print(x)

#to print length of the string
print(len(a))

#To check a word in a string, if available it returns yes 
print("free" in a)

#slicing operations
#slice from the start
print(a[:2])
#Slice To the End
print(a[2:])
#slicing in between strings
print(a[2:5])
#slicing with negative numbers
print(a[-5:-2])

#built in methods for string
print(a.upper())
print(a.lower())
print(a.strip())
#Replace 
print(a.replace("S", "J"))

