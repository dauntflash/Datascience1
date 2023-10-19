while True:
    try:
        price=float(input("Enter the price: "))
        tip_percent=float(input("Enter the percentage of the tip: "))
    except ValueError:
        print("\nInvalid input. Try again\n")
    else:
        if price >0 and tip_percent >0:
            tip=(tip_percent/100)*price
            total=tip+price
            print("The price was ksh. ",price, ", the tip is of ksh.",tip)
            print("The total bill is ksh. ",total)
            break
        else:
            print("\nEnter a positive value\n")