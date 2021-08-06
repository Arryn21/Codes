import turtle
import time

b=time.time()
turtle.speed(30)

turtle.bgcolor("black")
turtle.hideturtle()

for i in range(1):
    for c in ("red","green","pink","orange"):
        turtle.color(c)
        turtle.pensize(2)
        turtle.lt(12)
        for i in range(10):
            turtle.fd(5)
            turtle.lt(150)
            turtle.rt(150)
            
turtle.Screen().bye()
#turtle.done()
e=time.time()
print(f"{e-b}")
