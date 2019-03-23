# This program draws a square and a circle!

import turtle

#set up a window
window = turtle.Screen()
window.bgcolor("red")

# This function draws a square
def draw_square():
    
    
    #set up a brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(15) 
    
    for i in range(4):
        brad.forward(100)
        brad.right(90)
        i += 1

def draw_circle():
    #set up a pin
    pin = turtle.Turtle()
    pin.shape("arrow")
    pin.color("blue")
    pin.circle(100)


draw_square()
draw_circle()
window.exitonclick()
