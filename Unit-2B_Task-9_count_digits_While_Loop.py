#TO Count Digits using while loop
number = int(input("Enter a number: "))
original_number = number
digit_count = 0

if number == 0:
    digit_count = 1
else:
    while ____:  # continue while number still has digits
        digit_count = ____  # increase the count by 1
        number = ____  # remove the last digit with // 10

print(f"Number of digits in {original_number} is {digit_count}")