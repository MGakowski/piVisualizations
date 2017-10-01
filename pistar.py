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

m = int(10)

pos1 = 0.00, 350.00
pos2 = 205.72, 283.16
pos3 = 332.87, 108.16
pos4 = 332.87, -108.16
pos5 = 205.72, -283.16
pos6 = 0.00, -350.00
pos7 = -205.72, -283.16
pos8 = -332.87, -108.16
pos9 = -332.87, 108.16
pos0 = -205.72, 283.16

for i in range(1000000):
    if i % 10000 == 0:
        print(str(i)+":1 000 000")
    my_turtle.ht()
    if nox == 1:
        my_turtle.goto(pos1)
        my_turtle.rt(18)
        my_turtle.forward(1)
        my_turtle.lt(18)
        pos1 = my_turtle.pos()
        count += 1
        nox = int(pi[count])
        # print str("1 "+str(count)+":"+str(nox))
    if nox == 2:
        my_turtle.goto(pos2)
        my_turtle.rt(54)
        my_turtle.forward(1)
        my_turtle.lt(54)
        pos2 = my_turtle.pos()
        count += 1
        nox = int(pi[count])
        # print str("2 " + str(count) + ":" + str(nox))
    if nox == 3:
        my_turtle.goto(pos3)
        my_turtle.rt(90)
        my_turtle.forward(1)
        my_turtle.lt(90)
        pos3 = my_turtle.pos()
        count += 1
        nox = int(pi[count])
        # print str("3 " + str(count) + ":" + str(nox))
    if nox == 4:
        my_turtle.goto(pos4)
        my_turtle.rt(126)
        my_turtle.forward(1)
        my_turtle.lt(126)
        pos4 = my_turtle.pos()
        count += 1
        nox = int(pi[count])
        # print str("4 " + str(count) + ":" + str(nox))
    if nox == 5:
        my_turtle.goto(pos5)
        my_turtle.rt(162)
        my_turtle.forward(1)
        my_turtle.lt(162)
        pos5 = my_turtle.pos()
        count += 1
        nox = int(pi[count])
        # print str("5 " + str(count) + ":" + str(nox))
    if nox == 6:
        my_turtle.goto(pos6)
        my_turtle.rt(198)
        my_turtle.forward(1)
        my_turtle.lt(198)
        pos6 = my_turtle.pos()
        count += 1
        nox = int(pi[count])
        # print str("6 " + str(count) + ":" + str(nox))
    if nox == 7:
        my_turtle.goto(pos7)
        my_turtle.rt(234)
        my_turtle.forward(1)
        my_turtle.lt(234)
        pos7 = my_turtle.pos()
        count += 1
        nox = int(pi[count])
        # print str("7 " + str(count) + ":" + str(nox))
    if nox == 8:
        my_turtle.goto(pos8)
        my_turtle.rt(270)
        my_turtle.forward(1)
        my_turtle.lt(270)
        pos8 = my_turtle.pos()
        count += 1
        nox = int(pi[count])
        # print str("8 " + str(count) + ":" + str(nox))
    if nox == 9:
        my_turtle.goto(pos9)
        my_turtle.rt(306)
        my_turtle.forward(1)
        my_turtle.lt(306)
        pos9 = my_turtle.pos()
        count += 1
        nox = int(pi[count])
        # print str("9 " + str(count) + ":" + str(nox))
    if nox == 0:
        my_turtle.goto(pos0)
        my_turtle.rt(342)
        my_turtle.forward(1)
        my_turtle.lt(342)
        pos0 = my_turtle.pos()
        my_turtle.pencolor(int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
        count += 1
        nox = int(pi[count])
        # print str("0 " + str(count) + ":" + str(nox))

turtle.exitonclick()
