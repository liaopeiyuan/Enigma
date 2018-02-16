while True:
    
    a=['null','a','b','c','d']
    b=['null','a','b','c','d']

    h=input()
    n= h % 4
    if n==0:
        n=4
    i=1
    v=1

    while i<n:
        i += 1
        a.pop(1)

    while v<n:
        d=b[v]
        v+=1
        a.append(d)

    print a
