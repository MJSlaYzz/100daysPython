import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")

# save the image path to a variable
image_path = "workingWithCSVData/us-states-game/blank_states_img.gif"

# add the image shape to the turtle shapes list
screen.addshape(image_path)

# change the shape of the turtle to the image
turtle.shape(image_path)
screen.setup(width = 725, height = 491)

# a way to obtain X and Y coordinations of states:
# def get_mouse_click_coordinations(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coordinations)
# turtle.mainloop()

guessed_state_count = 0
guessed_list = []
lives = 3
while True:
    answer_state = screen.textinput(title= f"Guess the State {guessed_state_count}/50", prompt= f"What's another state's name?  \nlives: {lives}").title()
    states_data = pandas.read_csv("workingWithCSVData/us-states-game/50_states.csv")
    if answer_state in states_data.state.to_list():
        if  answer_state not in guessed_list:
            state_row = states_data[states_data["state"] == answer_state]
            # x_position = state_row["x"].to_list()[0]
            # y_position = state_row["y"].to_list()[0]
            # print(f"x= {x_position} y= {y_position}")
            tur = turtle.Turtle()
            tur.hideturtle()
            tur.penup()
            # tur.goto(x_position, y_position)
            tur.goto(int(state_row.x), int(state_row.y))
            #tur.write(arg= answer_state, align= "center", font=("Arial", 6, "bold"))
            tur.write(arg= state_row.state.item(), align= "center", font=("Arial", 6, "bold"))
            print("True")
            guessed_state_count += 1
            guessed_list.append(answer_state)
        else:
            print("Already guessed that state before")
    else:
        print("False")
        lives -=1

    if guessed_state_count >= 50 or lives <= 0 or answer_state == "Exit":
        if lives <= 0 or answer_state == "Exit":
            # create a list of states that player missed:
            # on day 25
            # list_of_missed_states = []
            # for state in states_data.state.to_list():
            #     if state not in guessed_list:
            #         list_of_missed_states.append(state)
            # data = pandas.DataFrame(list_of_missed_states)
            # data.to_csv("workingWithCSVData/us-states-game/missed_states.csv")

            # on day 26
            list_of_missed_states = [state for state in states_data.state.to_list() if state not in guessed_list]
            data = pandas.DataFrame(list_of_missed_states)
            data.to_csv("workingWithCSVData/us-states-game/missed_states.csv")
        break
   

    



