# finding biggest palindrome
number = 999
palindromebig = 0
while number > 99:
    for i in range(99,999):
        palindrome = number*i
        tostring = str(palindrome)
        reverse = int(tostring[::-1])
        if palindrome == reverse:
            if palindrome > palindromebig:
                palindromebig = palindrome
    number=number-1
print(palindromebig)
