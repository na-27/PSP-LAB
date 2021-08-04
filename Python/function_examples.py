'''
#C=[39.2, 36.5, 37.3, 38, 37.8] is a list containing temperature values in degree
#celsius. Using lamda function convert the above list of temperature values in Fahrenheit.

C=[39.2, 36.5, 37.3, 38, 37.8]
F=map(lambda x:((9/5 * x) + 32),C)
print(list(F))
'''

#lambdas in reduce()

from functools import reduce
even_list=[2,4,6,8,10]
product= reduce(lambda x,y:x*y, even_list)
print(product)

from functools import reduce
even_list=[2,4,6,8,10]
squares= reduce(lambda x,y: x+y*y,even_list)
print(squares)

