import turtle
from random import random, randint
import time

# create a window


# countdown


CURSOR_SIZE = 20

num = 0


def increase_score():
    global num
    num += 1


def my_turtle():
    radius = 25
    enes = turtle.Turtle('turtle', visible=False)
    enes.color("green")
    enes.shapesize(radius / CURSOR_SIZE)
    enes.penup()

    while True:
        nx = randint(2 * radius - width // 2, width // 2 - radius * 2)
        ny = randint(2 * radius - height // 2, height // 2 - radius * 2)

        enes.goto(nx, ny)

        for other_radius, other_circle in circles:
            if enes.distance(other_circle) < 2 * max(radius, other_radius):
                break
        else:
            break

    enes.showturtle()
    click = False
    enes.onclick(lambda x, y, t=enes, : (enes.hideturtle(), increase_score()))

    return radius, enes



screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Speed Clicker")

width, height = screen.window_width(), screen.window_height()

circles = []

gameLength = 20
# Higher number means faster blocks
# 1-10
difficulty = 10
startTime = time.time()
while True:
    time.sleep(1 / difficulty)

    timeTaken = time.time() - startTime
    circles.append(my_turtle())
    screen.title('SCORE: {}, TIME LEFT: {}'.format(num, int(round(gameLength - timeTaken, 0))))

    if time.time() - startTime > gameLength:
        break

screen.title('FINISHED! FINAL SCORE: {}'.format(num))



# an instance of turtle
'''
enes = turtle.Turtle()
enes.shape("turtle")
enes.color("green")
enes.shapesize(1.5, 1.5, 3)
'''
turtle.mainloop()
