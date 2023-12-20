class Book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Representing an instance of a data pointer as the string you actucally want to display to the user.
    def __str__(self):
        return ("{} written by <{}>".format(self.title, self.author))
    
    def __len__(self):
        return self.pages
    
mybook = Book('Python bible', "Python God", 500)
print(mybook)
# <__main__.Book instance at 0x10fe31368> -> Python bible written by Python God
print(len(mybook))
