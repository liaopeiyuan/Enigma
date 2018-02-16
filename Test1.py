def let_to_num (input):

        result=0

        if input=='a':
            result=1

        elif input=='b':
            result=2
    
        elif input=='c':
            result=3
    
        elif input=='d':
            result=4
    
        return result

while True:
    
    rotors=['b','c','d','e']
    
    init=raw_input()

    we=let_to_num(input=init)-1

    print rotors[we]
