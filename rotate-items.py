"""
rotate items in a list
Ex:
  list = [ 1,2,3,4,5,6,7]
  number = 3
  expected return = [5,6,7,1,2,3,4]
"""

list = [1,2,3,4,5,6,7]
number_of_times = 3

def rota(list, n):
    list = (list[len(list) - n:len(list)] + list[0:len(list) - n])
    return print(list)

rota(list, number_of_times)
