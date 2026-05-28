try:
    numbers = list(map(float, input("Enter numbers seperated by space: ").split()))
    for number in numbers:
        if number % 2 == 0:
            print("Even")
        else:
            print("odd")
except ValueError:
    print("Invalid input! Please enter a valid real number.")

