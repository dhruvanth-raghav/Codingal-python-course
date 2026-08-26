books = ["Sudha Murty", "Animal Farm", "wonder", "The war horse", "TinTin"]
copy_counts = [4, 1, 6, 3, 2]

library = {book: count for book, count in zip(books, copy_counts)}
print("Full Library Stock☑️:", library)

available_books = [book for book in books if library[book] > 0]
print("Books Available:", available_books)

selcted_book = input("Which book do you want to borrow❔ ")

if selcted_book not in library or library[selcted_book] == 0:
    print(selcted_book, "is not available!❌ Stopping the checker.")
    exit()

late_fees = [5, 8, 4, 6, 7]
extra_fee = int(input("Enter the extra library fee to add to every book🪙: "))

updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))
print("Updated Late Fees:", updated_fees)

book_index = books.index(selcted_book)
selcted_fee = updated_fees[book_index]
print("Late fee for", selcted_book, "after update:", selcted_fee)

library[selcted_book] = library[selcted_book] - 1
print(selcted_book, "borrowed! Remaining copies:", library[selcted_book])

print()
print("===== LIBRARY BOOK AVAILABILITY CHECKER =====")
print("Book Borrowed:", selcted_book)
print("Late Fee:", selcted_fee)
print("Updated Library Stock:", library)
