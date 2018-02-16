a=['null','b','d','c','a','e']
b=['null','','','','','']
n=1

def conversion(con_input):

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

    if con_input==1:
        result='a'
        
    if con_input==2:
        result='b'

    if con_input==3:
        result='c'

    if con_input==4:
        result='d'

    if con_input==5:
        result='e'
        
    if con_input==6:
        result='f'

    if con_input==7:
        result='g'

    if con_input==8:
        result='h'

    if con_input==9:
        result='i'
        
    if con_input==10:
        result='j'

    if con_input==11:
        result='k'

    if con_input==12:
        result='l'

    if con_input==13:
        result='m'
        
    if con_input==14:
        result='n'

    if con_input==15:
        result='o'

    if con_input==16:
        result='p'

    if con_input==17:
        result='q'
        
    if con_input==18:
        result='r'

    if con_input==19:
        result='s'

    if con_input==20:
        result='t'
        
    return result

while n<=5:
    g=conversion(con_input=n)
    z=a[n]
    u=conversion(con_input=z)
    b[u]=g
    n+=1

print b
    
    
