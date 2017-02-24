# Practice declaring a class
class Circle:

# Apparently Python does not allow variable values to be changed upon initialization of instance, so constructor method is needed
	def _init_(self, radius = 0):
		self.radius = radius

# Apparently Python does not have an equivalent of attr_accessor, so need to create setter method
	def setRadius(self, radius):
		self.radius = radius

	def findArea(self):
		return 3.14 * (self.radius**2)

# Practice creating an instance of class and executing methods defined in it
circle = Circle()
circle.setRadius(3)
print circle.findArea()