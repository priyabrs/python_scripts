import turtle
import pandas as pd
screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

state_df = pd.read_csv('50_states.csv')
ans_count = 0
ans_states = []
no_of_states = state_df.shape[0]
while len(ans_states) < 50: 
        # print(f'{ans_count}/{no_of_states}')
        answer_state_unformatted = screen.textinput(title=f'{ans_count}/{no_of_states} States correct',prompt='Enter the state name')
        answer_state = answer_state_unformatted.title()
        if  answer_state == 'Exit':
            missing_states_df = pd.DataFrame(set(state_df.state.to_list()) - set(ans_states), columns=['state'])
            missing_states_df.to_csv('States_to_learn.csv')
            break
        if answer_state in list(state_df['state']):
            ans_count += 1
            ans_states.append(answer_state)
            state_xcor = int(state_df[state_df.state == answer_state].x)
            state_ycor = int(state_df[state_df.state == answer_state].y)
            stt = turtle.Turtle()
            stt.penup()
            stt.hideturtle()
            stt.goto(state_xcor, state_ycor)
            stt.write(f'{answer_state}', False, align = 'center') 
# screen.exitonclick()