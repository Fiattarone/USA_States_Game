import turtle
from turtle import Turtle, Screen
import pandas
import csv

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

states_guessed = 0
guessed_states = {}
state_list = data["state"].to_list()

while states_guessed < 50:
    state_answer = screen.textinput(title=f"{states_guessed}/50 States Guessed Correctly", prompt="Name of the state?").title()
    # print(data["state"])
    # print(state_answer in data["state"].to_list())
    if state_answer in state_list and state_answer not in guessed_states:
        guessed_states[state_answer] = True
        # Write turtle object at x and y
        new_state = Turtle()
        new_state.penup()
        new_state.hideturtle()
        new_state_data = data[data["state"] == state_answer]
        new_state.goto(int(new_state_data.x), int(new_state_data.y))
        new_state.write(new_state_data.state.item())
        states_guessed += 1
    elif state_answer in guessed_states:
        print("Lol already guessed nub")
    elif state_answer == "Exit":
        break
    else:
        print(f"not in: {state_answer}" )

states_to_study = []
# with open("states_to_study.csv", "w") as study_file:
for x in state_list:
    if x not in guessed_states:
        states_to_study.append(x)

print(states_to_study)
new_data = pandas.DataFrame(states_to_study)
new_data.to_csv("states_to_study.csv")


screen.exitonclick()