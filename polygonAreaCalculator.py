"""
In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit
methods and attributes.

Rectangle class
When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:
    - set_width
    - set_height
    - get_area: Returns area (width * height)
    - get_perimeter: Returns perimeter (2 * width + 2 * height)
    - get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
    - get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line
      should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string:
      "Too big for picture.".
    - get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape
      (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)

Square class

The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The __init__ method should store the side length
in both the width and height attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string,
it should look like: Square(side=9)

Additionally, the set_width and set_height methods on the Square class should set both the width and height.

Usage example:

rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

That code should return:

50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
"""

class Rectangle:
    width=0
    height=0

    def __init__(self, width, height):
        self.width=width
        self.height=height
    def __str__(self):
        return('Rectangle(width='+str(self.width)+', height='+str(self.height)+')')
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        area=self.width*self.height
        return area
    def get_perimeter(self):
        perimeter=2*(self.width+self.height)
        return perimeter
    def get_diagonal(self):
        diagonal=(self.width**2+self.height**2)**0.5
        return diagonal
    def get_picture(self):
        pictureStr=''
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        else:
            for i in range(self.height):
                pictureStr=pictureStr+'*'*self.width+'\n'
        return pictureStr
    def get_amount_inside(self,shape):
        if shape.width>self.width or shape.height>self.height:
            return 0
        else:
            return int(((self.width-self.width%shape.width)/shape.width)*((self.height-self.height%shape.height)/shape.height))

class Square(Rectangle):
    def __init__(self,sideLength):
        self.width=sideLength
        self.height=sideLength
    def __str__(self):
        return 'Square(side='+str(self.width)+')'
    def set_side(self, sideLength):
        self.width=sideLength
        self.height=sideLength
    def set_width(self, sideLength):
        self.width=sideLength
        self.height=sideLength
    def set_height(self, sideLength):
        self.width=sideLength
        self.height=sideLength



test=Square(3)
print(test.get_picture())
test.set_side(2)
print(test.get_picture())
test.set_width(4)
print(test.get_picture())
test.set_height(5)
print(test.get_picture())
print(test)






#test=Rectangle(16,8)
#test2=Rectangle(4,4)
#test3=test.get_amount_inside(test2)
#print(test3)
#print(test)