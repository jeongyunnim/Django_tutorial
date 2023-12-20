class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def hello(self):
        print("hello")
    
    def report(self):
        print ("i'm {} {}".format(self.first_name, self.last_name))
    
x = Person("John", "Smith")
x.hello()
x.report()

class Agent(Person):

    def __init__(self, first_name, last_name, code):
        Person.__init__(self, first_name, last_name)
        self.code = code

    def reveal(self):
        if self.code == 123:
            print("I'm secret agent")
        else :
            self.report()

    def hello(self):
        print("<(-_-) I can do!")

x = Agent("John", "smith", 123)
x.hello()
x.reveal()
