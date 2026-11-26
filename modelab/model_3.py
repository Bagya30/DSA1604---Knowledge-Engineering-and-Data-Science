import matplotlib.pyplot as plt
genres = [
    'Fiction', 'Mystery', 'Science',
    'History', 'Biography', 'Self-help', 'Comics'
]
books = [14, 9, 6, 5, 7, 11, 8]
total = sum(books)
print("BOOKSTORE SALES ANALYSIS")
for i in range(len(genres)):
    percentage = (books[i] / total) * 100
    print(genres[i], ":", books[i],
          "(", round(percentage, 2), "%)")
print("Total Books Sold:", total)
plt.pie(books, labels=genres, autopct='%1.1f%%',
        startangle=90)
plt.title("Percentage Distribution of Books Sold")
plt.show()
