class Book:
    def __init__(self, title=None, author=None, ISBN=None, price=None):

        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price

    def display_info(self):

        print(f"Название: {self.title}, Автор: {self.author}, ISBN: {self.ISBN}, Цена: {self.price} USD")


def main():
    books = []

    n = int(input("Сколько книг вы хотите добавить? "))

    for i in range(n):
        print(f"\nВведите данные для книги {i+1}:")
        title = input("Название книги: ")
        author = input("Автор книги: ")
        ISBN = input("ISBN книги: ")
        price = input("Цена книги (USD): ")


        book = Book(title, author, ISBN, price)
        books.append(book)

    print("\n📚 Информация о книгах:")
    for book in books:
        book.display_info()

if __name__ == "__main__":
    main()
