#Write a program to create a byte type array, read, modify, and display the elements of the array
data = bytearray([10,20,30,40,50])

print("original array :")
for value in data:
    print(value,end=" ")

print("\nmodify array :")
for i in range(len(data)):
    data[i]=data[i]+5

for value in data:
    print(value,end=" ")

index = int(input("\n Enter value of index (0-4) :"))
print("\n Value at index ",index,"is:",data[index])