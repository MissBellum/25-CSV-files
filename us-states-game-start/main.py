from turtle import Turtle, Screen

import pandas

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = pandas.read_csv("50_states.csv")
score = 0

states_list = all_states.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answers = screen.textinput(title=f"Score: {len(guessed_states)}/50 States Correct",
                               prompt="What's another state's name?").title()
    states_cor = all_states[all_states.state == f"{answers}"]
    print(states_cor.x)
    if answers == "Exit":
        missing_states = [state for state in all_states.state if state not in guessed_states]
        # missing_states.append(missing_states)
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv("states to learn")
        break
    if answers in states_list:
        guess = Turtle()
        guess.hideturtle()
        guess.penup()
        guess.goto(x=int(states_cor.x), y=int(states_cor.y))
        guess.write(states_cor.state.item())  # gets first item of data series
        score += 1
        guessed_states.append(answers)
print(guessed_states)
