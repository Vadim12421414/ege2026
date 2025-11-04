from turtle import *
screensize(4000,4000)
m=20
tracer(False)
for i in range(3):
    fd(27*m)
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
for x in range(-10, 100):
    for y in range(-15, 15):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()


