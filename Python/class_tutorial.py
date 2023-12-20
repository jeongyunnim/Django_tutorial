class Sample():

    species = 'Human' # CLASS OBJECT ATTRIBUTE
    def __init__(self, name):
        self.name = name

num = Sample(name = "jeseo")
# lecture's out put is "<class '__main__.sample'>" but my output is "<type 'instance'>"
print(num.name)

print("\n==================\n")

class Studnet:
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def print_info(self):
        print("[{}]\ngpa: {}".format(self.name, self.gpa))

student1 = Studnet(name = "jeseo", gpa = 4.0)
student2 = Studnet(name = "gildong", gpa = 3)

print(student1)
student1.print_info()
student2.print_info()

print("\n==================\n")

class Agent():
    
    origin = "USA"

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

x = Agent("jeseo", 200, 100)
print(x.weight)
x.weight = 160

print(x.weight)

print("\n==================\n")

class Circle():
    
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return (self.radius * self.radius * Circle.pi) # self.pi ( OK )

    def perimeter(self):
        return (2 * self.radius * self.pi)
    
mycircle = Circle(20)
print("area: {}".format(mycircle.area()))
print("perimeter: {}".format(mycircle.perimeter()))