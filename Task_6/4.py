from turtle import *
tracer(False)
m=20
screensize(4000,4000)
for i in range(2):
    fd(28*m)
    rt(90)
    fd(18*m)
    rt(90)
penup()
fd(14*m)
rt(90)
fd(10*m)
lt(90)
pendown()
for i in range(2):
    fd(30*m)
    rt(90)
    fd(7*m)
    rt(90)
penup()
for x in range(-10, 100):
    for y in range(-130, 11):
        goto(x * m, y * m)
        dot(3,'red')
update()
done()