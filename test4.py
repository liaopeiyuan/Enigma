def  calc_output (start, string, bkup):
        
        b=bkup
        print b
        a=string
        ind=start
        n=a.index(ind)
        i=1
        v=1

        while v<n:
            d=b[v]
            a.append(d)
            v+=1
        while i<n:
            i += 1
            a.pop(1)

            

        return a


a=['a','b','c','d','e','f']

b=calc_output(start='f',string=a,bkup=a)

print b
