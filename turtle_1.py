import turtle




atish_turtle = turtle.Turtle()


def atish():
    s = input("Enter 'q' to quit or any other key to continue: ")

    if s == "q":
        return s
    else:
        distance = int(input("Enter distance to move forward: "))
        degree = int(input("Enter degree to turn (0 for no turn): "))

        atish_turtle.forward(distance)
        atish_turtle.left(degree)

        atish()


if __name__ == "__main__":
    atish_turtle.speed(1)  # Set turtle speed
    atish()
    turtle.done()
