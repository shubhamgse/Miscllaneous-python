print('enter your string to check palindrome')
name=input()
print('Entered string is ' + name)

#lenght of the string
length  = len(name)
x = ""


#Reverse the string
while(length > 0):
  x += name[length-1]
  length = length - 1


#Check if reversed string and the given string are equal
if( x == name):
  print("String is Palindrome")
else:
  print("Not a Palindrome")