class Plugboard (object):
    
  def __init__ (plug,letter1='',letter2=''):

    plug.letter1=plug.set_letter1() #The First letter in the plugboard cable.
    plug.letter2=plug.set_letter2() #The Second letter in the plugboard cable.
    plug.output=''                  #When a letter is imported into the plugboard, no matter it's changed or not, the output will be stored in this variable.

        
  def set_letter1 (plug):

    while True:

      raw_letter1=raw_input('1st letter in the cable:  ') #Inform the user to indicate the letter.
      raw2_letter1=raw_letter1.strip()
      letter1=raw2_letter1.lower()

      try:
        test_1=ord(letter1)
        return letter1
        break

      except:
        print('info invalid')

  def set_letter2 (plug):

    while True:

      raw_letter2=raw_input('2nd letter in the cable:  ') #Inform the user to indicate the letter.
      raw2_letter2=raw_letter2.strip()
      letter2=raw2_letter2.lower()

      try:
        test_2=ord(letter2)
        return letter2
        break

      except:
        print('info invalid')


class Rotor (object):
    
  def __init__ (rotor,ini_pos='',ascii_dif='',output=''):

    rotor.ini_pos=rotor.set_inipos() #The letter to which the letter 'a' is wired.
    rotor.ascii_dif=rotor.set_asciidif() #The mathematical difference between the rela_pos's ASCII number and 97(a)
    rotor.output=output
    rotor.raw=rotor.ascii_dif

  def set_inipos (rotor):

    while True:

      raw_letter1=raw_input('Initial position of the rotor["b" means "a" is wired to "b"]  ')
      raw2_letter1=raw_letter1.strip()
      letter1=raw2_letter1.lower()

      if letter1=='a':
        print "rotor idle"
        ini_pos=letter1
        return ini_pos
        break

      else:
          
        try:
          test_1=ord(letter1)
          ascii_dif=test_1-97

          if ascii_dif<0:
            print ('info invalid')

          elif ascii_dif>26:
            print ('info invalid')

          else:
            ini_pos=letter1
            print 'Substitutional difference',ascii_dif
            return ini_pos
            break

        except:
          print('info invalid')
                      
  def set_asciidif(rotor):

    process=ord(rotor.ini_pos)
    ascii_dif=int(process-97)
    return ascii_dif

  def raw(rotor):

    raw=rotor.ascii_dif
    return raw
              

def interchange (let,letter1,letter2): #The function that can determine whether the letter needs to be changed in the PLUGBOARD.

  if let==letter1:
    out=letter2
    return out

  elif let==letter2:
    out=letter1
    return out

  else:
    out=let
    return out

        
def comparison (let,ascii): #The function that makes the Ceasar Shift.

  comp1=ord(let)
  proc3=ascii
  test_2=comp1+proc3

  if test_2>122:
    test_2=96-(122-comp1-proc3)


  elif test_2<97:
    test_2=123-(97-comp1-proc3)


  return chr(test_2)


def vector(): #The function that informs the user to input the ring settings.

  while True:

    vec=raw_input('Ring settings: ')
    try:

      vector=int(vec)

      if vector<0:
        print('info invalid')

      elif vector>26:
        print('info invalid')

      else:
        return vector
        break
    
    except:
          print('info invalid')


def rotorI(let): #Historical settings of the rotor in the Enigma machine.

    a=let
    if a=='a':
        a='e'
    elif a=='b':
        a='k'
    elif a=='c':
        a='m'
    elif a=='d':
        a='f'
    elif a=='e':
        a='l'
    elif a=='f':
        a='g'
    elif a=='g':
        a='d'
    elif a=='h':
        a='q'
    elif a=='i':
        a='v'
    elif a=='j':
        a='z'
    elif a=='k':
        a='n'
    elif a=='l':
        a='t'
    elif a=='m':
        a='o'
    elif a=='n':
        a='w'
    elif a=='o':
        a='y'
    elif a=='p':
        a='h'
    elif a=='q':
        a='x'
    elif a=='r':
        a='u'
    elif a=='s':
        a='s'
    elif a=='t':
        a='p'
    elif a=='u':
        a='a'
    elif a=='v':
        a='i'
    elif a=='w':
        a='b'
    elif a=='x':
        a='r'
    elif a=='y':
        a='c'
    elif a=='z':
        a='j'
    return a


def IVrotorI(let): #Historical settings of the rotor in the Enigma machine in a reversed manner.

    a=let
    if a=='e':
        a='a'
    elif a=='k':
        a='b'
    elif a=='m':
        a='c'
    elif a=='f':
        a='d'
    elif a=='l':
        a='e'
    elif a=='g':
        a='f'
    elif a=='d':
        a='g'
    elif a=='q':
        a='h'
    elif a=='v':
        a='i'
    elif a=='z':
        a='j'
    elif a=='n':
        a='k'
    elif a=='t':
        a='l'
    elif a=='o':
        a='m'
    elif a=='w':
        a='n'
    elif a=='y':
        a='o'
    elif a=='h':
        a='p'
    elif a=='x':
        a='q'
    elif a=='u':
        a='r'
    elif a=='s':
        a='s'
    elif a=='p':
        a='t'
    elif a=='a':
        a='u'
    elif a=='i':
        a='v'
    elif a=='b':
        a='w'
    elif a=='r':
        a='x'
    elif a=='c':
        a='y'
    elif a=='j':
        a='z'
    return a


def rotorII(let): #Historical settings of the rotor the in Enigma machine.

    a=let
    if a=='a':
        a='a'
    elif a=='b':
        a='j'
    elif a=='c':
        a='d'
    elif a=='d':
        a='k'
    elif a=='e':
        a='s'
    elif a=='f':
        a='i'
    elif a=='g':
        a='r'
    elif a=='h':
        a='u'
    elif a=='i':
        a='x'
    elif a=='j':
        a='b'
    elif a=='k':
        a='l'
    elif a=='l':
        a='h'
    elif a=='m':
        a='w'
    elif a=='n':
        a='t'
    elif a=='o':
        a='m'
    elif a=='p':
        a='c'
    elif a=='q':
        a='q'
    elif a=='r':
        a='g'
    elif a=='s':
        a='z'
    elif a=='t':
        a='n'
    elif a=='u':
        a='p'
    elif a=='v':
        a='y'
    elif a=='w':
        a='f'
    elif a=='x':
        a='v'
    elif a=='y':
        a='o'
    elif a=='z':
        a='e'
    return a


def IVrotorII(let): #Historical settings of the rotor in the Enigma machine in a reversed manner.

    a=let
    if a=='a':
        a='a'
    elif a=='j':
        a='b'
    elif a=='d':
        a='c'
    elif a=='k':
        a='d'
    elif a=='s':
        a='e'
    elif a=='i':
        a='f'
    elif a=='r':
        a='g'
    elif a=='u':
        a='h'
    elif a=='x':
        a='i'
    elif a=='b':
        a='j'
    elif a=='l':
        a='k'
    elif a=='h':
        a='l'
    elif a=='w':
        a='m'
    elif a=='t':
        a='n'
    elif a=='m':
        a='o'
    elif a=='c':
        a='p'
    elif a=='q':
        a='q'
    elif a=='g':
        a='r'
    elif a=='z':
        a='s'
    elif a=='n':
        a='t'
    elif a=='p':
        a='u'
    elif a=='y':
        a='v'
    elif a=='f':
        a='w'
    elif a=='v':
        a='x'
    elif a=='o':
        a='y'
    elif a=='e':
        a='z'
    return a


def rotorIII(let): #Historical settings of the rotor in the Enigma machine.

    a=let
    if a=='a':
        a='b'
    elif a=='b':
        a='d'
    elif a=='c':
        a='f'
    elif a=='d':
        a='h'
    elif a=='e':
        a='j'
    elif a=='f':
        a='l'
    elif a=='g':
        a='c'
    elif a=='h':
        a='p'
    elif a=='i':
        a='r'
    elif a=='j':
        a='t'
    elif a=='k':
        a='x'
    elif a=='l':
        a='v'
    elif a=='m':
        a='z'
    elif a=='n':
        a='n'
    elif a=='o':
        a='y'
    elif a=='p':
        a='e'
    elif a=='q':
        a='i'
    elif a=='r':
        a='w'
    elif a=='s':
        a='g'
    elif a=='t':
        a='a'
    elif a=='u':
        a='k'
    elif a=='v':
        a='m'
    elif a=='w':
        a='u'
    elif a=='x':
        a='s'
    elif a=='y':
        a='q'
    elif a=='z':
        a='o'
    return a


def IVrotorIII(let): #Historical settings of the rotor in the Enigma machine in a reversed manner.

    a=let
    if a=='b':
        a='a'
    elif a=='d':
        a='b'
    elif a=='f':
        a='c'
    elif a=='h':
        a='d'
    elif a=='j':
        a='e'
    elif a=='l':
        a='f'
    elif a=='c':
        a='g'
    elif a=='p':
        a='h'
    elif a=='r':
        a='i'
    elif a=='t':
        a='j'
    elif a=='x':
        a='k'
    elif a=='v':
        a='l'
    elif a=='z':
        a='m'
    elif a=='n':
        a='n'
    elif a=='y':
        a='o'
    elif a=='e':
        a='p'
    elif a=='i':
        a='q'
    elif a=='w':
        a='r'
    elif a=='g':
        a='s'
    elif a=='a':
        a='t'
    elif a=='k':
        a='u'
    elif a=='m':
        a='v'
    elif a=='u':
        a='w'
    elif a=='s':
        a='x'
    elif a=='q':
        a='y'
    elif a=='o':
        a='z'
    return a


def rotorIV(let): #Historical settings of the rotor in the Enigma machine.

    a=let
    if a=='a':
        a='e'
    elif a=='b':
        a='s'
    elif a=='c':
        a='o'
    elif a=='d':
        a='v'
    elif a=='e':
        a='p'
    elif a=='f':
        a='z'
    elif a=='g':
        a='j'
    elif a=='h':
        a='a'
    elif a=='i':
        a='y'
    elif a=='j':
        a='q'
    elif a=='k':
        a='u'
    elif a=='l':
        a='i'
    elif a=='m':
        a='r'
    elif a=='n':
        a='h'
    elif a=='o':
        a='x'
    elif a=='p':
        a='l'
    elif a=='q':
        a='n'
    elif a=='r':
        a='f'
    elif a=='s':
        a='t'
    elif a=='t':
        a='g'
    elif a=='u':
        a='k'
    elif a=='v':
        a='d'
    elif a=='w':
        a='c'
    elif a=='x':
        a='m'
    elif a=='y':
        a='w'
    elif a=='z':
        a='b'
    return a


def IVrotorIV(let): #Historical settings of the rotor in the Enigma machine in a reversed manner.

    a=let
    if a=='e':
        a='a'
    elif a=='s':
        a='b'
    elif a=='o':
        a='c'
    elif a=='v':
        a='d'
    elif a=='p':
        a='e'
    elif a=='z':
        a='f'
    elif a=='j':
        a='g'
    elif a=='a':
        a='h'
    elif a=='y':
        a='i'
    elif a=='q':
        a='j'
    elif a=='u':
        a='k'
    elif a=='i':
        a='l'
    elif a=='r':
        a='m'
    elif a=='h':
        a='n'
    elif a=='x':
        a='o'
    elif a=='l':
        a='p'
    elif a=='n':
        a='q'
    elif a=='f':
        a='r'
    elif a=='t':
        a='s'
    elif a=='g':
        a='t'
    elif a=='k':
        a='u'
    elif a=='d':
        a='v'
    elif a=='c':
        a='w'
    elif a=='m':
        a='x'
    elif a=='w':
        a='y'
    elif a=='v':
        a='z'
    return a


def rotorV(let): #Historical settings of the rotor in the Enigma machine.

    a=let
    if a=='a':
        a='v'
    elif a=='b':
        a='z'
    elif a=='c':
        a='b'
    elif a=='d':
        a='r'
    elif a=='e':
        a='g'
    elif a=='f':
        a='i'
    elif a=='g':
        a='t'
    elif a=='h':
        a='y'
    elif a=='i':
        a='u'
    elif a=='j':
        a='p'
    elif a=='k':
        a='s'
    elif a=='l':
        a='d'
    elif a=='m':
        a='n'
    elif a=='n':
        a='h'
    elif a=='o':
        a='l'
    elif a=='p':
        a='x'
    elif a=='q':
        a='q'
    elif a=='r':
        a='w'
    elif a=='s':
        a='m'
    elif a=='t':
        a='j'
    elif a=='u':
        a='q'
    elif a=='v':
        a='o'
    elif a=='w':
        a='f'
    elif a=='x':
        a='e'
    elif a=='y':
        a='c'
    elif a=='z':
        a='k'
    return a


def IVrotorV(let): #Historical settings of the rotor in the Enigma machine in a reversed manner.

    a=let
    if a=='v':
        a='a'
    elif a=='z':
        a='b'
    elif a=='b':
        a='c'
    elif a=='r':
        a='d'
    elif a=='g':
        a='e'
    elif a=='i':
        a='f'
    elif a=='t':
        a='g'
    elif a=='y':
        a='h'
    elif a=='u':
        a='i'
    elif a=='p':
        a='j'
    elif a=='s':
        a='k'
    elif a=='d':
        a='l'
    elif a=='n':
        a='m'
    elif a=='h':
        a='n'
    elif a=='l':
        a='o'
    elif a=='x':
        a='p'
    elif a=='q':
        a='q'
    elif a=='w':
        a='r'
    elif a=='m':
        a='s'
    elif a=='j':
        a='t'
    elif a=='q':
        a='u'
    elif a=='o':
        a='v'
    elif a=='f':
        a='w'
    elif a=='e':
        a='x'
    elif a=='c':
        a='y'
    elif a=='k':
        a='z'
    return a


def reflectorB(let): #Historical settings of the reflector in the Enigma machine.
    a=let
    if a=='a':
        a='y'
    elif a=='b':
        a='r'
    elif a=='c':
        a='u'
    elif a=='d':
        a='h'
    elif a=='e':
        a='q'
    elif a=='f':
        a='s'
    elif a=='g':
        a='l'
    elif a=='h':
        a='d'
    elif a=='i':
        a='p'
    elif a=='j':
        a='x'
    elif a=='k':
        a='n'
    elif a=='l':
        a='g'
    elif a=='m':
        a='o'
    elif a=='n':
        a='k'
    elif a=='o':
        a='m'
    elif a=='p':
        a='i'
    elif a=='q':
        a='e'
    elif a=='r':
        a='b'
    elif a=='s':
        a='f'
    elif a=='t':
        a='z'
    elif a=='u':
        a='c'
    elif a=='v':
        a='w'
    elif a=='w':
        a='v'
    elif a=='x':
        a='j'
    elif a=='y':
        a='a'
    elif a=='z':
        a='t'
    return a


def reflectorC(let): #Historical settings of the reflector in the Enigma machine.
    a=let
    if a=='a':
        a='f'
    elif a=='b':
        a='v'
    elif a=='c':
        a='p'
    elif a=='d':
        a='j'
    elif a=='e':
        a='i'
    elif a=='f':
        a='a'
    elif a=='g':
        a='o'
    elif a=='h':
        a='y'
    elif a=='i':
        a='e'
    elif a=='j':
        a='d'
    elif a=='k':
        a='r'
    elif a=='l':
        a='z'
    elif a=='m':
        a='x'
    elif a=='n':
        a='w'
    elif a=='o':
        a='g'
    elif a=='p':
        a='c'
    elif a=='q':
        a='t'
    elif a=='r':
        a='k'
    elif a=='s':
        a='u'
    elif a=='t':
        a='q'
    elif a=='u':
        a='s'
    elif a=='v':
        a='b'
    elif a=='w':
        a='n'
    elif a=='x':
        a='m'
    elif a=='y':
        a='h'
    elif a=='z':
        a='l'
    return a


def main():
    
 print ('Welcome, this is a computer version of the Wehrmacht Enigma I.')
 print ('This version is modified from Enigma G, and was used extensively by German military services and other government organizations before and during World War II.')
 print ('It contains THREE plugboard cables and THREE rotors.')
 print ('FIVE rotors and TWO FIXED reflectors.')
 print ('The info you need to enter is listed below.')
 print ('    ring settings')
 print ('   (relative position of alphabet ring to rotor disk)')
 print ('    initial position of the rotors')
 print ('    THREE rotors you wish to use in Roman numerals')
 print ('    ONE in TWO reflectors you wish to use')
 print ('             ')
 print ('The settings of rotors and reflectors are historical, which you can access by typing "set".')
 print ('To use the indicator to encrypt your initial positions, type in the indicators when the value of the initial position is requested.') 
 print ('Due to the limitation of codes, this program cannot fully simulate the reflexivity of the Enigma machine.')
 print ('You have to indicate the mode before you can enter the plaintext/ciphertext.')

 #This is the introduction of the program.

 while True:

   init=raw_input('Enter "s" to start, "credits", "author" or "set" for more information, "q" to quit: ')
   init1=init.strip()
   init2=init1.lower()

   if init2=='s':

     print '*'*40

     while True: #Setting active rotor 1.

       rotor1raw=raw_input('First rotor you wish to use in Roman numeral: ') 
       rotor1raw1=rotor1raw.strip()
       rotor1=rotor1raw1.lower()

       if rotor1=='i':
         rot1=1
         break
        
       elif rotor1=='ii':
         rot1=2
         break
        
       elif rotor1=='iii':
         rot1=3
         break
        
       elif rotor1=='iv':
         rot1=4
         break
        
       elif rotor1=='v':
         rot1=5
         break
        
       else:
         print('info invalid')

     while True: #Setting active rotor 2.

       rotor2raw=raw_input('Second rotor you wish to use in Roman numeral: ')
       rotor2raw1=rotor2raw.strip()
       rotor2=rotor2raw1.lower()

       if rotor2=='i':
         rot2=1
         if rot2==rot1:
           print('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
         else:
           break
        
       elif rotor2=='ii':
         rot2=2
         if rot2==rot1:
           print('Error: 2 rotors used at the same time')
         else:
           break
        
       elif rotor2=='iii':
         rot2=3
         if rot2==rot1:
           print('Error: 2 rotors used at the same time')
         else:
           break
        
       elif rotor2=='iv':
         rot2=4
         if rot2==rot1:
           print('Error: 2 rotors used at the same time')
         else:
           break

       elif rotor2=='v':
         rot2=5
         if rot2==rot1:
           print('Error: 2 rotors used at the same time')
         else:
           break
       else:
         print('info invalid')

     while True: #Setting active rotor 2.
         
       rotor3raw=raw_input('Third rotor you wish to use in Roman numeral: ')
       rotor3raw1=rotor3raw.strip()
       rotor3=rotor3raw1.lower()

       if rotor3=='i':
         rot3=1
         if rot3==rot1:
           print('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
         elif rot3==rot2:
           print('Error: 2 rotors used at the same time')
         else:
           break

       elif rotor3=='ii':
         rot3=2
         if rot3==rot1:
           print('Error: 2 rotors used at the same time')
         elif rot3==rot2:
           print('Error: 2 rotors used at the same time')
         else:
           break
        
       elif rotor3=='iii':
         rot3=3
         if rot3==rot1:
           print('Error: 2 rotors used at the same time')
         elif rot3==rot2:
           print('Error: 2 rotors used at the same time')
         else:
           break
        
       elif rotor3=='iv':
         rot3=4
         if rot3==rot1:
           print('Error: 2 rotors used at the same time')
         elif rot3==rot2:
           print('Error: 2 rotors used at the same time')
         else:
           break
        
       elif rotor3=='v':
         rot3=5
         if rot3==rot1:
           print('Error: 2 rotors used at the same time')
         elif rot3==rot2:
           print('Error: 2 rotors used at the same time')
         else:
           break

       else:
         print('info invalid')

     print'*'*40 #Rotor picking done.
     
     while True: #Setting acitve reflector.

       re_raw=raw_input('Reflecor:(B or C)')
       re2=re_raw.strip()
       re=re2.lower()

       if re=='b':
         ref=1
         break

       elif re=='c':
         ref=2
         break

       else:
         print('info invalid')

     print'*'*40 #Reflector setting done.
     
     print ('First cable:')
     plug1=Plugboard() #Setting first plugboard cable.
     print'*'*30

     while True:
         
       print ('Second cable:')
       plug2=Plugboard() #Setting second plugboard cable.
       
       if plug1.letter1==plug2.letter1:
         print('Error: 2 cables on 1 letter') #Preventing the user from putting two cables on a single letter socket.
         print'*'*20
         
       elif plug1.letter1==plug2.letter2:
         print('Error: 2 cables on 1 letter')
         print'*'*20
         
       elif plug1.letter2==plug2.letter1:
         print('Error: 2 cables on 1 letter')
         print'*'*20
         
       elif plug1.letter2==plug2.letter2:
         print('Error: 2 cables on 1 letter')
         print'*'*20
         
       else:
         break
    
     print'*'*30
    
     while True:
         
       print ('Third cable:')
       plug3=Plugboard() #Setting third plugboard cable.
       
       if plug1.letter1==plug3.letter1:
         print('Error: 2 cables on 1 letter') #Preventing the user from putting two cables on a single letter socket.
         print'*'*20
         
       elif plug1.letter1==plug3.letter2:
         print('Error: 2 cables on 1 letter')
         print'*'*20

       elif plug1.letter2==plug3.letter1:
         print('Error: 2 cables on 1 letter')
         print'*'*20

       elif plug1.letter2==plug3.letter2:
         print('Error: 2 cables on 1 letter')
         print'*'*20

       elif plug2.letter1==plug3.letter2:
         print('Error: 2 cables on 1 letter')
         print'*'*20

       elif plug2.letter1==plug3.letter1:
         print('Error: 2 cables on 1 letter')
         print'*'*20

       elif plug2.letter2==plug3.letter1:
         print('Error: 2 cables on 1 letter')
         print'*'*20

       elif plug2.letter2==plug3.letter2:
         print('Error: 2 cables on 1 letter')
         print'*'*20

       else:
         break
        
     #print'*'*30
     #plug4=Plugboard()
     #print'*'*30
     #plug5=Plugboard()
     #print'*'*30
     #plug6=Plugboard()
     #print'*'*30
     #plug7=Plugboard()
     #print'*'*30
     #plug8=Plugboard()
     #print'*'*30
     #plug9=Plugboard()
     #print'*'*30
     #plug10=Plugboard()
     #print'*'*30
     #plug11=Plugboard()
     #print'*'*30
     #plug12=Plugboard()
     #print'*'*30
     
     print'*'*40 #Plugboard setting done.
    
     print ('Rotor 1')
     rotor1=Rotor()
     print'*'*30
     
     print ('Rotor 2')
     rotor2=Rotor()
     print'*'*30
     
     print ('Rotor 3')
     rotor3=Rotor()

     print'*'*40 #Rotor attributes setting done.
     
     print ('Rotor 1')
     vector1=vector()
     print'*'*30
     
     print ('Rotor 2')
     vector2=vector()
     print'*'*30
     
     print ('Rotor 3')
     vector3=vector()

     lettercount=[]#Ring setting done.

     while True:

       raw1=raw_input('Letter, enter "reset" to reset rotor position: ')
       raw2=raw1.strip()
       letter=raw2.lower()

       if letter=='reset':

         lettercount=[]
         rotor1.ascii_dif=rotor1.raw
         rotor2.ascii_dif=rotor2.raw
         rotor3.ascii_dif=rotor3.raw

       else:
         try:

           test_3=ord(letter)
           if test_3-97<0:
             print 'info invalid'

           elif test_3-97>26:
             print 'info invalid'

           else:

             #print '0',letter
                          
               

             
             plug1.output=interchange(let=letter,letter1=plug1.letter1,letter2=plug1.letter2)
             plug2.output=interchange(let=plug1.output,letter1=plug2.letter1,letter2=plug2.letter2)
             plug3.output=interchange(let=plug2.output,letter1=plug3.letter1,letter2=plug3.letter2)
             #plug4.output=interchange(let=plug3.output,letter1=plug4.letter1,letter2=plug4.letter2)
             #plug5.output=interchange(let=plug4.output,letter1=plug5.letter1,letter2=plug5.letter2)
             #plug6.output=interchange(let=plug5.output,letter1=plug6.letter1,letter2=plug6.letter2)
             #plug7.output=interchange(let=plug6.output,letter1=plug7.letter1,letter2=plug7.letter2)
             #plug8.output=interchange(let=plug7.output,letter1=plug8.letter1,letter2=plug8.letter2)
             #plug9.output=interchange(let=plug8.output,letter1=plug9.letter1,letter2=plug9.letter2)
             #plug10.output=interchange(let=plug9.output,letter1=plug10.letter1,letter2=plug10.letter2)
  

             #print '11',plug3.output
             
             rotor1.output=comparison(let=plug3.output,ascii=rotor1.ascii_dif)
             rotor1.output=comparison(let=rotor1.output,ascii=vector1)


             #print '12',rotor1.output
             
             if rot1==1:
               bombe1=rotorI(let=rotor1.output)
             elif rot1==2:
               bombe1=rotorII(let=rotor1.output)
             elif rot1==3:
               bombe1=rotorIII(let=rotor1.output)
             elif rot1==4:
               bombe1=rotorIV(let=rotor1.output)
             elif rot1==5:
               bombe1=rotorV(let=rotor1.output)

             #print '21',bombe1             

             rotor2.output=comparison(let=bombe1,ascii=rotor2.ascii_dif)
             rotor2.output=comparison(let=rotor2.output,ascii=vector2)

             #print '22',rotor2.output

             if rot2==1:
               bombe2=rotorI(let=rotor2.output)
             elif rot2==2:
               bombe2=rotorII(let=rotor2.output)
             elif rot2==3:
               bombe2=rotorIII(let=rotor2.output)
             elif rot2==4:
               bombe2=rotorIV(let=rotor2.output)
             elif rot2==5:
               bombe2=rotorV(let=rotor2.output)

             #print '31',bombe2

             rotor3.output=comparison(let=bombe2,ascii=rotor3.ascii_dif)
             rotor3.output=comparison(let=rotor3.output,ascii=vector3)

             #print '32',rotor3.output

             if rot3==1:
               bombe3=rotorI(let=rotor3.output)
             elif rot3==2:
               bombe3=rotorII(let=rotor3.output)
             elif rot3==3:
               bombe3=rotorIII(let=rotor3.output)
             elif rot3==4:
               bombe3=rotorIV(let=rotor3.output)
             elif rot3==5:
               bombe3=rotorV(let=rotor3.output)

             if rotor3.ascii_dif==26:
               rotor3.ascii_dif=0

             #print '41',bombe3
               
             if ref==1:
               reflector=reflectorB(bombe3)

             elif ref==2:
               reflector=reflectorC(bombe3)
              

             #print '42',reflector
             
             if rot3==1:
               bombe4=IVrotorI(let=reflector)
             elif rot3==2:
               bombe4=IVrotorII(let=reflector)
             elif rot3==3:
               bombe4=IVrotorIII(let=reflector)
             elif rot3==4:
               bombe4=IVrotorIV(let=reflector)
             elif rot3==5:
               bombe4=IVrotorV(let=reflector)
               
             #print '32',bombe4
             
             rotor3.output=comparison(let=bombe4,ascii=-rotor3.ascii_dif)
             rotor3.output=comparison(let=rotor3.output,ascii=-vector3)

             #print '31',rotor3.output

             if rot2==1:
               bombe5=IVrotorI(let=rotor3.output)
             elif rot2==2:
               bombe5=IVrotorII(let=rotor3.output)
             elif rot2==3:
               bombe5=IVrotorIII(let=rotor3.output)
             elif rot2==4:
               bombe5=IVrotorIV(let=rotor3.output)
             elif rot2==5:
               bombe5=IVrotorV(let=rotor3.output)

             #print '22',bombe5

             rotor2.output=comparison(let=bombe5,ascii=-rotor2.ascii_dif)
             rotor2.output=comparison(let=rotor2.output,ascii=-vector2)

             #print '21',rotor2.output

             if rot1==1:
               bombe6=IVrotorI(let=rotor2.output)
             elif rot1==2:
               bombe6=IVrotorII(let=rotor2.output)
             elif rot1==3:
               bombe6=IVrotorIII(let=rotor2.output)
             elif rot1==4:
               bombe6=IVrotorIV(let=rotor2.output)
             elif rot1==5:
               bombe6=IVrotorV(let=rotor2.output)

             #print '12',bombe6

             rotor1.output=comparison(let=bombe6,ascii=-rotor1.ascii_dif)
             rotor1.output=comparison(let=rotor1.output,ascii=-vector1)

             #print '11',rotor1.output 

             plug3.output=interchange(let=rotor1.output,letter1=plug3.letter1,letter2=plug3.letter2)
             plug2.output=interchange(let=plug3.output,letter1=plug2.letter1,letter2=plug2.letter2)
             plug1.output=interchange(let=plug2.output,letter1=plug1.letter1,letter2=plug1.letter2)
             #plug4.output=interchange(let=plug3.output,letter1=plug4.letter1,letter2=plug4.letter2)
             #plug5.output=interchange(let=plug4.output,letter1=plug5.letter1,letter2=plug5.letter2)
             #plug6.output=interchange(let=plug5.output,letter1=plug6.letter1,letter2=plug6.letter2)
             #plug7.output=interchange(let=plug6.output,letter1=plug7.letter1,letter2=plug7.letter2)
             #plug8.output=interchange(let=plug7.output,letter1=plug8.letter1,letter2=plug8.letter2)
             #plug9.output=interchange(let=plug8.output,letter1=plug9.letter1,letter2=plug9.letter2)
             #plug10.output=interchange(let=plug9.output,letter1=plug10.letter1,letter2=plug10.letter2)

             lettercount.extend(plug1.output)
             print 'Output:',plug1.output
             print 'Letter count:',lettercount

             #rotor1.ascii_dif=rotor1.ascii_dif+1
             if rotor1.ascii_dif==26:
               rotor1.ascii_dif=0
               rotor2.ascii_dif=rotor2.ascii_dif+1

             if rotor2.ascii_dif==26:
               rotor2.ascii_dif=0
               rotor3.ascii_dif=rotor3.ascii_dif+1

         except:
             print('Info invalid')
           
             
             

           

   elif init2=='credits':

     print ('')
     
   elif init2=='author':

     print '*'*40
     print ('This program is created by Alexander Liao, an independent programming hobbyist.')
     print '*'*40
     
   elif init2=='set':
       
     print '*'*40
     print ('Rotor I:   EKMFLGDQVZNTOWYHXUSPAIBRCJ')
     print ('Rotor II:  AJDKSIRUXBLHWTMCQGZNPYFVOE')
     print ('Rotor III: BDFHJLCPRTXVZNYEIWGAKMUSQO')
     print ('Rotor IV:  ESOVPZJAYQUIRHXLNFTGKDCMWB')
     print ('Rotor V:   VZBRGITYUPSDNHLXAWMJQOFECK')
     print ('Reflector B: YRUHQSLDPXNGOKMIEBFZCWVJAT')
     print ('Refeector C: FVPJIAOYEDRZXWGCTKUQSBNMHL')
     print '*'*40
     
   elif init2=='q':

     break
    
   else:
      
      print ('info invalid')
     
              
if __name__=="__main__":
    main()
         
