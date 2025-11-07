#Write a menu driven python program which perform the following:
#Find area of circle
#Find area of triangle 
#Find area of square and rectangle
#Find Simple Interest Exit.( Hint: Use infinite while loop for Menu)
while True:
    print("\n------ MENU ------")
    print("1. Area of Circle")
    print("2. Area of Triangle")
    print("3. Area of Square and Rectangle")
    print("4. Simple Interest")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        r = float(input("Enter radius: "))
        area = 3.14 * r * r
        print("Area of Circle =", area)

    elif choice == 2:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        area = 0.5 * b * h
        print("Area of Triangle =", area)

    elif choice == 3:
        print("1. Square")
        print("2. Rectangle")
        ch = int(input("Enter 1 or 2: "))

        if ch == 1:
            side = float(input("Enter side: "))
            area = side * side
            print("Area of Square =", area)
        else:
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            area = l * w
            print("Area of Rectangle =", area)

    elif choice == 4:
        p = float(input("Enter Principal: "))
        r = float(input("Enter Rate: "))
        t = float(input("Enter Time: "))
        si = (p * r * t) / 100
        print("Simple Interest =", si)

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")