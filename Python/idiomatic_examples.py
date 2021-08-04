#Idiomatic python

#
sum=sum+1

sum+=1

#
print()
x='apple'
y='apple'
z='apple'

x=y=z='apple'

#
print()
print('hello')
print('world')

print('hello\nworld')

#
print()
a,b=1,2
print(a,b)
rev=a
a=b
b=rev
print(a,b)

print()
a,b=1,2
print(a,b)
a,b=b,a
print(a,b)

#
a=True
val=0
if a:
  val=1
print(val)

a=True
val= 1 if a else 0
print(val)

#
print()
for i in [0,1,2,3,4,5,6]:
    print (i*3)
print()
for i in range(7):
    print (i*3)

#
print()
name='apple'
price='100'
if name: print(name)
print(price)


if name:
   print(name)
print(price)

#
fruits=['apple','banana','orange','grapes','melon']
print()
for i in range(len(fruits)):
    print (fruits[i])
print()
for fruit in fruits:
    print(fruit)

#
print()
for i in range (len(fruits)-1,-1,-1):
    print(fruits[i])
print()
for fruit in reversed(fruits):
    print(fruit)

#
print()
fruit='melon'
found= False
if fruit == 'melon' or fruit== 'orange' or fruit=='apple':
    found=True
print(fruit)

fruit='melon'
found= fruit in {'melon','orange','apple'}

#
print()
fruits=['apple','banana','orange','grapes','melon']
index=0
while index<len(fruits):
    print(fruits[index])
    index+=1
print()
for fruit in fruits:
    print(fruit)

#
print()
a=fruits[0]
for fruit in fruits[1:]:
    a+=','+fruit
print(a)
print()

print(','.join(fruits))

#
print()
a=('apple',15,'hyd',5)
name=a[0]
price=a[1]
place=a[2]
dis=a[3]

name,price,place,dis=a

#
print()
def fibonacci(n):
    x=0
    y=1
    for i in range(n):
        print(x)
        t=y
        y=x+y
        x=t

def fibonacci(n):
    x,y=0,1
    for i in range(n):
        print (x)
        x,y=y,x+y

#
print()
result=[]
for i in range(10):
     a=i**2
     result.append(a)
print (sum(result))


print(sum(i**2 for i in range(10)))

#
print()
if user:
      print('----------------------')
      print(user)
      print('----------------------')

if user:
    print('{0}\n{1}\n{0}'.format('-'*20, user))


#
print()
fruits=['apple','banana','orange','grapes','melon']
a=list(fruits)
a.sort()
print()

a=sorted(fruits)

#
print()
fruits =  [("apple", 10), ("banana", 20), ("orange", 50)]
for a in fruits:
    name = a[0]
    price = a[1]
    print("Item is " + name + ". The price is " + str(price))

print()
fruits = [("apple", 10), ("banana", 20), ("orange", 50)]
for a in fruits:
    name = a[0]
    price = a[1]
    print("Item is {}. The price is {}.".format(name, price))

#
print()
person = input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)

person = input('Enter your name: ')
print('Hello {}!'.format(person))


#
print()
a=[1,2,3,4,5]
b=[4,5,6,7,8]
numbers=[]
for num in a:
    if num in b:
        numbers.append(num)
print(numbers)


numbers=list(set(a) & set(b))
print(numbers)














    


