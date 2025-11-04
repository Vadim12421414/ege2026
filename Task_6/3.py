from turtle import *
tracer(False)
m=20
screensize(5000,5000)
for i in range(8):
    fd(16*m)
    rt(90)
    fd(22*m)
    rt(90)
penup()
bk(5*m)
rt(90)
fd(5*m)
lt(90)
pendown()
for i in range(8):
    fd(52*m)
    rt(90)
    fd(77*m)
    rt(90)
penup()
for x in range(-10, 100):
    for y in range(-130, 11):
        goto(x * m, y * m)
        dot(10,'white')
update()
done()