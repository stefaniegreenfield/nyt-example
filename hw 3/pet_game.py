from random import randrange

class Pet:
    boredom_decrement = -4
    hunger_decrement = -4
    boredom_threshold = 6
    hunger_threshold = 10
    age=0

    def __init__(self, name="Coco"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.words=['hello']

    def clock_tick(self):
        self.hunger+=2
        self.boredom+=2
        self.age+=1

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

class Dog(Pet):
    def __str__(self):
        state = "I'm " + self.name + ", arrrf! "
        state += 'I feel ' + self.mood() + ", arrrf! "
        if self.mood() == 'hungry':
            state += 'Feed me , arrrf!'
        if self.mood() == 'bored':
            state += 'You can teach me new words, arrrf!'
        return state
    def clock_tick(self):
        self.hunger+=2
        self.boredom+=2
        self.age+=2

class Cat(Pet):
    def __init__(self,name, meow_count):
        super().__init__(name)
        self.meow_count=meow_count
    def hi(self):
        print(self.words[randrange(len(self.words))]*self.meow_count)
    def clock_tick(self):
        self.hunger+=2
        self.boredom+=2
        self.age+=3

class Poodle(Dog):
    def dance(self):
        return "Dancing in circles like poodles do!"
    def say(self):
        print(self.dance())
        super().say()

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

pet_types = {'dog': Dog, 'poodle': Poodle, 'cat': Cat}
def whichtype(adopt_type="general pet"):
    return pet_types.get(adopt_type.lower(), Pet)

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                # figure out which class it should be
                if len(words) > 2:
                    Cl = whichtype(words[2])
                else:
                    Cl = Pet
                # Make an instance of that class and append it
                animals.append(Cl(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()

        younglings = []
        for each_animal in animals:
            if each_animal.age <= 18:
                younglings.append(each_animal)
        animals=younglings

        if len(younglings) == 0:
            if input("Type 'again' or 'exit'") == "exit":
                break

play()
