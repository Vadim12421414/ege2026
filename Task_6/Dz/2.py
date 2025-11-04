from turtle import *

screensize(5000, 5000)
tracer(False)
m=20
for i in range(4):
    fd(19*m)
    rt(90)
    fd(30*m)
    rt(90)
penup()
fd(2*m)
rt(90)
fd(8*m)
lt(90)
pendown()
for i in range(4):
    fd(93*m)
    rt(90)
    fd(97*m)
    rt(90)
penup()
for x in range(-10, 100):
    for y in range(-130, 11):
        goto(x * m, y * m)
        dot(3,'red')
update()
done()