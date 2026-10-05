class library :
    def __init__(self , booktital , avalilablecopy):
        self.booktital = booktital
        self.avalilablecopy = avalilablecopy

    def borrow_books(self):
        wantcopy = int(input("how many copies you want : "))
        if self.avalilablecopy < wantcopy   :
            print("insufficent copy available ")
        else :
            self.avalilablecopy -= wantcopy
            print(self.avalilablecopy)

    def return_book(self):
        retnbook = int(input("how many books you want return : "))
        self.avalilablecopy += retnbook
        print(self.avalilablecopy)

my_library = library("python basics" , 5)
my_library.borrow_books()
my_library.return_book()
        

        
    
    


