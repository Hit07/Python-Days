import random
import turtle
from turtle import Turtle,Screen
color_list = ["violet","purple","blue","pink","orange","green","yellow","brown"]
# def move(i):
#     speed = random.randint(1, 10)
#     i.forward(speed)

screen = Screen()
screen.setup(width=500,height=400)
input_1 = screen.textinput("Guess","Who will win the race?Enter the color:")
j = 0
participants = []
for i in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(random.choice(color_list))
    new_turtle.penup()
    new_turtle.goto(-230,-100+j)
    j += 30
    participants.append(new_turtle)

if input_1:
    race_on = True
    while race_on:
        for i in participants:
            if i.xcor() > 240.00:
                race_on = False
                if i.pencolor() == input_1:
                    print(f"You win😁.The winning turtle color:{i.pencolor()}")
                    break
                else:
                    print(f"You lose😓.The winning turtle color:{i.pencolor()}")
                    break
            else:
                speed = random.randint(1, 10)
                i.forward(speed)























screen.exitonclick()
