class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False

    def borrow(self):
        self.is_borrowed=True
        print(self.title,"has been borrowed!")

    def return_book(self):
        self.is_borrowed=False
        print(self.title,"has been returned!")

dog_man=Book("Dog Man","Pilkey")
ikigai=Book("IKIGAI","Francesc Miralles and Hector Garcia")
animal_farm=Book("Animal Farm","George Orwell")

dog_man.borrow()
dog_man.return_book()

ikigai.borrow()
ikigai.return_book()

animal_farm.borrow()
animal_farm.return_book()



        