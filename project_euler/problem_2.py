# variable for sum of even numbers
sum = 0

# first,second and temporary fibonacci value to temporarily save both fibonacci numbers
fib1 = 1
fib2 = 1
temp = 0

# sums changes tha values and repeats until the value exceeds 4000000
while temp<=4000000:
    temp = fib1 + fib2
    fib2 = fib1
    fib1 = temp
    # checks whether if number is even then adds to the sum
    if temp%2==0:
        sum=sum+temp
print(sum)
