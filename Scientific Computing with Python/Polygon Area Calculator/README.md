# Shape Classes: Rectangle and Square

## Rectangle Class

The `Rectangle` class represents a rectangle shape and provides methods to calculate its properties:

- `__init__(self, width, height)`: Initializes a rectangle with the specified width and height.
- `set_width(self, width)`: Sets the width of the rectangle.
- `set_height(self, height)`: Sets the height of the rectangle.
- `get_area(self)`: Returns the area of the rectangle.
- `get_perimeter(self)`: Returns the perimeter of the rectangle.
- `get_diagonal(self)`: Returns the length of the diagonal of the rectangle.
- `get_picture(self)`: Returns a string representation of the rectangle using asterisks.
- `get_amount_inside(self, shape)`: Calculates the maximum number of smaller shapes that can fit inside the rectangle.
- `__str__(self)`: Returns a string representation of the rectangle's dimensions.

## Square Class (Subclass of Rectangle)

The `Square` class is a subclass of `Rectangle` and represents a square shape. It inherits most of its methods from the `Rectangle` class:

- `__init__(self, side)`: Initializes a square with the specified side length.
- `set_side(self, side)`: Sets the side length of the square.
- `set_width(self, width)`: Overrides the `set_width` method to set both width and height as the same side length.
- `set_height(self, height)`: Overrides the `set_height` method to set both width and height as the same side length.
- `get_picture(self)`: Returns a string representation of the square using asterisks, respecting the maximum width constraint.
- `__str__(self)`: Returns a string representation of the square's side length.

## Key Features

- **Rectangle and Square Calculation:** Both classes provide methods to calculate various properties of rectangles and squares.
- **Inheritance:** The `Square` class inherits methods from the `Rectangle` class, while also adding specialized methods for squares.
- **String Representation:** The `__str__` method allows easy printing of the rectangle's or square's dimensions.

## Learning Outcomes

Working with the `Rectangle` and `Square` classes enhanced my skills in:

- **Object-Oriented Programming:** I learned how to design classes that represent geometric shapes and inherit properties from each other.
- **Method Overriding:** I practiced overriding methods in subclasses to tailor them to specific requirements.
- **Calculation and Geometry:** I gained experience in calculating area, perimeter, diagonal, and other geometric properties.

Happy coding! 💻🚀
