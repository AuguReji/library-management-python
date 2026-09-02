import sys
flag = 0
borrow_list = []
class Books:
    def __init__(self, id, title, author, year, status, count):
        self.id = id 
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.count = count

########### Search for Adding #############    
def add_search(n, books_list, title):
    for i in range (n):
        if title == books_list[i].title:
            return i
    
    return -1


########### ADD BOOK #############    
def add_book(n, books_list, title ):
    status = 'Available'
    index = add_search(n,books_list, title)

    if index == -1:
        author = input("Author Name: ")
        author = author.upper()

        while True:
            try:
                year = int(input("Published Year: "))
                break
            except ValueError:
                print("Wrong Year Format: Re-enter")

        new_book = Books(n+1, title, author, year, status, 1)
        books_list.append(new_book)
        print("Book Added to Library!!😎️ ")
    else:
        books_list[index].count += 1
        print("Book already in library!!🤔️\nBook Count Increased!!😎️")

########### SEARCH BOOK #############  

def search_book(booksearch, n, books_list):
    global flag
    flag = 0
    for i in range(n):
        if booksearch in books_list[i].title:
            flag = 1
            print(
                    f"Book Id: {books_list[i].id}\n"
                    f"Title: {books_list[i].title}\n"
                    f"Author: {books_list[i].author}\n"
                    f"Published Year: {books_list[i].year}\n"
                    f"Status: {books_list[i].status}\n"
                    f"Count: {books_list[i].count}\n\n"
                )      

    if flag == 0:
        print("👉️Book NOT Found!!😥️")


########### BORROW BOOK #############  

def borrow_book(booksearch, n, books_list):
    global flag
    flag = 0
    search_book(booksearch, n, books_list)
    if flag == 1:
        done = 0
        while True:
            try:
                id = int(input("Enter Book Id: "))
                break
            except ValueError:
                print("Wrong Id Format: Re-enter")

        for i in range(n):
            if books_list[i].id == id and books_list[i].status == "Available":
                print(f"\n\tBorrowed Book Details\n{'-' * 25}\n")   # moved here
                print(
                    f"Book Id: {books_list[i].id}\n"
                    f"Title: {books_list[i].title}\n"
                    f"Author: {books_list[i].author}\n"
                    f"Published Year: {books_list[i].year}\n\n"
                )
                cc = books_list[i].count - 1
                books_list[i].count = cc
                if cc > 0:
                    books_list[i].status = "Available"
                else:
                    books_list[i].status = "Not Available"
                print(f"Status: {books_list[i].status}\n")
                print(f"Count: {books_list[i].count}\n")
                print("👉️Book Borrowed Successfully👈️\n")
                borrow_list.append(id)
                done = 1
                break
        if done == 0:
            print("👉️Sorry Book Not Available!!👈️\n")

########### RETURN BOOK #############       


def return_book(n, books_list):
    title = input("\nReturning Book Title: ")
    title = title.upper()
    index = add_search(n, books_list, title)

    if index != -1 and books_list[index].id in borrow_list:
        bid = books_list[index].id
        print(
            f"Book Id: {books_list[index].id}\n"
            f"Title: {books_list[index].title}\n"
            f"Author: {books_list[index].author}\n"
            f"Published Year: {books_list[index].year}"
        )
        books_list[index].count += 1
        books_list[index].status = "Available"
        print(
            f"Status: {books_list[index].status}\n"
            f"Count: {books_list[index].count}\n\n"
        )
        print("Book Returned Successfully!!🙏️🫂️")
        borrow_list.remove(bid)
    else:
        print("👉️Book was not yet borrowed!!😯️\nYou can add this book to library.😊️")
        add_book(n, books_list, title)

########### MAIN FUNCTION #############       
        

proceed = 'y'

print('-'*28)
print("|  Welcome to the Library  |")
print('-'*28)

books_list = []
books_list.append(Books(1, "WINGS OF FIRE", "Dr.A. P. J. ABDUL KALAM and ARUN TIWARI", 1999, "Available", 1))
books_list.append(Books(2, "GOD OF SMALL THINGS", "ARUNDATHI ROY", 1997, "Available", 1))
books_list.append(Books(3, "THE PSHYCHOLOGY OF MONEY", "MORGAN HOUSEL", 2020, "Available", 1))
books_list.append(Books(4, "THE ALCHEMIST", "PAULO COELHO", 1988, "Available", 1))
books_list.append(Books(5, "MALGUDI DAYS", "R. K. NARAYAN", 1942, "Available", 1))

while proceed == 'y' or proceed == 'Y':
    print(f"\tMenu\n{'-' * 25}\nAdd Book(a)\nSearch(s)\nBorrow(b)\nReturn(r)\nCatalogue(c)\nExit(y)")
    c = input("Please Choose one option:")

    match c:
        case 'a' | 'A':
            print(f"\n\tAdd a Book\n{'-' * 25}\n Enter the details: \n")
            n = len(books_list)
            title = input("Book Title : ")
            title = title.upper()
            add_book(n, books_list,title)
        case 's' | 'S':
            print(f"\n\tSearch a Book\n{'-' * 25}\n Enter the details: \n")
            booksearch = input("Which book do you want: ")
            booksearch = booksearch.upper()
            n = len(books_list)
            search_book(booksearch, n, books_list)
        case 'b' | 'B': 
            print(f"\n\tBorrow a Book\n{'-' * 25}\n Enter the details: \n")
            booksearch = input("Which book do you want: ")
            booksearch = booksearch.upper()
            n = len(books_list)
            borrow_book(booksearch, n, books_list)
        case 'r' | 'R':
            n = len(books_list)
            return_book(n,books_list)
        case 'c' | 'C':
            print(f"\n\tCatalogue\n{'-' * 25}\n")
            n = len(books_list)
            for i in range (0, n):
                print(
                    f"Book Id: {books_list[i].id}\n"
                    f"Title: {books_list[i].title}\n"
                    f"Author: {books_list[i].author}\n"
                    f"Published Year: {books_list[i].year}\n"
                    f"Status: {books_list[i].status}\n"
                    f"Count: {books_list[i].count}\n\n"
                )        
        case 'y' | 'Y':
            print("THANK YOU 🫂️ !! Visit Again!!❤️🤟️\n")
            proceed = 'n'
            sys.exit(0)
        case _:
            print("\nWrong Choice 😥️")




                