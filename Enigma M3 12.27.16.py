import time
from datetime import datetime

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
 
#################################################################################################################################   

def input_position ():

        while True:

            raw_1=raw_input('Starting position of the wheel (it is a letter):')
            raw_2=raw_1.strip()
            start_position=raw_2.lower()

            if start_position.isdigit()==True:
              
              print ('info invalid')

            else:

              try:
                test=ord(start_position)
                return start_position
                break

              except:
                print ('info invalid')
                
    
def  calc_output (start, string):
        
        a=string
        b=string
        ind=start
        n=a.index(ind)
        i=1
        v=1

        while v<n:
            d=b[v]
            v+=1
            a.append(d)
            
        while i<n:
            i += 1
            a.pop(1)



        return a

def clockwiserotate (stepper, string):
  n=stepper
  v=1
  k=1
  a=string
  b=a

  while v<n:
    b.append(a[v])
    v+=1
  for k in range(1,n,+1):
    del b[k]
    k+=1





  return b

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




def ring_setting (sett, string):

        a=string
        b=string
        n=sett
        i=1
        v=1

        while v<n:
          d=b[v]
          v+=1
          a.append(d)
          
        while i<n:
          i+=1
          a.pop(1)



        return a
#################################################################################################################################

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

    if con_input==21:
        result='u'
        
    if con_input==22:
        result='v'

    if con_input==23:
        result='w'

    if con_input==24:
        result='x'
        
    if con_input==25:
        result='y'
        
    if con_input==26:
        result='z'
        
    return result

#################################################################################################################################   

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

#################################################################################################################################

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

#################################################################################################################################

def main():
  
  print ('Welcome, this is an digital emulator of the Enigma M3.')
  print (' ')
  print ('This version is used extensively by German Army (Heer) during World War II, where approximately 800 units were built.')
  print ('This emulator contains THREE available Steckerbrett cables and all EIGHT wheels.')
  print ('Five of the wheels are the same as the one used in Enigma I, which is used by German army and airforce.')
  print ('Of all the Umkehrwalze (reflectors) used, only type B and C are available in this emulator ')
  print ('')
  print ('The info you need to enter is listed below:')
  print ('')
  print ('    Ringstellung (relative position of alphabet ring to rotor disk)')
  print ('    Grundstellung (initial position of the rotors)')
  print ('    Walzenlage (order of THREE rotors you wish to use in Roman numerals)')
  print ('    ONE in TWO reflectors you wish to use')
  print ('             ')
  print ('The settings of wheels and Umkehrwalze are historically correct, which you can access by typing "set".')
  print ('To use the "daily keys" to encrypt your initial positions, type in the keys when the value of the Grundstellung is requested.')  
  print ('You need to type "reset" in order to reset the position of the wheels')

 

  while True:

    wheelI=['null','e','k','m','f','l','g','d','q','v','z','n','t','o','w','y','h','x','u','s','p','a','i','b','r','c','j']

    wheelII=['null','a','j','d','k','s','i','r','u','x','b','l','h','w','t','m','c','q','g','z','n','p','y','f','v','o','e']

    wheelIII=['null','b','d','f','h','j','l','c','p','r','t','x','v','z','n','y','e','i','w','g','a','k','m','u','s','q','o']

    wheelIV=['null','e','s','o','v','p','z','j','a','y','q','u','i','r','h','x','l','n','f','t','g','k','d','c','m','w','b']
    
    wheelV=['null','v','z','b','r','g','i','t','y','u','p','s','d','n','h','l','x','a','w','m','j','q','o','f','e','c','k']

    wheelVI=['null','j','p','g','v','o','u','m','f','y','q','b','e','n','h','z','r','d','k','a','s','x','l','i','c','t','w']

    wheelVII=['null','n','z','j','h','g','r','c','x','m','y','s','w','b','o','u','f','a','i','v','l','p','e','k','q','d','t']

    wheelVIII=['null','f','k','q','h','t','l','x','o','c','b','j','s','p','d','z','r','a','m','e','w','n','i','u','y','g','v']
    
    in_wheelI=['null','u','w','y','g','a','d','f','p','v','z','b','e','c','k','m','t','h','x','s','l','r','i','n','q','o','j']

    in_wheelII=['null','a','j','p','b','z','w','r','l','f','b','d','k','o','t','y','u','q','g','e','n','h','x','m','i','v','s']
    
    in_wheelIII=['null','t','a','g','b','p','c','s','d','q','e','u','f','v','n','z','h','y','i','x','j','w','l','r','k','o','m']
    
    in_wheelIV=['null','h','z','w','v','a','r','t','n','l','g','u','p','x','q','c','e','j','m','b','s','k','d','y','o','i','f']

    in_wheelV=['null','q','c','y','l','x','w','e','n','f','t','z','o','s','m','v','j','u','d','k','g','i','a','r','p','h','b']

    in_wheelVI=['null','s','k','x','q','l','h','c','n','w','a','r','v','g','m','e','b','j','p','t','y','f','d','z','u','i','o']

    in_wheelVII=['null','q','m','g','y','v','p','e','d','r','c','w','t','i','a','n','u','x','f','k','z','o','s','l','h','j','b']

    in_wheelVIII=['null','q','j','i','n','s','a','y','d','v','k','b','f','r','u','h','m','c','p','l','e','w','z','t','g','x','o']

    UKW_B=['null','y','r','u','h','q','s','l','d','p','x','n','g','o','k','m','i','e','b','f','z','c','w','v','j','a','t']
    
    UKW_C=['null','f','v','p','j','i','a','o','y','e','d','r','z','x','w','g','c','t','k','u','q','s','b','n','m','h','l']



    start = raw_input('Enter "s" to start, "credits", "author" or "wiring" for more information, "q" to quit: ')

    s1= start.strip()
    init= s1.lower()
    
    if init=='s':

  

      print '*'*40 #Picking Wheels
      print ('initiating basic configuration procedure...')
      time.sleep(0.1)

      while True: #Setting wheel 1.

        wheel_1raw=raw_input('First wheel you wish to use (from right to left) in Roman numeral: ') 
        wheel_1raw1=wheel_1raw.strip()
        wheel_1=wheel_1raw1.lower()

        if wheel_1=='i':
            wheel1=wheelI
            in_wheel1=in_wheelI
            break
        elif wheel_1=='ii':
            wheel1=wheelII
            in_wheel1=in_wheelII
            break
        elif wheel_1=='iii':
            wheel1=wheelIII
            in_wheel1=in_wheelIII
            break
        elif wheel_1=='iv':
            wheel1=wheelIV
            in_wheel1=in_wheelIV
            break
        elif wheel_1=='v':
            wheel1=wheelV
            in_wheel1=in_wheelV
            break
        elif wheel_1=='vi':
            wheel1=wheelVI
            in_wheel1=in_wheelVI
            break
        elif wheel_1=='vii':
            wheel1=wheelVII
            in_wheel1=in_wheelVII
            break
        elif wheel_1=='viii':
            wheel1=wheelVIII
            in_wheel1=in_wheelVIII
            break
        else:
          print('info invalid')

      while True: #Setting wheel 2.

        wheel_2raw=raw_input('Second wheel you wish to use in Roman numeral: ') 
        wheel_2raw1=wheel_2raw.strip()
        wheel_2=wheel_2raw1.lower()

        if wheel_2=='i':
            wheel2=wheelI
            in_wheel2=in_wheelI
            if wheel2==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            else:
                break
        elif wheel_2=='ii':
            wheel2=wheelII
            in_wheel2=in_wheelII
            if wheel2==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            else:
                break
        elif wheel_2=='iii':
            wheel2=wheelIII
            in_wheel2=in_wheelIII
            if wheel2==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            else:
                break
        elif wheel_2=='iv':
            wheel2=wheelIV
            in_wheel2=in_wheelIV
            if wheel2==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            else:
                break
        elif wheel_2=='v':
            wheel2=wheelV
            in_wheel2=in_wheelV
            if wheel2==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            else:
                break
        elif wheel_2=='vi':
            wheel2=wheelVI
            in_wheel2=in_wheelVI
            if wheel2==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            else:
                break
        elif wheel_2=='vii':
            wheel2=wheelVII
            in_wheel2=in_wheelVII
            if wheel2==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            else:
                break
        elif wheel_2=='viii':
            wheel2=wheelVIII
            in_wheel2=in_wheelVIII
            if wheel2==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            else:
                break
        else:
          print('info invalid')

      while True: #Setting wheel 3.

        wheel_3raw=raw_input('Third wheel you wish to use in Roman numeral: ') 
        wheel_3raw1=wheel_3raw.strip()
        wheel_3=wheel_3raw1.lower()

        if wheel_3=='i':
            wheel3=wheelI
            in_wheel3=in_wheelI
            if wheel3==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            elif wheel3==wheel2:
                print ('Error: 2 rotors used at the same time')
            else:
                break
        elif wheel_3=='ii':
            wheel3=wheelII
            in_wheel3=in_wheelII
            if wheel3==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            elif wheel3==wheel2:
                print ('Error: 2 rotors used at the same time')
            else:
                break
        elif wheel_3=='iii':
            wheel3=wheelIII
            in_wheel3=in_wheelIII
            if wheel3==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            elif wheel3==wheel2:
                print ('Error: 2 rotors used at the same time')
            else:
                break
        elif wheel_3=='iv':
            wheel3=wheelIV
            in_wheel3=in_wheelIV
            if wheel3==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            elif wheel3==wheel2:
                print ('Error: 2 rotors used at the same time')
            else:
                break
        elif wheel_3=='v':
            wheel3=wheelV
            in_wheel3=in_wheelV
            if wheel3==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            elif wheel3==wheel2:
                print ('Error: 2 rotors used at the same time')
            else:
                break
        elif wheel_3=='vi':
            wheel3=wheelVI
            in_wheel3=in_wheelVI
            if wheel3==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            elif wheel3==wheel2:
                print ('Error: 2 rotors used at the same time')
            else:
                break
        elif wheel_3=='vii':
            wheel3=wheelVII
            in_wheel3=in_wheelVII
            if wheel3==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            elif wheel3==wheel2:
                print ('Error: 2 rotors used at the same time')
            else:
                break
        elif wheel_3=='viii':
            wheel3=wheelVIII
            in_wheel3=in_wheelVIII
            if wheel3==wheel1:
                print ('Error: 2 rotors used at the same time') #Preventing user from using two identical rotors.
            elif wheel3==wheel2:
                print ('Error: 2 rotors used at the same time')
            else:
                break
        else:
          print('info invalid')


      print'*'*40 #Wheel picking done.

 
      print wheel1
      print wheel2
      print wheel3

      
      while True: #Setting acitve reflector.

       re_raw=raw_input('Reflecor:(B or C)')
       re2=re_raw.strip()
       re=re2.lower()

       if re=='b':
         reflector=UKW_B
         break

       elif re=='c':
         reflector=UKW_C
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

      print'*'*40 #Plugboard setting done.

      
      print ('Wheel 1')
      position1=input_position()
      wheel_one_start=calc_output(start=position1,string=wheel1)
      print'*'*30


      print ('Wheel 2')
      position2=input_position()
      wheel_two_start=calc_output(start=position2,string=wheel2)
      print'*'*30

      print ('Wheel 3')
      position3=input_position()
      wheel_three_start=calc_output(start=position3,string=wheel3)
      print'*'*30#Starting position setting done.

      print wheel_one_start
      print wheel_two_start
      print wheel_three_start

      print ('Wheel 1')
      vector1=vector()
      wheel_one_output=ring_setting(sett=vector1, string=wheel_one_start)
      print'*'*30
     
      print ('Wheel 2')
      vector2=vector()
      wheel_two_output=ring_setting(sett=vector2, string=wheel_two_start)
      print'*'*30
     
      print ('Wheel 3')
      vector3=vector()
      wheel_three_output=ring_setting(sett=vector3, string=wheel_three_start)

      lettercount=[]#Ring setting done.  
      stepper1=0
      stepper2=0
      stepper3=0 
      print ('Basic configuration finished.')

      print wheel_one_output
      print wheel_two_output
      print wheel_three_output




      while True:

       raw1=raw_input('Letter, enter "reset" to reset rotor position: ')
       raw2=raw1.strip()
       letter=raw2.lower()

       if letter=='reset':

         lettercount=[]
         stepper1=0
         stepper2=0
         stepper3=0 

       else:

         #try:

           test_3=ord(letter)
           if test_3-97<0:
             print 'info invalid'

           elif test_3-97>26:
             print 'info invalid'

           else:

               stepper1=2
               
               plug1.output=interchange(let=letter,letter1=plug1.letter1,letter2=plug1.letter2)
               plug2.output=interchange(let=plug1.output,letter1=plug2.letter1,letter2=plug2.letter2)
               plug3.output=interchange(let=plug2.output,letter1=plug3.letter1,letter2=plug3.letter2)

               plugcon=conversion(con_input=plug3.output)

               print plug3.output
               
               access1=plugcon
               
               if access1<=0:
                   access1=26-access1

               if access1>26:
                   access1=access1-26

               print access1
               print wheel_one_output

               wheel_one_output=clockwiserotate(stepper=stepper1, string=wheel_one_output)

               print wheel_one_output

               output1=wheel_one_output[access1]

               print output1

               outcon1=conversion(con_input=output1)
               access2=outcon1
               if access2<=0:
                   access2=26-access2

               wheel_two_output=clockwiserotate(stepper=stepper2, string=wheel_two_output)

               output2=wheel_two_output[access2]

               print output2

               outcon2=conversion(con_input=output2)
               access3=outcon2
               if access3<=0:
                   access3=26-access3

               wheel_three_output=clockwiserotate(stepper=stepper3, string=wheel_three_output)

               output3=wheel_three_output[access3]

               print output3
               #print wheel_three_output

               outcon3=conversion(con_input=output3)
               
               ref_output=reflector[outcon3]

               print ref_output
               print stepper1

               ref_con=conversion(con_input=ref_output)

               wheel3interval=clockwiserotate(stepper=stepper3,string=wheel_three_output)
               wheel3inverse=calc_inverse(string=wheel3interval)

               in_output3=wheel3inverse[ref_con]

               #print wheel3inverse
               print in_output3
               
               in_access2=conversion(con_input=in_output3)

               wheel2interval=clockwiserotate(stepper=stepper2,string=wheel_two_output)
               wheel2inverse=calc_inverse(string=wheel2interval)   

               in_output2=wheel2inverse[in_access2]

               print in_output2
               
               in_access1=conversion(con_input=in_output2)   

               wheel1interval=clockwiserotate(stepper=stepper1,string=wheel_one_output)
               wheel1inverse=calc_inverse(string=wheel1interval)  

               in_output1=wheel1inverse[in_access1]

               print in_output1
               print stepper1

               plug1.output=interchange(let=in_output1,letter1=plug1.letter1,letter2=plug1.letter2)
               plug2.output=interchange(let=plug1.output,letter1=plug2.letter1,letter2=plug2.letter2)
               plug3.output=interchange(let=plug2.output,letter1=plug3.letter1,letter2=plug3.letter2)

               lettercount.extend(plug3.output)
               print 'Output:',plug3.output
               print 'Letter count:',lettercount





         #except:
           #print ('info invalid')
               

            
    elif init=='credits':
        print('nothing yet')
      
    elif init=='author':
        print('nothing yet')
     
    elif init=='wiring':
        print('nothing yet')
      
    else:
      print ('info invalid')
        

    
if __name__=="__main__":
    main()   



