while True:
    n = int(input())
    if n == -1:
        break
    
    fac = []
    for i in range(1,n):
        if not n % i:
            fac.append(i)
    
    if sum(fac) == n:
        print(n, " = ", " + ".join(str(i) for i in fac), sep="")
    else:
        print(n,'is NOT perfect.')