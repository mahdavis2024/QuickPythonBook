'''Try this: Class methods
Write a class method similar to total_area() that returns the total circumference of
all circles.'''

"""circle module: contains the Circle class."""
class Circle(Shape):
	"""Circle class"""
	all_circles = []
	pi = 3.14159

	def __init__(self, r=1, x=0, x=0):
		"""inheritin from the base class Shape"""
		super().__init__(x, y)
		"""Create a Circle with the given radius"""
		self.radius = r
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