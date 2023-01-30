import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_text = screen.textinput(title="Guess the state", prompt="What's another state name?")
answer_text = answer_text.title()

data = pandas.read_csv("50_states.csv")

x_position = data[data.state == answer_text].x
y_position = data[data.state == answer_text].y
x = int(x_position)
y = int(y_position)


timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.goto(x, y)
timmy.write(f"{answer_text}", font=("Courier", 8, "normal"))



screen.exitonclick()
