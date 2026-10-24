def function(a):
	def wrapper(b):
		return (a + b) // 2
	return wrapper


f1 = function(10)
f2 = f1(20)
print(f2)

class Point:

	def __init__(self, a, d):
		self.a = a
		self.d = d

	def get_coord(self):
		return self.a, self.d

pt = Point(100, 500)
print(pt.get_coord())
