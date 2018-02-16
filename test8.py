def clockwiserotate (stepper, string):
  n=stepper
  v=1
  k=1
  a=string
  b=a

  while v<=n:
    b.append(a[v])
    v+=1
  print b
  for k in range(1,n,+1):
    del b[k]
    k=k+1


  print b


a=['null','a','b','c','d','e']

b=clockwiserotate(stepper=2, string=a)

print b
