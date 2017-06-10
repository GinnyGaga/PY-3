class TheThing(object):
	
	def __init__(self):#  #类内访问私有方法和特性.python默认情况下的方法和特性都是公有的，如果你想变为私有的，那么要在方法和特性的名字前加上双下划线.所以，你不可能完全限制其他人无法访问到你的类中方法和特性，所以，Python 并不能实现完全的封装.
		self.number=0
	
	def some_function(self):
		print("I got called.")
	
	def add_me_up(self,more):
		self.number += more
		return self.number

a=TheThing()
b=TheThing()

a.some_function()
b.some_function()

print(a.add_me_up(20))
print(a.add_me_up(20))
print(b.add_me_up(30))
print(b.add_me_up(30))

print(a.number)
print(b.number)

