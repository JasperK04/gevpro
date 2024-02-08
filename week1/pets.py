class Pet:

	def __init__(self, name):
		self.name = name

	def greeting(self):
		return f'I am {self.name}'

class Dog(Pet):

	def sound(self):
		return 'Woof'

	def greeting(self):
		return f'{self.sound()}, I am {self.name}'

class Cat(Pet):

   def sound(self):
	   return "Meow"

cat = Cat('Lord Purr')
dog = Dog('Peaches')
print(cat.greeting() +
dog.greeting())
print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
