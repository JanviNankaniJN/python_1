#Write a program to create nested list and display its elements.
nested_list = [
    [10, 20, 30],
    ["Apple", "Banana", "Mango"],
    [True, False, True]
]

# printing nested list
print("Nested List:", nested_list)

print("\nDisplaying elements:")
for sub_list in nested_list:        # outer list
    for item in sub_list:           # inner list
        print(item, end=" ")
