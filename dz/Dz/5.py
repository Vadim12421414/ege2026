from turtle import *
screensize(3000, 3000)
tracer(False)
m=20
for i in range(5):
    fd(37*m)
    rt(90)
    fd(44*m)
    rt(90)
penup()
bk(18*m)
rt(90)
fd(29*m)
lt(90)
pendown()
for i in range(5):
    fd(31*m)
    rt(90)
    fd(35*m)
    rt(90)
penup()
for x in range(-10, 100):
    for y in range(-100, 25):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()