while True:
    try:
        first=float(input("Enter the first number: "))
        second=float(input("Enter the second number: "))
        third=float(input("Enter the third number: "))
    except ValueError:
        print("\nEnter a valid number\n")
    else:
        total=first+second+third
        average=total/3
        print("The total is ",total)
        print("The average is ",average)
        break