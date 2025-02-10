def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

user_input = int(input("Enter a number: "))
result = sum_of_digits(user_input)
print("The sum of the digits is:", result)