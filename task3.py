#!python3
"""
Create a function called perimeter()
The input is a list or tuple.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""
def perimeter():
  
  Tuple = ()
  a = 0
  
  while a < 10:
    
    try:
      num = int(input("Please enter a number: "))
      Tuple = Tuple + (num,)
      a = a + 1
    except:
      print("Not a number")
      print("Please try again!")
    
    
    if a == 10:
      List = list(Tuple)
      Everything = sum(List)
      Everything_str = str(Everything)
      print("Everything added in the list is", Everything_str+'!')

perimeter()

#done

