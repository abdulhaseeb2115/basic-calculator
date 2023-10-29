print("NOTE:This calculator can perform;;\n---Simple Arthematic Calculations---Trignometric calculations---Determinant---Factorial---RAD to DEG\n\
---DEG to RAD---Perfect Square---Square root---Square---Discriminant---Decimal to Binary\n\
---Binary to Decimal---Power to any number---LCM---")

print("\nPRESS::'A'--for Arth calculations>><<'T'--for Trig calculations>><<'D'--for Determinant>><<'F'--for Factorial>>\n\
       <<'RD'--for Rad to Deg>><<'DR'--for Deg to Rad>><<'P'--for Perfect NO>><<'SR'--for Square root>>\n\
       <<'SQ'--for Square>><<'DI'--for Disc>><<'DB'--for Deci to Bin>><<'BD'--for Bin to Deci>><<'PW'--for Power>><<'L'--for Lcm>><<")


#//////////////////////////////////FUNCTION///////////////////////////////////////


def calculator():
 #/////////////////////////////////START////////////////////////////////////////////
 choice=input("                       What do you want to do?.....")
 #ARTHEMATIC/////////////////////////////////////////////////////////
 if choice=='A' or choice=='a':
    yn='T'
    x=eval(input("Enter number:"))
    while yn=='T':
        opr=str(input("Enter operator:"))
        y=eval(input("Enter number:"))
        yn=input("Press'Q' to Quit::")
        if opr=='+':
            x=x+y
        elif opr=='-':
            x=x-y
        elif opr=='*':
            x=x*y
        elif opr=='/':
           if y!=0:
               x=x/y
           else:
               x="Not Possible"
               break
        if yn=='Q' or yn=='q':
            break
        yn='T'
    print("Answer=",x)

 #DETERMINANT///////////////////////////////////////////////////////////////

 elif choice=='D' or choice=='d':
    print("----Enter rows with '3' elements seperated by commas----")
    a1,b1,c1=eval(input("Enter 1st row :"))
    a2,b2,c2=eval(input("Enter 2nd row:"))
    a3,b3,c3=eval(input("Enter 3rd row:"))
    det=(a1*((b2*c3)-(c2*b3)))+(-b1*((a2*c3)-(c2*a3)))+(c1*((a2*b3)-(a3*b2)))
    print("Determinat is",det)
    
 #TRIGNOMETRIC//////////////////////////////////////////////////////////////

 elif choice=='T' or choice=='t':
    import math
    trig=input("Enter trig function:")
    ang=eval(input("Enter angle:"))
    if trig=='sin':
        print(math.sin(ang))
    elif trig=='cos':
        print(math.cos(ang))
    elif trig=='tan':
        print(math.tan(ang))
    elif trig=='cosec' or trig=='csc':
        print(1/math.sin(ang))
    elif trig=='sec':
        print(1/math.cos(ang))
    elif trig=='cot':
        print(1/math.tan(ang))
    else:
        print("invalid")

 #FACTORIAL//////////////////////////////////////////////////////

 elif choice=='F' or choice=='f':
    x=eval(input(":"))
    sum=1
    while x>0:
        sum=sum*x
        x=x-1
    print(sum)

 #SQUARE//////////////////////////////////////////////////////////

 elif choice=='sq' or choice=='SQ':
  num=eval(input("Enter number:"))
  ans=num**2
  print("Square of",num,"is",ans)

#SQUARE ROOT///////////////////////////////////////////////////

 elif choice=='sr' or choice=='SR':
      num=eval(input("Enter number:"))
      ans=num**0.5
      print("Square Root of",num,"is",ans)

#RAD to DEG///////////////////////////////////////////////////////
 #DEG to RAD///////////////////////////////////////////////////////
 elif choice=='DR' or choice=='dr':
     import math
     deg=eval(input("Enter value in degrees:"))
     print(math.radians(deg),"Radians")

#DISC///////////////////////////////////////////////////////////////
 elif choice=='di' or choice=='DI':
     a,b,c=eval(input("Enter values of a,b&c seperated by commas:"))
     disc=(b**2)-(4*a*c)
     print("disc of",a,",",b,"&",c,"i=",disc)

#  PERFECT SQUARE////////////////////////////////////////////////
 elif choice=='p' or choice=='P':
     num=eval(input("Enter number:"))
     ans=num**0.5
     if ans%2==0 or ans%2==1:
              print(num,"is a Perfect square")
     else:
               print(num,"is not a Perfect square")
 #DECIMAL TO BINARY////////////////////////////////////////////
 elif choice=='DB' or choice=='db':
     num=int(input("Enter a number:"))
     ans=[]
     while num>=1:
         s=num%2
         num=num//2
         ans.append(s)
     ans.reverse()
     for i in ans:
         print(i,end="")
     print()
 #BINARY TO DECIMAL////////////////////////////////////////////
 elif choice=='BD' or choice=='bd':
     length=int(input("Enter length of number to convert:"))
     num=eval(input("Enter binary number:"))
     x=1
     z=0
     k=0
     while x<=length:
        y=num%10
        s=y*(2**k)
        x=x+1
        k=k+1
        z=z+s
        num=num//10
     print("decimal is",z)
#POWER///////////////////////////////////////////////////////////
 elif choice=='pw' or choice=='PW':
       num=eval(input("Enter number:"))
       power=int(input("Enter power:"))
       print(num,"raised to power",power,"=",num**power)
#LCM////////////////////////////////////////////////////////////\
 elif choice=='l' or choice=='L':
      def lcm(x, y):
        if x > y:
            gtr = x
        else:
            gtr = y
        while(True):
            if((gtr % x == 0) and (gtr % y == 0)):
                lcm = gtr
                break
            gtr += 1
        print( "Lcm of",x,"and",y,"is",lcm)

      x=eval(input("Enter number:"))
      y=eval(input("Enter number:"))
      lcm(x,y)
 else :
     print("Invalid Input.")  
#////////////////////////////////END///////////////////////////////
calculator()
more='M'
while more=='M':
    more=input("Print 'M' for more calculations:")
    if more=='M' or more=='m':
        calculator()
    else:
        print("BYE")
        break
    more='M'

  
