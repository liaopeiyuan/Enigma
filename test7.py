a=['null','a','b','c','d','e']

b=['null','a','b','c','d','e']

n=1
v=1

while n<=v:
    del b[v]
    b.append(a[v])
    n+=1

print b
print a
    
