import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# GAME VARIABLES:
count = 0
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_text = screen.textinput(title=f"{count}/50 Correct guesses.", prompt="What's another state name?")
    answer_text = answer_text.title()
    if answer_text == "Exit":
        break
    if answer_text in states:
        guessed_states.append(answer_text)
        count += 1
        state_data = data[data.state == answer_text]
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(int(state_data.x),int(state_data.y))
        timmy.write(f"{state_data.state.item()}", font=("Courier", 8, "normal"))

missing_states = [state for state in states if state not in guessed_states]


missing_data = pandas.DataFrame(missing_states)
missing_data.to_csv("Missing_states.csv")
