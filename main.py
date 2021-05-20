# Create Turtle race, many turtles with different color
# instance inside object
# Positional arguments : def my_function(a,b,c)
import turtle
from turtle import Turtle, Screen

import random

# tim = Turtle() : moved down

is_race_on = False     #  this let user keep betting when the race is ON
screen = Screen()

screen.setup(width=500, height=400)  # positional argument : x=500, y = 400



# turtle.textinput(title, prompt) : title(string), prompt(string)-->pop up a dialog window for input of string
user_bet = screen.textinput(title="Make your bet", prompt=" Which turtle will win the race ? Enter a color :")

print(user_bet)

new_turtle = Turtle()
# the Method: turtle.goto(x, y =None). if height =400 : from middle (0,0)- go up : +200, go down = -200
# turtle.goto(x, y =None). if width =500 : from middle (0,0)- go right : +250, go left = -250
colors = ["red","brown","orange","yellow","green","pink","blue","purple","black"]    # 6 colors for 6 turtles
# 6 turtles at the same position at x, but y is different :
y_positions = [-120,-90,-40,-10, 20, 50,90,130,170]

# Make an empty list of turtles at beginning, then use Append (added turtles to this list later :
all_turtles = []

# use For Loop to go through the array Color :
for turtle_index in range(0, 9):     # if color = 9, y =9---> range from 0 to 9

   # create new turtle (instance) or object of Turtle below has different states (color,speed :
   new_turtle = Turtle(shape="turtle")     #  pass one parameter appearance : 'shape' of the turtle
   new_turtle.penup()               # this method : no drawing when the turtle move
   new_turtle.color(colors[turtle_index])     # this method gives 6 colors to 6 turtles
# tim.goto(x=-250, y=-100)  # if x =-250, the turtle rans out of the screen, so x =-230
  #tim.goto(x=-250, y=-100) if  y position = 100--> 6 turtles start at the same position, so :

   new_turtle.goto(x=-230, y=y_positions[turtle_index])    # position y to pass the turtle index of each item of the array

 # Now, use Append to add new turtles to  empty all_turtles above :
   all_turtles.append(new_turtle)
  # tim.shape("turtle")  # change the turtle appearance at your own preference

#Create a random of numbers from 0 to 10 for any turtle move forward, and repeat it many time :


if user_bet :
  is_race_on = True   # different from False---> the race is ON

while is_race_on:

    for turtle in all_turtles:  # this For Loop for the moving of each turtle in all_turtle

        # use method xcor() to set up the finished line value for each turtle at 230 (250 is the length of +x) :
        # If any turtle reaches the finished line, the race stops :

        if turtle.xcor() > 230:
            is_race_on = False   # this is the same declared at beginning, the game stops !
            winning_color = turtle.pencolor()   # the method pencolor(r,g,b) give the color for each turtle
            if winning_color == user_bet :
                print(f" You've won ! The {winning_color} turtle is the winner !")
            else :
                print(f" You've lost ! The {winning_color} turtle is the winner !")


        rand_distance = random.randint(0,10)   # the length of the race road
        turtle.forward(rand_distance)


screen.exitonclick()
