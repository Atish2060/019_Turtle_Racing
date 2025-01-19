import random
from turtle import Turtle, Screen
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
initial_pos = [-100, -60, -20, 20, 60, 100]
turtle_list = []
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title= "Make your Bet", prompt= "Which of the seven turtle"
                                                              " will win the race? ")
is_race_on = False
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-240, y=initial_pos[i])
    turtle_list.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:

    for turtle_no in turtle_list:
        random_speed = random.randint(0, 10)
        turtle_no.forward(random_speed)

        if turtle_no.xcor() > 230:
            if turtle_no.pencolor() == user_input.lower():
                print(f"You have won!! {turtle_no.pencolor()} has won.")
            else:
                print(f"You have lost!! {turtle_no.pencolor()} has won instead of {user_input}")
            print("Game ends!! Thank You for playing.")
            is_race_on = False


screen.exitonclick()
