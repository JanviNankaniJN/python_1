#Write a program to accept elements in the form of a tuple and
#display its minimum, maximum, sum and average.
elements=input("enter numbers separated by spaces:")
numbers=tuple(map(int,elements.split()))
minimum=min(numbers)
maximum=max(numbers)
total=sum(numbers)
average=total/len(numbers)
print("tuple elements=",numbers)
print("minimum=",minimum)
print("maximum=",maximum)
print("sum=",total)
print("average=",average)