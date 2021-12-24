import turtle
import random
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
colors = ['red', 'blue', 'green', 'pink', 'yellow', 'orange']
def draw_lines(l, c):
    for value in l:
        turtle.forward(value)
        turtle.pencolor(random.choice(c))
        (turtle.stamp())
        turtle.backward(value)
        turtle.right(40)

draw_lines(list1, colors)