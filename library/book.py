"""define a Book class"""
class Book:
    """ initilize differ variable with id auto increment """
    _id_counter = 1
    def __init__(self, title, author, year, available = True ):
        self.id = Book._id_counter
        Book._id_counter += 1
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        return f"""ID: {self.id} | Title: {self.title} | Author: {self.author} |
        Year: {self.year} | Available: {'Yes' if self.available else 'No'}"""

    def to_dict(self):
        """defing a to dictionary funtion for data in dictionary"""
        return{
            "id" : self.id,
            "title" : self.title,
            "author" : self.author,
            "year": self.year,
            "available" : self.available
        }
    @classmethod
    def from_dict(cls, data):
        """creating from dictionary function to display data"""
        return cls(
            title = data["title"],
            author = data["author"],
            year = data["year"],
            available = data["available"]
        )
if __name__ == "__main__":
    b1 = Book("Pyhton", "Saif Ali", 2001 )
    print(b1)
    print(b1.to_dict())
