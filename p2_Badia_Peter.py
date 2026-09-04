def find_pythagorean(n) :
    c = n**2
    if n > 0 :
        for a in range (1, n+1) :
            for b in range(1, n+1) :
                if c == a**2 + b**2 :
                    return((a,b,n))


n = int(input('Enter a positive number to find a triple: '))
triples = find_pythagorean(n)
print(triples)