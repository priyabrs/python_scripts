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

    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

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
            scoreboard.game_over()
            game_on = False

        #Detect Collision with body:
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                scoreboard.game_over()


    screen.exitonclick()

if __name__ == '__main__':
    main()