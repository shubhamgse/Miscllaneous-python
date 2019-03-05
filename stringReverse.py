print('enter your string')
name=input()
print('Entered string is   ' + name)

length  = len(name)
x = ""

while(length > 0):
  x += name[length-1]
  length = length - 1


print("Reverse of string is ",x)