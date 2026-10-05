class book :
    def __init__(self , tital , author ):
        self.tital = tital
        self.author = author
        self.is_avelable = True

    def borrow_book(self):
        if self.is_avelable :
            self.is_avelable = False
            print("book is borrowed")
        else :
            print("book is unavalable")

    def return_book(self):
        if not self.is_avelable :
            self.is_avelable = True
            print("book is returned")
        else :
            print("book wasan't borrowed")
    def get_details(self):
        status = "avaliable" if self.is_avelable else "on loan"
        return  f'"{self.tital} by {self.author} - {status}'

b1 = book("ash","anshuman")
b1.borrow_book()
b1.return_book()
b1.get_details()
print(b1.get_details())
    