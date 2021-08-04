
fruits=["apple", "banana", "orange", "grapes", "melon"]
fruit_info=['apple',10.5,23,'FRUIT',['grapes','melon','orange']]


'''
print(type(fruits))
print(fruits)
print(type(fruit_info))
print(fruit_info)
'''


#list slicing
'''
print(fruits[0:3])
print(fruits[0:4])
print(fruits[2:-1])
'''
'''
fruits=["apple", "banana", "orange", "grapes", "melon"]
fruit_info=['apple',10.5,23,'FRUIT',['grapes','melon','orange']]
print(fruit_info[1:-2])
print(fruit_info[-1][1]) #should give another subscript to print in the list
'''

#appending list elements

'''
fruits.append("papaya")
print(fruits)
'''

#modification of list
'''
fruits[2]="pear"
print(fruits)
'''


#length of a list

'''
print(len(fruits))
'''

#removing an element from the list
'''
fruits.pop(1)
print(fruits)
'''

#finding index of an element
'''
melon_index=fruits.index("melon")
print(fruits)
print(melon_index)

for element in fruits:
    print(element)
'''












