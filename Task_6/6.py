from turtle import *
screensize(4000, 4000)
tracer(False)
m=20
lt(30)
for i in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)
penup()
for x in range(-15,10):
    for y in range(-15, 10):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()