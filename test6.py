def calc_inverse (string):
    a=string
    b=['null','','','','','','','','','','','','','','','','','','','','','','','','','','']
    n=1
    while n<=26:
        con_input=a[n]
        coninput=n
        
        if con_input=='a':
          result=1

        if con_input=='b':
          result=2

        if con_input=='c':
            result=3

        if con_input=='d':
            result=4

        if con_input=='e':
            result=5

        if con_input=='f':
            result=6

        if con_input=='g':
            result=7

        if con_input=='h':
            result=8

        if con_input=='i':
            result=9

        if con_input=='j':
            result=10

        if con_input=='k':
            result=11

        if con_input=='l':
            result=12

        if con_input=='m':
            result=13

        if con_input=='n':
          result=14

        if con_input=='o':
            result=15

        if con_input=='p':
            result=16

        if con_input=='q':
            result=17

        if con_input=='r':
            result=18

        if con_input=='s':
            result=19

        if con_input=='t':
           result=20

        if con_input=='u':
           result=21

        if con_input=='v':
           result=22

        if con_input=='w':
            result=23

        if con_input=='x':
            result=24

        if con_input=='y':
            result=25

        if con_input=='z':
            result=26

        if coninput==1:
            result1='a'
        
        if coninput==2:
            result1='b'

        if coninput==3:
            result1='c'

        if coninput==4:
           result1='d'

        if coninput==5:
            result1='e'
        
        if coninput==6:
            result1='f'

        if coninput==7:
            result1='g'

        if coninput==8:
            result1='h'

        if coninput==9:
            result1='i'
        
        if coninput==10:
            result1='j'

        if coninput==11:
           result1='k'

        if coninput==12:
            result1='l'

        if coninput==13:
            result1='m'
        
        if coninput==14:
            result1='n'

        if coninput==15:
            result1='o'

        if coninput==16:
            result1='p'

        if coninput==17:
            result1='q'
        
        if coninput==18:
           result1='r'

        if coninput==19:
            result1='s'

        if coninput==20:
            result1='t'

        if coninput==21:
            result1='u'
        
        if coninput==22:
           result1='v'

        if coninput==23:
           result1='w'

        if coninput==24:
           result1='x'
        
        if coninput==25:
            result1='y'
        
        if coninput==26:
            result1='z'
        
        b[result]=result1
        n+=1

    return b

a=['null','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

b=calc_inverse(string=a)

print b
