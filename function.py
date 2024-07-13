# calling a function
def my_function():
    txt="Let it go"
    print(txt)
my_function()

#function with argument
def function2(name):
    print(f"My name is {name}")
function2("hepzi")
function2("beulah")

#function when arguments are not known
def function3(*name):
    x="my name is"+name[2]
    print(x)
function3("emil","tobias","Linus")

#python built in function
val1=abs(-7.25)
print(val)

val2 = abs(3+5j)
print(val1)


