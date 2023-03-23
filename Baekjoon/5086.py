
while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    if a < b:
        
        fac = []
        for i in range(1,b+1):
            if not b % i:
                fac.append(i)
            if a in fac:
                print('factor')
                break
        
        if a not in fac:
            print('neither')
    elif a > b:
        
        if not a % b:
            print('multiple')
        
        else:
            print('neither')