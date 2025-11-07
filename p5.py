#Write a program to find out and display the common and the non common elements in the list using membership operators
list1=[1,2,3,4]
list2=[5,4,2,6]
common=[]
for i in list1:
    if i in list2:
        common.append(i)

noncommon=[]
for i in list1:
    if i not in list2:
        noncommon.append(i)

for j in list2:
    if j not in list1:
        noncommon.append(j)

print("list1=",list1)
print("list2=",list2)
print("common elements=",common)
print("noncommon elements=",noncommon)