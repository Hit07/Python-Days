#Object oriented programming

from turtle import Turtle,Screen
from prettytable import PrettyTable
'''Importing a module which is already in-built in pycharm and
   from the module we import the class "Turtle()" which is pascal cased and
   creating an object by using an assingment operator'''
# tom = Turtle()
# tom.shape("turtle")
# tom.color("black","green")
# my_screen = Screen()
# # tom.circle(30)
# # while True:
# #     tom.forward(100)
# #     tom.left(90)
# my_screen.exitonclick()
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"],"c")
table.add_column("Type",["Electric","Water","Fire"],"c")
table.align = "l"
print(table)

