from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.title("My Snaka Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
food=Food()
scoreboard=Scoreboard()


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.segments[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        game_is_on = False
        scoreboard.game_over()











screen.exitonclick()
