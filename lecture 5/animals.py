
class Animal:
  legs = 4

  def __init__(self, nm):
    self.name = nm

  def get_num_legs(self):
    return self.legs

  def greeting(self):
    return "cowers"

  def speak(self):
    return "grrr"

class Dog(Animal):

  def __init__(self, nm, br):
    super().__init__(nm)
    self.breed = br

  def greeting(self):
    return "wags"

  def speak(self):
    return 'woof'


class Cow(Animal):
  pass

class Bird(Animal):
  legs = 2
  def speak(self):
      return 'eek'

class Spider(Animal):
  legs = 8

class Snake(Animal):
  legs=0
  def greeting(self):
      return 'slides'
  def speak(self):
      return 'hiss'


class Labrador(Dog):
  def __init__(self, nm):
    super().__init__(nm, 'Labrador')

  def greeting(self):
    return super().greeting() + " enthusiastically"


d1 = Dog('Fido', 'Australian Shepherd')
c1 = Cow('Bessie')
b1 = Bird('Polly')
s1 = Spider('Charlotte')
l1 = Labrador('Air Bud')
s2 = Snake('Emily')

animals = [d1, c1, b1, s1, l1, s2]
for a in animals:
  print (a.name, 'has', a.get_num_legs(), 'legs and', a.greeting(), 'and says', a.speak())

if isinstance(d1, Animal):
  print("A dog is an animal")
else:
  print("A dog is not an animal")
