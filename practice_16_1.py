from Practice_16 import Rectangle, Square, Circle
r1 = Rectangle(10, 5)
r2 = Rectangle(12, 10)


# print(r1.get_area(), r2.get_area())

square_1 = Square(5)
square_2 = Square(10)

# print(square_1.get_area_square(),
#       square_2.get_area_square())

rad = Circle(125)
# print(rad.get_area_circle())


figures = [r1, r2, square_1, square_2, rad]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())
