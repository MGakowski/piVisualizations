import turtle
import random

loadWindow = turtle.Screen()
my_turtle = turtle.Turtle()
turtle.bgcolor("#11303d")
turtle.colormode(255)
my_turtle.speed(0)

f = open('pimillion.txt', 'r')
pi = str(f.read())
count = int(0)
nox = int(pi[count])
print nox

m = int(5)

for i in range(1000000):
    my_turtle.ht()
    if nox == 1:
        my_turtle.rt(36)
        my_turtle.forward(m)
        my_turtle.lt(36)
        count += 1
        nox = int(pi[count])
        # print str("1 "+str(count)+":"+str(nox))
    if nox == 2:
        my_turtle.rt(72)
        my_turtle.forward(m)
        my_turtle.lt(72)
        count += 1
        nox = int(pi[count])
        # print str("2 " + str(count) + ":" + str(nox))
    if nox == 3:
        my_turtle.rt(108)
        my_turtle.forward(m)
        my_turtle.lt(108)
        count += 1
        nox = int(pi[count])
        # print str("3 " + str(count) + ":" + str(nox))
    if nox == 4:
        my_turtle.rt(144)
        my_turtle.forward(m)
        my_turtle.lt(144)
        count += 1
        nox = int(pi[count])
        # print str("4 " + str(count) + ":" + str(nox))
    if nox == 5:
        my_turtle.rt(180)
        my_turtle.forward(m)
        my_turtle.lt(180)
        count += 1
        nox = int(pi[count])
        # print str("5 " + str(count) + ":" + str(nox))
    if nox == 6:
        my_turtle.rt(216)
        my_turtle.forward(m)
        my_turtle.lt(216)
        count += 1
        nox = int(pi[count])
        # print str("6 " + str(count) + ":" + str(nox))
    if nox == 7:
        my_turtle.rt(252)
        my_turtle.forward(m)
        my_turtle.lt(252)
        count += 1
        nox = int(pi[count])
        # print str("7 " + str(count) + ":" + str(nox))
    if nox == 8:
        my_turtle.rt(288)
        my_turtle.forward(m)
        my_turtle.lt(288)
        count += 1
        nox = int(pi[count])
        # print str("8 " + str(count) + ":" + str(nox))
    if nox == 9:
        my_turtle.rt(324)
        my_turtle.forward(m)
        my_turtle.lt(324)
        count += 1
        nox = int(pi[count])
        # print str("9 " + str(count) + ":" + str(nox))
    if nox == 0:
        my_turtle.rt(0)
        my_turtle.forward(m)
        my_turtle.lt(0)
        my_turtle.pencolor(int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
        my_turtle.penup()
        # my_turtle.home()
        my_turtle.pendown()
        count += 1
        nox = int(pi[count])
        # print str("0 " + str(count) + ":" + str(nox))

turtle.exitonclick()
