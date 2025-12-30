# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close() 

# file = open("file/example.txt", "r")
# content = file.readlines()
# print(content)
# file.close()

file = open("file/example.txt", "r")
content = file.readlines()
for line in content:
    print(line[2])
file.close()