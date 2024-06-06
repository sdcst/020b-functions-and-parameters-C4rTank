#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger():
    
    num = input("Please enter a number: ")
  
    if '.' in num:
      print('False')

    else:
      print('True')


isInteger()

#done