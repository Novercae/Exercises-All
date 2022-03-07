'''
Reverse a list without (sort, reverse)
Ex:
  >>> list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  >>> list.sort(reverse=True)
  >>> print(list)
'''

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
end = len(list) - 1

for i in range(len(list)//2):
    list[i], list[end] = list[end], list[i]
    end -= 1

print(list)
