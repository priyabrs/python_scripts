from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake game')
    screen.tracer(0)

    snake = Snake('green')
    food = Food('red')
    scoreboard = ScoreBoard()

    def reset_game():
        scoreboard.reset_scoreboard()
        snake.reset_snake()
        

    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    screen.onkey(screen.bye, 'n')
    

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect collision with food:
        if snake.head.distance(food) < 15:
            food.reset_food()
            scoreboard.increase_score()
            snake.extend_snake()
        
        #Detect collision with wall:
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
            # scoreboard.game_over()
            reset_game()
            # screen.onkey(reset_game, 'y')

        #Detect Collision with body:
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                reset_game()
                # screen.onkey(reset_game, 'y')


    screen.exitonclick()
    scoreboard.set_highscore(game_end=True)

if __name__ == '__main__':
    main()