a = 0
while a < 1 or a > 7:
    a = int(input("Please Enter a number between 1 to 7: "))
    if a < 1 or a > 7:
        print("Please enter a valid number between 1 to 7.")
    else:
        if a == 1:
            print("Monday")
        elif a == 2:
            print("Tuesday")
        elif a == 3:
            print("Wednesday")
        elif a == 4:
            print("Thursday")
        elif a == 5:
            print("Friday")
        elif a == 6:
            print("Saturday")
        elif a == 7:
            print("Sunday")