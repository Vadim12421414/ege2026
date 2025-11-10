from turtle import *
screensize(3000, 3000)
tracer(False)
m=20
lt(90)
for i in range(7):
    rt(45)
    fd(11*m)
    rt(45)
penup()
for x in range(-10, 100):
    for y in range(-100, 25):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()