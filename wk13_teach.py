import math

def compute_square_area(side):
    square_area = side ** 2
    return square_area

def compute_rectangle_area(height, width):
    rectangle_area = height * width
    return rectangle_area

def compute_circle_area(radius):
    circle_area = math.pi * (radius ** 2)
    return circle_area

restart = True
while restart:
    shape = input('What is the shape for which you would like to know the area (square, rectangle, or circle)? Or type quite to exit. ' )

    if shape.lower() == 'square':
        side = float(input("What is the length of a side of the square? "))
        square_area = compute_square_area(side)
        print(f'The area of the square is: {square_area:.2f}')
        restart = True

    elif shape.lower() == 'rectangle':
        height = float(input('What is the height of the rectangle? '))
        width = float(input('What is the width of the rectangle? '))
        rectangle_area = compute_rectangle_area(height, width)
        print(f'The area of the rectangle is: {rectangle_area:.2f}')
        restart = True

    elif shape.lower() == 'circle':
        radius = float(input('What is the radius of the circle? '))
        circle_area = compute_circle_area(radius)
        print(f'The area of the circle is: {circle_area:.2f}')
        restart = True

    elif shape.lower() == 'quit':
        restart = False