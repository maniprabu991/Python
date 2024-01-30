class runmultipleFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        List=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for display in List:
            print(display)
                    
    def OddEven():
        num = int(input("Enter a number: "))
        if ((num % 2) == 0):
            print("{0} is Even number".format(num))
        else:
            print("{0} is Odd number".format(num))
                    
    def Eligible():
        gender = input('Your Gender:')
        age = int(input('Your Age:'))
        if(gender=='Male'):
            if(age>=21):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        elif(gender=='Female'):
            if(age>18):
                 print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        else:
            print('INVALID INPUT DATA')
            
    def percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        Total = sub1+sub2+sub3+sub4+sub5
        print("Total : ",Total)
        Percent = (Total / 500) * 100
        print("Percentage : ",Percent)
          
    def triangle():
        Height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(Height*breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Height1+Height2+breadth)