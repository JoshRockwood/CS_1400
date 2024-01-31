def ask_for_input():
    number = input("Please enter a number: ")
    if int(number) % 2 == 0:
        print(str(number) + " is an even number.")
    else:
        print(str(number) + " is an odd number.")


ask_for_input()
