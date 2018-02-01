'''
SI 206 W18 Homework03: Classes and Inheritance

Your discussion section: 004
People you worked with:

######### DO NOT CHANGE PROVIDED CODE ############
'''

#######################################################################
#---------- Part 1: Class
#######################################################################

'''
Task A
'''
from random import randrange
class Explore_pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state

coco = Explore_pet()
coco.hunger=6
coco.boredom=7
print (coco)

brian= Explore_pet("Brian")
brian.hunger=12
print (brian)

#your code begins here . . .

'''
Task B
'''
#For task B, add your code inside the Pet class
class Pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.words=['hello']

    def clock_tick(self):
        self.hunger+=2
        self.boredom+=2

    def say(self):
        print ("I know how to say")
        for word in self.words:
            print (word)

    def teach(self,word):
        self.words.append(word)
        self.boredom+=self.boredom_decrement
        if self.boredom<0:
            self.boredom=0

    def feed(self):
        self.hunger+=self.hunger_decrement
        if self.hunger<0:
            self.hunger=0

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. '
        if self.mood() == 'hungry':
            state += 'Feed me.'
        if self.mood() == 'bored':
            state += 'You can teach me new words.'
        return state

    def hi(self):
        print(self.words[randrange(len(self.words))])

'''
Task C
'''

def teaching_session(my_pet,new_words):
    for word in new_words:
        my_pet.teach(word)
        my_pet.hi()
        print(my_pet)
        if my_pet.mood()=='hungry':
            my_pet.feed()
        my_pet.clock_tick()

stefanie= Pet('Stefanie')
teaching_session(stefanie, ['I am sleepy', 'You are the best','I love you, too'])






#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################
'''
Task A: Dog and Cat
'''
class Dog(Pet):
    def __str__(self):
        state = "I'm " + self.name + ", arrrf! "
        state += 'I feel ' + self.mood() + ", arrrf! "
        if self.mood() == 'hungry':
            state += 'Feed me , arrrf!'
        if self.mood() == 'bored':
            state += 'You can teach me new words, arrrf!'
        return state

class Cat(Pet):
    def __init__(self,name, meow_count):
        super().__init__(name)
        self.meow_count=meow_count
    def hi(self):
        print(self.words[randrange(len(self.words))]*self.meow_count)

'''
Task B: Poodle
'''
class Poodle(Dog):
    def dance(self):
        return "Dancing in circles like poodles do!"
    def say(self):
        print(self.dance())
        super().say()
print()
stefanie= Poodle('stefanie')
stefanie.say()
print()
alexa= Cat('alexa',8)
alexa.hi()
