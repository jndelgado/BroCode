# snake
# game
# yeet

import turtle
import time
import random

delay = 0.08

# Score
score = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.title("Snake game by Mateo")
wn.bgcolor("green")
wn.setup(width=500, height=500)
wn.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("darkblue")
head.penup()
head.goto(-100,0)
head.direction = "stop"

# Apple
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(100,0)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.ht()
pen.goto(0, 215)
pen.write("Score: 0   High Score: 0", align="center", font=("Courier", 20, "normal"))

# Fuctions
def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_up():
    if head.direction != "down":
        head.direction = "up"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()
    # Border collision
    if head.xcor()>250 or head.ycor()>250 or head.ycor()<-250 or head.xcor()<-250:
        time.sleep(1)
        head.goto(-100,0)
        head.direction = "stop"
        apple.goto(100,0)

        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments list
        segments.clear()
        
        # Reset the score
        score = 0

        pen.clear() 
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("courier", 20, "normal"))


    # Check for a collision with the food 
    if head.distance(apple) < 20:
        # Move apple to random spot on screen
        x = random.randint(-235, 235)
        y = random.randint(-235, 235)
        apple.goto(x,y)

        # Add a segment 
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        # Increasse the score
        score += 1

        if score > high_score:
            high_score = score

        pen.clear() 
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("courier", 20, "normal"))

    # Move the end sgment first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segments 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(-100,0)
            head.direction = "stop"
            apple.goto(100,0)

            # Hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            pen.clear() 
            pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("courier", 20, "normal"))

    time.sleep(delay)

wn.mainloop()