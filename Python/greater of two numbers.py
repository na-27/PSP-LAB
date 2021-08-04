#conditional statements
# using if statements

x=int(input("enter first number "))
print("x=",x)
print(type(x))
y=int(input("enter second number "))
print("y=",y)
print(type(y))
if x>y:
   print("x is greater than y")
elif x==y:
   print("x is equal to y")
else:
   print("y is greater than x")
z=x+y
print("z=",z)
