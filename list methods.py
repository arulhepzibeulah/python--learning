#insert method
l = ['a','b','c','a']
l.insert(1,'d')
print(l)

#append method which is used to append only one element in the list
l.append(1)
print(l)

#extend method id used to add more elements in the list
l.extend([3,4,5])
print(l)

#pops out the element in the given index
l.pop(3)
print(l)

#removes element from the list , it just deletes the first occurence of list
l.remove('a')
print(l)

#prints the count of the given element
print(l.count('a'))

#prints the index of the given element
print(l.index('a'))

#sorts
l2=[1,4,5,6,8,11,99,300]
l2.sort()
print(l2)

#To reverse sorting
l2.sort(reverse=True)
print(l2)

#To copy a list to another list
list1 = l.copy()
print(list1)

#To clear the list
l2.clear()
print(l2)


l3=["hepzi","jaya"]
l3.append(["nilesh","jithin"])
print(l3)

l3.extend(["daniel","Shivani"])
print(l3)
t1=(1,2,3,4,5)
print(t1)

l4=[10,10,19,10]

print(l4.count(10))

