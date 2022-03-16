# finding biggest palindrome
number = 999
palindromebig = 0
# checks all first and second three digit multipliers
while number > 99:
    for i in range(99,999):
        # checks if palindrome
        palindrome = number*i
        tostring = str(palindrome)
        reverse = int(tostring[::-1])
        if palindrome == reverse:
            if palindrome > palindromebig:
                palindromebig = palindrome
    number=number-1
print(palindromebig)
