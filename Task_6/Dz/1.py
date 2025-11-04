from turtle import *

screensize(5000, 5000)
tracer(False)
m=20
for i in range(3):
    fd(7*m)
    rt(90)
    fd(12*m)
    rt(90)
penup()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
pendown()
for i in range(4):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
penup()
for x in range(-110, 10):
    for y in range(-25, 110):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()