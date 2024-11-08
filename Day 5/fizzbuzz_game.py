for number in range(1, 101):  # Loop through numbers from 1 to 100
    if number % 3 == 0 and number % 5 == 0:  # Divisible by both 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:  # Divisible by 3
        print("Fizz")
    elif number % 5 == 0:  # Divisible by 5
        print("Buzz")
    else:  # Not divisible by 3 or 5
        print(number)