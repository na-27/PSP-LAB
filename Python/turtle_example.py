'''
# making a star
import turtle                    
ws=turtle.Screen()
ws.bgcolor("lightblue")
clr=["white","pink","blue","purple","yellow"]

amy=turtle.Turtle()
amy.pensize(6)

amy.speed(3)
for i in range(5):
    amy.pencolor(clr[i])
    amy.forward(300)
    amy.right(144)
'''







#random design
import turtle                    
ws=turtle.Screen()
ws.bgcolor("black")
clr=["red","orange","yellow","green","blue","indigo"]

amy=turtle.Turtle()
amy.pensize(3)
amy.speed(0)
for i in range(360):
    amy.pencolor(clr[i%6])
    amy.width(i/100+1)
    amy.forward(i)
    amy.left(59)

'''
#writing name
import turtle
ws=turtle.Screen()
ws.bgcolor("lightblue")

turtle.color('purple')
style = ('Helvetica', 60, 'italic')
turtle.write('Neha', font=style, align='center')
turtle.hideturtle()
'''

