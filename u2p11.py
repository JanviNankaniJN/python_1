#Write a program to create a list using range functions and
#perform append, update and delete elements operations
#in it.
num=list(range(1,11))
print("original list=",num)

num.append(50)
print("append list=",num)

num[2]=100
print("update list=",num)

del num[5]
print("delete list=",num)