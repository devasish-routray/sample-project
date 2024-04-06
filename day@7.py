def check_even_odd_4digit(num):
    if num >= 1000 and num <= 9999:
        if num % 2 == 0:
            return "Even 4-digit number"
        else:
            return "Odd 4-digit number"
    else:
        return "Not a 4-digit number"

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Call the check_even_odd_4digit function and print the result
print(check_even_odd_4digit(num))