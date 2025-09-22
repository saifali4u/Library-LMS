"""Make a class of Book name"""
class Book:
    """Now we have to define the const"""
    _id_counter = 1

    def __init__(self, title, author, year, available=True):
        self.id = Book._id_counter
        Book._id_counter += 1
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        return (
            f"ID: {self.id} "
            f"Title: {self.title} "
            f"Author: {self.year} "
            f"Year{self.year} "
            f"Available: {'Yes' if self.available else 'No'} "
         )

    def to_dict(self):
        """To return data in dicitonary form"""
        return {
            "ID": self.id,
            "Title": self.title,
            "Author": self.author,
            "Year": self.year,
            "Available": self.available
        }


if __name__ == "__main__":
    b1 = Book("Python", "Saif", "2000",)
    print(b1)
