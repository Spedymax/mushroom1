import turtle

def draw_pixel(t, size):
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_heart(t, pixel_size):
    heart = [
        "   ____   ____  ",
        "  _****___****_ ",
        " _******_******_",
        "_***************_",
        "_***************_",
        " _*************_",
        " _*************_",
        "  _***********_ ",
        "   _*********_  ",
        "    _*******_   ",
        "     _*****_    ",
        "      _***_     ",
        "       _*_      ",
        "        _       "
    ]

    t.penup()
    start_x = -(len(heart[0]) * pixel_size) / 2
    start_y = (len(heart) * pixel_size) / 2

    for y, row in enumerate(heart):
        for x, pixel in enumerate(row):
            t.goto(start_x + x * pixel_size, start_y - y * pixel_size)
            if pixel == "*":
                t.color("black", "red")
                draw_pixel(t, pixel_size)
            elif pixel == "_":
                t.color("black", "black")
                draw_pixel(t, pixel_size)

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Pixelated Heart")
screen.bgcolor("white")

# Create and set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.hideturtle()

# Draw the heart
draw_heart(t, 25)

# Exit on click
screen.exitonclick()