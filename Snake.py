import os
import turtle
import time
import random
import winsound

dela = 0.1

window = turtle.Screen()
window.title("Snake")
window.bgcolor("green")
window.setup(width= 800, height=600)
window.tracer(0)

score = 0
high_score = 0
#Snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction="stop"


#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

seggs = []

#Text
txt = turtle.Turtle()
txt.speed(0)
txt.color("blue")
txt.penup()
txt.hideturtle()
txt.goto(0, 260)
txt.write("Score:0  High Score:0", align="center", font=("Arial", 15, "normal"))

#Movement
def head_move():
    if head.direction == "up":
        y = head.ycor()
        y += 20
        head.sety(y)
    if head.direction == "down":
        y = head.ycor()
        y -= 20
        head.sety(y)
    if head.direction == "right":
        x = head.xcor()
        x += 20
        head.setx(x)
    if head.direction == "left":
        x = head.xcor()
        x -= 20
        head.setx(x)

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"
#keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

#Game
while True:
    window.update()

    # Collision

    if head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        winsound.PlaySound('C:/Users/Arymzn/OneDrive/Desktop/Projects/Snake/mi_explosion_03_hpx.wav', winsound.SND_ASYNC)
        for segments in seggs:
            segments.goto(1000, 1000)
        #Clearing Segments
        seggs.clear()
        score = 0
        txt.clear()
        txt.write("Score:{}  High Score:{}".format(score, high_score), align="center", font=("Arial", 15, "normal"))
    if head.distance(food) < 20:
        x = random.randint(-390, 390)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_s = turtle.Turtle()
        new_s.speed(0)
        new_s.shape("square")
        new_s.color("white")
        new_s.penup()
        seggs.append(new_s)
        winsound.PlaySound('C:/Users/Arymzn/OneDrive/Desktop/Projects/Snake/BiteAppleClosePers PE390101.wav', winsound.SND_ASYNC)

        score += 1
        if score > high_score:
            high_score = score
        txt.clear()
        txt.write("Score:{}  High Score:{}".format(score, high_score), align="center", font=("Arial", 15, "normal"))
    # Move segments in reverse order

    for i in range(len(seggs)-1, 0, -1):
        x = seggs[i - 1].xcor()
        y = seggs[i - 1].ycor()
        seggs[i].goto(x, y)
    
    # Move segment to the head

    if len(seggs) > 0:
        x = head.xcor()
        y = head.ycor()
        seggs[0].goto(x, y)

    head_move()

    #Head Collisions
    for seg in seggs:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            winsound.PlaySound('C:/Users/Arymzn/OneDrive/Desktop/Projects/Snake/mi_explosion_03_hpx.wav', winsound.SND_ASYNC)

            for segments in seggs:
                segments.goto(1000, 1000)
            #Clearing Segments
            seggs.clear()
            score = 0
            txt.clear()
            txt.write("Score:{}  High Score:{}".format(score, high_score), align="center", font=("Arial", 15, "normal"))


    time.sleep(dela)


window.mainloop()
