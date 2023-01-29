import turtle


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_text = screen.textinput(title="Guess the state", prompt="What's another state name?")








screen.exitonclick()