def view_all_books(all_books):
    if all_books != []:
        for book in all_books:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Yeaar: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}")


    else:
        print("No Books found in program")        