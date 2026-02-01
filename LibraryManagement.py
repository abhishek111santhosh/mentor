class library:
    def __init__(self,book):
        self.book_self = {"Wings of Fire": True}
        self.book = book

    def add_book(self,value):
        self.book_self[value] = True
        print(f"Add book {value} succesfully ✅")

    def issue_book(self,value):
        for key in self.book_self.items():
            if key == value:
                self.book_self[value] = False
                print("Book Issued succesfully: ✅")
    
    def return_book(self,value):
        for key in self.book_self.items():
            if key == value:
                self.book_self[value] = True
                print("Book is return sucessfully✅")
    
    def book_search(self,value):
        return_value = False
        for key in self.book_self.items():
            if key == value:
                return_value = True
        return return_value
    

            
        
             
 