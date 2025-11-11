x=lambda a : a + 10
print(x(5))

x=lambda a,b:a*b
print(x(5,6))

x=lambda a,b,c:a+b+c
print(x(5,6,2))

def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(2)

print(mydoubler(11))

def myfunc(n):
    return lambda a:a*n

mytriple=myfunc(3)

print(mytriple(11))

def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(2)
mytriple=myfunc(3)

print(mytriple(11))
print(mydoubler(11))

#functions 

#map()
num=[1,2,3,4,5,6]
doubled=list(map(lambda x:x*2,num))
print(doubled)

#filter
num=[1,2,3,4,5,6,7,8,9]
on=list(filter(lambda x: x % 2 != 0,num))
print(on)

#sorted
stu=[("Email",25),("Tobias",22),("Linus",28)]
s1=sorted(stu,key=lambda x: x[1])
print(s1)

word=["apple","pie","banana","cherry"]
sw=sorted(word,key=lambda x: len(x))
print(sw)