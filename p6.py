#Create a program to display memory locations of two variables using id() function,
#and then use identity operators two compare whether two objects are same or not.
a=10
b=20
print("id of a variable:",id(a))
print("id of b variable:",id(b))

print(a is b)
print(a is not b)