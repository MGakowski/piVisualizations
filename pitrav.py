import turtle
import random
import time

start = time.time()
loadWindow = turtle.Screen()
my_turtle = turtle.Turtle()
turtle.bgcolor("#11303d")
turtle.colormode(255)
my_turtle.speed(0)
turtle.title("Pi Trav")
turtle.screensize(10000, 10000)

f = open('pimillion.txt', 'r')
pi = str(f.read())
count = int(0)
nox = int(pi[count])
#  print nox

m = int(5)

for i in range(1000000):

    # if i % 10000 == 0:
        # print(str(i)+":1 000 000")  # Helps track every 10000th step.
    my_turtle.ht()
    ang = nox*36
    #  print(str(nox) + "=nox, angle=" + str(ang))  # Show number on and angle.

    my_turtle.rt(ang)
    my_turtle.forward(m)
    my_turtle.lt(ang)
    count += 1
    nox = int(pi[count])
    if nox == 0:
        my_turtle.pencolor(int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))

end = time.time()
print(end - start)
turtle.exitonclick()
