'''Try this-1: Instance Variables
What code would you use to create a Rectangle class?'''
'''Try this-2: Instance variables and Methods
Update the code for a Rectangle class so that you can set the dimensions when an
instance is created, just as for the Circle class above. Also, add an area() method.'''
'''Try this-3: Class methods
Write a class method similar to total_area() that returns the total circumference of
all circles.'''
'''Try this-4: Inheritance
Rewrite the code for a Rectangle class to inherit from Shape. Because squares and
rectangles are related, would it make sense to inherit one from the other? If so, which
would be the base class, and which would inherit?
How would you write the code to add an area() method for the Square class? Should
the area method be moved into the base Shape class and inherited by circle, square,
and rectangle? If so, what issues would result?'''
'''Try this-5: Private instance variables
Modify the Rectangle class’s code to make the dimension variables private. What
restriction will this modification impose on using the class?'''
'''Try this-6: Properties
Update the dimensions of the Rectangle class to be properties with getters and
setters that don’t allow negative sizes.'''


class Shape:
	""" parent class defining any shape with coordinates and moving function"""
	def __init__(self, x, y):
		"""defining x and y coordinates for any shape"""
		self.x = x
		self.y = y
	def move(self, delta_x, delta_y):
		"""defining movement as change of coordinates"""
		self.x = self.x + delta_x
		self.y = self.y + delta_y

class Circle(Shape):
	"""Circle class inheriting from Shape"""
	all_circles = []
	pi = 3.14159

	def __init__(self, rad=1, x=0, y=0):
		"""inheritin from the base class Shape"""
		super().__init__(x, y)
		"""Creates a Circle with the given radius"""
		self.radius = rad
		self.__class__.all_circles.append(self) 

	def area(self):
		"""determine the area of the Circle"""
		return self.__class__.pi * self.radius * self.radius

	def circumference(self):
		return 2 * self.radius * Circle.pi

	@classmethod 
	def total_area(cls): 
		total = 0
		for c in cls.all_circles: 
			total = total + c.area()
		return total

	@classmethod 
	def total_circ(cls): 
		"""class method to total the circumference of all circles created """
		total = 0
		for c in cls.all_circles: 
			total = total + c.circumference()
		return total

class Rectangle(Shape):
	"""Rectangle class inhering from Shape"""
	def __init__(self, arg1=1, arg2=2, x=0, y=0):
		"""assigning measurment for two sides of the rectangle"""
		super().__init__(x, y)
		self.__height = arg1
		self.__width = arg2

"""making hieght and width variables private is by using double underscores before their name.
it makes them safe from name clash and accidental change in other programs.
however there's no way to access private variables from instance attributes. 
unless explicitally prepended by class name.
Or there should be getter and setter defined for them with @property decorator."""

		@property
		def height(self):
			return self.__height

		@height.setter
		def height(self, value):
			if value <= 0:
				raise ValueError('Height must be a positive number.')
			self.__height = value

		@property
		def width(self):
			return self.__width

		@width.setter
		def width(self, value):
			if value <= 0:
				raise ValueError('Width must be a positive number.')
			self.__width = value		

		
	def area(self):
		"""calculating the area of rectangle"""
		return self.__height * self.__width

	def perimeter(self):
		"""calculating the perimeter of ractangle"""
		return 2*self.__height + 2*self.__width

"""it makes sense for square class to ingerit from rectangle class,
as it is just a rectangle with both sides the same size.
the area method can be ingerited by square from regtangle but it cannot be put into
shape class and be inherited by circle class, 
because the formula for the area of a circle is different and not the same as rectangle."""

class Square(Rectangle): 
	def __init__(self, arg=1):
		self.arg1 = arg
		self.arg2 = arg
		Rectangle.__init__(self, self.arg1, self.arg2)

	
#testing Rectangle class
rec = Rectangle(2,3)
print(rec.area())
print(rec.perimeter())
rec.move(5,5)
print((rec.x,rec.y))


#testing Square class
squ = Square(2)
print(squ.area())
print((squ.x,squ.y))


