d={"Name":["hepzi","Beulah","Ann"],
"Age":[21,21,19]}
print(d)

#update
d.update({"cities":["cbe","cbe","nagercoil"]})
print(d)

#popItem
d.popitem()
print(d)

#pop
d.pop("Age")
print(d)

D1={"cities":["cbe","nagercoil","tirunelveli"],
"temperature":[20,30,40]}

#to get keys
print(D1.keys())

#to get values
print(D1.values())

#to print dict items with values and pair
print(D1.items())

#get method 
print(D1.get("age"))

#To copy a dict
D3=D1.copy()
print(D3)

#To clear a dict
D3.clear()
print(D3)

#setdefault
x={"key1":[1,2,3]}
y={"key2":"abba"}
z=x.setdefault("key2","mustang")
print(z)
print






