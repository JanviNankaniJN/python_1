#Write a python program that removes any repeated items
#from a list so that each item appears at most once. For
#instance, the list [1,1,2,3,4,3,0,0] would become
#[1,2,3,4,0].

lst=[1,1,2,3,4,3,0,0]
new_list = []
for i in lst:
    if i not in new_list:     # duplicates skip
        new_list.append(i)

print(new_list)