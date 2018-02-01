class Library():

    def __init__(self, days_remaining = 0, checked_out = False):
        self.days_remaining = days_remaining
        self.checked_out = checked_out
        self.type = "Misc. Media"

    def clock_tick(self):
        self.days_remaining -= 1

    def checkout(self):
        if self.checked_out == True:
            print("Already checked out")
        else:
            self.checked_out = True
            return True

    def item_return(self):
        if self.checked_out == False:
            print("Item not checked out")
        else:
            self.checked_out = False
            return True
    def __str__(self):
        return("Type: {}.  Checked Out: {}.  Days Remaining: {}".format(self.type, self.checked_out, self.days_remaining))

    def advance(self, addtl_days):
        self.days_remaining += addtl_days

    def overdue(self):
        return self.days_remaining < 0

class ReserveBook(Library):
    def __init__(self, days_remaining = 1, checked_out = False):
        super().__init__(days_remaining, checked_out)
        self.type = "Reserve Book"

class Book(Library):
    def __init__(self, days_remaining = 15, checked_out = False):
        super().__init__(days_remaining, checked_out)
        self.type = "Book"

class CD(Library):
    def __init__(self, days_remaining = 7, checked_out = False):
        super().__init__(days_remaining, checked_out)
        self.type = "CD"

shelf = [ReserveBook(), ReserveBook(2, checked_out=True), Book(), Book(12, checked_out=True), CD(), CD(5, checked_out=True)]

option = ""
base_prompt = """
What would you like to do?
    catalog: show the catalog
    checkout <item_number>
    return <item_number>
    advance <num_days>
    account: see account status, including checked out items and overdue items
    Choice:  """
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
        break
    elif command == "catalog":
        for index,item in enumerate(shelf):
            print(index, item)
    elif command == "checkout" and len(words)>1:
        placement= int(words[1])-1
        if not shelf[placement].checkout():
            print ('This is already checked out.')
    elif command == "return" and len(words)>1:
        placement=int(words[1])
        for item in shelf:
            item.advance(placement)
    elif command == "advance" and len(words)>1:
        days_remaining=int(words[1])
        for book in shelf:
            book.advance(days_remaining)
    elif command == "account":
        print ('checked out:')
        for item in [item for item in shelf if item.checked_out==True]:
            print(item)
        print("overdue:")
        for item in [item for item in shelf if item.checked_out==True and item.overdue()==True]:
            print(item)
