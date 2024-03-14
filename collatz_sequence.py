# Emulate Collatz Sequence
def collatz(number):
    # Check if it's a number
    try:
        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1
    except TypeError:
        print("Must enter an integer")


while True:
    number = input("Enter number: ")
    if number.isnumeric() == False:
        print("Must enter an positive integer")
        continue
    else:
        number= int(number)
        while number !=1:
            result = collatz(number)
            print(result)
            number = result
        break




