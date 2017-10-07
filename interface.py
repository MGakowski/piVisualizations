import tkinter
import turtle
import random
import time

window = tkinter.Tk()
window.title("Pi Trav settings")
window.geometry("300x330")
window.resizable(width=False, height=False)
window.configure(background="#11303D")
window.wm_iconbitmap('pico.ico')

def process():
    turtle.clearscreen()
    start = time.time()
    #loadWindow = turtle.Screen()
    my_turtle = turtle.Turtle()
    turtle.bgcolor("#11303d")
    turtle.colormode(255)
    my_turtle.speed(int(entSpeed.get()))
    turtle.title("Pi Trav")
    turtle.screensize(10000, 10000)

    f = open('pimillion.txt', 'r')
    pi = str(f.read())
    count = int(0)
    nox = int(pi[count])
    #  print nox

    m = int(entDist.get())

    for i in range(int(entSteps.get())):
        if nox == int(entColchange.get()):
            my_turtle.pencolor(int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
        # if i % 10000 == 0:
        # print(str(i)+":1 000 000")  # Helps track every 10000th step.
        my_turtle.ht()
        ang = nox * 36
        #  print(str(nox) + "=nox, angle=" + str(ang))  # Show number on and angle.

        my_turtle.rt(ang)
        my_turtle.forward(m)
        my_turtle.lt(ang)
        count += 1
        nox = int(pi[count])


    end = time.time()
    print("Time to complete, "+str(end - start)+" seconds.")
    turtle.exitonclick()

photo = tkinter.PhotoImage(file="pibg.gif")
img = tkinter.Label(window, image=photo)
img.pack()
lblSteps = tkinter.Label(window, text="How many digits of pi to step out?", fg="#FFFFFF", bg="#11303D")
entSteps = tkinter.Entry(window)
lblDist = tkinter.Label(window, text="Walk distance?", fg="#FFFFFF", bg="#11303D")
entDist = tkinter.Entry(window)
lblSpeed = tkinter.Label(window, text="Walking speed? (0=fast,1-9=slow)", fg="#FFFFFF", bg="#11303D")
entSpeed = tkinter.Entry(window)
lblColchange = tkinter.Label(window, text="Number to change colour on? (0-9)", fg="#FFFFFF", bg="#11303D")
entColchange = tkinter.Entry(window)

btn = tkinter.Button(window, text="Process", command=process, fg="#11303D", bg="#74D8CC")

lblSteps.pack()
entSteps.pack(pady=2)
lblDist.pack()
entDist.pack(pady=2)
lblSpeed.pack()
entSpeed.pack(pady=2)
lblColchange.pack()
entColchange.pack(pady=2)

btn.pack(pady=10)

window.mainloop()
