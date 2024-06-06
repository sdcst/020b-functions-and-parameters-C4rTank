#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side

assert hypotenuse(3,4,True) == 5
(2 points)
"""

def hypotenuse():
    num1 = 0   
    num2 = 0
    boolean = ""

    while num1 == 0:
        q1 = input("Please input your first number: ")
        
        try:
            num1 = int(q1)

        except:
            print("Invalid input")
            print("Please try again")
    
    while num2 == 0:
        q2 = input("Please input your second number: ")

        try:
            num2 = int(q2)
        except:
            print("Invalid input")
            print("Please try again")

    while boolean == '':
        boolean = input("Is the boolean is True or False? (T/F): ")
    
        try:
            if boolean == 'T':
        
                import math

                a = math.pow(num1,2)
                b = math.pow(num2,2)

                c = a + b
                c = float(c)
                answer = math.sqrt(c)
                answer = round(answer,2)

                print('(',num1,',',num2,',',boolean,') ==', answer)
                print(answer,"is your hypotenuse!")
            if boolean == 'F':
        
    
                if num1 > num2:
                    print(num1,"is your hypotenuse!")
                    print('(',num1,',',num2,',',boolean,')' ,'==',num1)
                else:
                    print(num2,"is your hypotenuse!")
                    print('(',num1,',',num2,',',boolean,')' ,'==',num2)

        except:
            print("Invalid input")
            print("Please try again")





hypotenuse()

#done



