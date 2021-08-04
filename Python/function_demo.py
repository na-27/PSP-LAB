'''
A function in python is a place of code which runs when it is referenced.
It is used to to utilize the code in more than one place in a program, in-built functions, user defined
functions
print(),input[]
'''

def add(x,y):
    return x+y
'''
x=3
y=4
z=add(x,y)
print("z=",z)
#print(add(30,40))
#print(add(30,40))

def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def square(x):
    return x*x
print(square(20))


#Lambda Function : It is an anonymous function or a function having no name.
#It is a small and restricted function having no more than one line.
#lambda p1,p2: expression



adder=lambda x,y : x+y 
print(adder(1,2))

import math
euclidian_distance= lambda x,y: math.sqrt((x**2) + (y**2))
print(euclidian_distance(3,4))


#map{} --> It is used to apply a particular operation to every element in a sequence

even_list= [2,4,6,8,10]

squared_even_list= map (lambda x:x*x, even_list)

print(list(squared_even_list))
'''


#C=[39.2, 36.5, 37.3, 38, 37.8] is a list containing temperature values in degree
#celsius. Using lamda function convert the above list of temperature values in Fahrenheit.

C=[39.2, 36.5, 37.3, 38, 37.8]
F=map(lambda x:((9/5 * x) + 32),C)
print(list(F))



