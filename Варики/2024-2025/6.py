from turtle import *
screensize(3000, 3000)
tracer(False)
m=20
for i in range(6):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
penup()
fd(1*20)
rt(90)
fd(5*m)
lt(90)
pendown()
for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)
penup()
for x in range(-5, 100):
    for y in range(-100, 100):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
