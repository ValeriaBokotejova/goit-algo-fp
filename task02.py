import turtle

def draw_pythagoras_tree(t, branch_length, level):
    
    if level > 0:
        t.forward(branch_length) 
        t.left(45)
        draw_pythagoras_tree(t, branch_length * 0.7, level - 1)
        t.right(90)
        draw_pythagoras_tree(t, branch_length * 0.7, level - 1)
        t.left(45)
        t.backward(branch_length)

def main():

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Pythagoras Tree")
    screen.bgcolor("#ECFFFF")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("green")
    t.pensize(3)
    t.hideturtle()
    
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)
    
    level = int(turtle.numinput("Pythagoras Tree", "Enter the recursion level:", minval=1, maxval=10))
    
    draw_pythagoras_tree(t, 150, level)
    
    turtle.done()

if __name__ == "__main__":
    main()