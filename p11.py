#Write a program to search an element in the list using for loop
#and also demonstrate the use of “else” with for loop.
lst = [10, 20, 30, 40, 50]

x = int(input("Enter element to search: "))

for i in lst:
    if i == x:
        print("Element found")
        break
else:
    print("Element not found")