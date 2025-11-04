from turtle import *
tracer(False)
m=20
screensize(4000,4000)
for i in range(2):
    fd(23*m)
    lt(90)
    bk(27*m)
    lt(90)
penup()
bk(5*m)
rt(90)
fd(11*m)
lt(90)
pendown()
for i in range(2):
    fd(26*m)
    rt(90)
    fd(32*m)
    rt(90)
penup()
for x in range(-10, 100):
    for y in range(-130, 11):
        goto(x * m, y * m)
        dot(3,'red')
update()
done()