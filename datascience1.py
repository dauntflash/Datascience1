while True:
    try:
        kilogram=float(input("Enter the mass in kg: "))
    except ValueError:
        print("Invalid input. Enter a valid number\n")
    else:
        if kilogram <0:
            print("Enter a positive number\n")
        else:
            pounds=kilogram*2.2
            print("The mass in pounds is ",pounds)
            break