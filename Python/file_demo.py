#file handling in python

'''
f= open("C:/Users/addep/OneDrive/Desktop/example/names.txt.txt","r")

if f.mode =="r":
   contents = f.read()
   print(contents)

'''
#when text file in same folder dont need to type full path of file.
'''
f=open("example1.txt","r")

if f.mode =="r":
    contents = f.read()
    print(contents)

'''
'''
f=open("example1.txt","a")
f.write(" Welcome to programming")
f.close()
'''

'''
f=open("example1.txt","a")
f.write(" Welcome to programming")
f=open("example1.txt","r")
contents=f.read()
print(contents)
f.close()
'''

f=open("example1.txt","w")
if f.mode== "w":
    f.write("Hello world!")
f.close()



