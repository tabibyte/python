# variable for sum of all numbers that divided by 3 and 5
sum = 0

# variable for numbers that would be checked
i = 3

# checks all numbers from 3 to 1000 whether if the number is able to be divided by 3 and 5, then sums it
while i<1000:
    if i%3==0 or i%5==0:
        sum=sum+i
    i=i+1

# prints the answer
print(sum)