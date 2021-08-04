#Tuples are identical to list in all respects,except for the folllowing properties
#1.Tuples are defined by enclosing the elements in paranthesis( {} ).
#2. Tuples are immutable

#Defining a tuple
fruits=("apple","banana","orange","pear","mango")

'''
print(type(fruits))
for i in fruits:
    print(i)


print(fruits[4])
print(fruits[0:3])
'''

#What are benefits of using tuples instead of lists in python?
fruits=("apple","banana","orange","pear","mango") #tuple packing
'''
(a1,a2,a3,a4,a5)=fruits  #Tuple unpacking
print(a1)
print(fruits)
print(a2,a3,a4,a5)

(a1,a2,a3)=fruits
'''

fruits=("apple","banana","orange","pear","mango")
fruit_1=("apple","banana",("orange","pear"),"mango")
'''
print(type(fruit_1))
print(fruit_1)

print(fruit_1[2][0])
'''
(a1,a2,a3,a4,a5)=fruits
#>>> a1
#>>> a1,a2=a2,a1       #for swapping 
#>>> a1
#'banana'

print(len(fruit_1[2][0]))

