name='neha'
#print(name)
#print(type(name))

subject1='my '
subject2='name '
subject3='is '
subject4='neha '
subject=subject1+subject2+subject3+subject4
#print(subject)

#slicing
subject1='my'
subject2='name'
subject3='is'
subject4='neha'
subject=subject1+subject2+subject3+subject4
#print(subject[0:6])

#print("Name" in subject)      #will get false
#print("name" in subject)      #will get true

#print("my" not in subject)

#print("\n prints \n")     #wherever \n present it leaves a line
#print(r"\n prints \n")    #keeping 'r' prints the entire statement


# %s string format
sub='maths'
part=1
#print("%s%d"%(sub,part))
#print("we have part %d of %s in first semester"%(part,sub))


#repeat(*) operator
#print(subject1*3,subject2*4,subject3*5,subject4*10)

#print((subject1+" ")*3)
#print(subject1.upper())
#print(subject2.lower())

sentence = "Neha is my name"
print(sentence)
print(sentence.split('m'))   #splits where the alphabet is there
