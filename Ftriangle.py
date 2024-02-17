import turtle

turtle.tracer(False)

def R():
    turtle.right(60)
def F(l, n):
    if n == 0:
        turtle.forward(l)
        return

    F(l/2, n - 1)
    R()
    F(l/2, 0)
    turtle.left(180)
    F(l/2, n - 1)
    R();R()
    F(l/2, n - 1)

l = 100
n = 4
F(l,n)
R()
R()
F(l,n)
R()
R()
F(l,n)
turtle.update()
turtle.mainloop()
