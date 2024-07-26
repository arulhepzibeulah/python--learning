try:
    file = open("example.txt", "r")
    for each in file:
        print(each)
    file.close()

except FileNotFoundError: 
    
    file = open("example.txt", "w")
    file.write("Hi there, it's about exception handling")
    file.close()

    
    file = open("example.txt", "r")
    for each in file:
        print(each)
    file.close()
