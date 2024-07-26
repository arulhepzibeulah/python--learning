

mark  = float(input("Enter your mark :"))
print(type(mark))
if mark >= 35 :
    print("You're passed")
else:
    print("You're failed")
    
    #Traffic signal
light=input("Enter the signal color ")
if light=="red" :
        print("Stop") 
elif light=="yellow":
        print("wait")
elif light=="green":
        print("Go")
else:
        print("You have entered wrong color signal")

#check whether string starts with a
str=input('Enter a string')
if str.startswith("a" or "A"):
    print("Your your string starts with a" )
else:
    print("Your string does nt starts with 'A'")

#To check whether its a positive number or negative or zero
num=int(input("Enter a number"))
if num > 0:
    print("Its a positive number")
elif num<0:
    print("Its a negative number")
elif num==0:
    print("It is zero")

#To check whether its odd or even
num1=int(input("Enter a number"))
if num1 % 2==0:
    print("Its even")
else:
    print("Its odd")

#To check voting elgibility
age=int(input("Enter your age "))
if age>=18 and age<=120:
    print("Your eligible for voting")
else:
    print("Your not eligible for voting")









