
import add_books
import view_all_books
import update_books
import remove_books
all_books = []

while True:    # using multiple running
    print("Welcome to Library Management system")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Books")
    print("4. Remove Books")
    

    menu  = input("Select any number: ")

    if menu == "0":
        print("Thanks for using  Library Management system") 
        break

    elif menu == "1":
         all_books = add_books.add_books(all_books)

    elif menu == "2":
         view_all_books.view_all_books(all_books)

    elif menu == "3":
         title = input("Enter title to Update: ")
         new_author = input("Enter New author Name: ")
         update_books.update_books(all_books,title, new_author)


    elif menu == "4":
         title = input("Enter title to Remove: ")
         
         remove_books.remove_book(all_books,title)         

    else:
         print("Choose a valid number")          

   