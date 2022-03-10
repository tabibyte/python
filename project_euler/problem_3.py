quotient=600851475143
primefactor=2

while quotient != 1:
    primefactor = primefactor + 1
    while quotient % primefactor == 0 :
        quotient = quotient / primefactor
print(primefactor)
