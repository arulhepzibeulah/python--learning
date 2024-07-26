import os


dirs = os.listdir('E:\\docs')

text_files=[]

for file in dirs:
    if file.endswith(".txt"):
       text_files.append(file)

print(text_files)
print(len(text_files))
