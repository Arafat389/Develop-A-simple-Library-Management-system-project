def remove_book(all_books,title):
        # Remove a book based on its ISBN or title
        for book in all_books:
            if book['title'] == title:
                all_books.remove(book)
                print(f"Book with TITLE  {title} removed successfully.")
                return
        print(f"No book found with TITLE {title}.")