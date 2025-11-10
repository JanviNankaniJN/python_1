#Write programs to demonstrate the use of Positional
#Argument, keyword argument , default arguments , variable
#length arguments

#positional argument
def add(a,b):
    print("positional argument:",a+b)
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
add(a,b)

#keyword argument
def show(x,y,name):
    print("keyword argument:",x,y,name)
show(x=a,y=b,name="janvi")

#default argument
def item(a,b,c=0):
    print("default argument:",a,b,c)

item(a,b,c=12)

#variable length argumenet
def var(*args):
    print("variable length argument:",args)

var(a,b)