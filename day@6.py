def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Call the reverse_number function and print the result
print("Reversed number:", reverse_number(num))






