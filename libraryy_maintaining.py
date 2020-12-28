import  datetime

class Library:
    def __init__(self,listofbooks,library_name):
        date_time = datetime.datetime.today()
        self.lendedbooklist = {}
        self.listofbooks = listofbooks
        self.library_name= library_name

    def displaybooks(self):
        print(f"We have following books in our: {self.library_name}")
        for books in listofbooks:
            print(books)

    def lendbooks(self,name,book_name):
            if book_name in self.listofbooks:
                self.lendedbooklist[book_name] = [name,datetime.datetime.today().strftime("%H:%M:%S %h,%d,%Y")]
                self.listofbooks.remove(book_name)
                print("Lended")
            else:
                try:
                    print(f"Sorry the book is lended by {self.lendedbooklist[book_name][0]}")
                except KeyError:
                    print("Sorry The book is not available in the library stock: ")
                except Exception as e:
                    print(e)



    def returnbook(self,clnt_name,book):
            if book not in self.listofbooks:
                try:
                    if clnt_name == self.lendedbooklist[book][0]:
                        self.lendedbooklist.pop(book)
                        self.listofbooks.append(book)
                        print("Returned")
                    else:
                        print("Your Name doesn't Matches in our Records, Please enter your name Correctly:")
                except KeyError:
                    print("You cannot return the book because the book is either not in our Library or it is not lended by you:")

            else:
                try:
                    if book in self.listofbooks:
                        print("You cannot return the book because the book is not lended by you")
                except Exception as e:
                    print(e)





if __name__ == '__main__':

    listofbooks = ["Python","C++","Java","Javascript","Django","Flask","HTML","CSS","Node.js","Mongodb"]

    l1 = Library(listofbooks,"Shubham's library")

    while True:
        print(f"Welcome to the {l1.library_name}.\n")
        option = input("Enter 'dis' for list of books available in the library\n"
                        "Enter 'lend' for lending a book from library if available\n"
                        
                        "Enter 'ret' to return a book to library\n"
                    
                       "and Enter 'quit' to quit for library menu\n")



        if option.lower() == 'dis':
            l1.displaybooks()

        elif option.lower() == 'lend':
            client_name = input("Please Provide your Full name: ")
            book_name = input("Which book you want to Lend: ")
            l1.lendbooks(client_name.lower(),book_name)





        elif option.lower() == 'ret':
            client_name = input("Please Provide your Full name: ")
            book_name = input("Which book you want to Return: ")
            l1.returnbook(client_name.lower(),book_name)




        else:
            print("Wrong input, Please Enter a valid Input:")

        user_op = ""
        while (user_op.lower() != 'q' and user_op.lower() != 'c'):
            user_op = input("Enter 'q' to Quit and 'c' to Continue: ")
            if user_op.lower() == 'q':
                exit()
            elif user_op.lower() == 'c':
                continue
            else:
                print("Enter a valid input please:")
