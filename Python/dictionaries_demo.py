# A Dictionary in python is the unorderes and changeable collection of data values that holds key-value pairs.
# A Dictionary in python is declared by enclosing a comma-separated list of key-value pairs using curly braces({}).
#Syntax for python Dictionary

'''
student1={'Name':'Neha', 'Branch':'ECE','Section':'A','Roll_no':27} #no '' in 27 as it is a number}
print(type(student1))
print(student1)
'''

'''
student1={'Name':'Neha', 'Branch':'ECE','Section':'A','Roll_no':27,'Name':'apple'}
print(student1) #neha will be replaces by apple
'''

'''
student1={'Name':'Neha', 'Branch':'ECE','Section':'A','Roll_no':27} 
print(student1['Branch'])
'''

'''
student1={'Name':'Neha', 'Branch':'ECE','Section':'A','Roll_no':27}
print("Before updating")
print(student1)
#'Member':'PSP'

student1.update({'Member':'PSP'})
print("After updating")
print(student1)
'''


#Delete keys from dictionaries
'''
student1={'Name':'Neha', 'Branch':'ECE','Section':'A','Roll_no':27,'Member':'PSP'} 
print("Before deleting")
print(student1)
del student1['Name']
print("After deleting")
print(student1)

print(student1.items())      
'''

student1={'Name':'Neha', 'Branch':'ECE','Section':'A','Roll_no':27,'Member':'PSP'}
#print("Keys of student1 are")
#print(student1.keys())

for i in student1.keys():
    print(student1[i])
    print(student1.values())





































