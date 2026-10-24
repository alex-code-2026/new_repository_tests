def function(a):
	def wrapper(b):
		return (a + b) // 2
	return wrapper


f1 = function(10)
f2 = f1(20)
print(f2)
