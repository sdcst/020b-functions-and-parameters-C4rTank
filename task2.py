#!python3
"""
##### Task 2
Create a function called largest.
The input is a list or tuple.
Your function should convert any tuples to lists so that you can sort
it and find the largest.
If you are stuck, don't forget to refer to your assignment on lists to help you sort (or ask Google)
The return value is the largest value in the list
(2 points)
"""




def largest():
  
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
      List.sort()
      print(List)
      for max in [9]:
        print(List[max],'is your lagrest number!')

largest()

#done