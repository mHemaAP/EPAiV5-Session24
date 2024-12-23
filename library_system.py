from enum import Enum, auto

# Enum for Book Genres
class BookGenre(Enum):
    """
    Enum representing different book genres.
    """
    FICTION = auto()        # Fiction genre
    NON_FICTION = auto()    # Non-fiction genre
    SCIENCE = auto()        # Science genre
    HISTORY = auto()        # History genre
    BIOGRAPHY = auto()      # Biography genre

# Enum for Membership Levels
class MembershipLevel(Enum):
    """
    Enum representing membership levels with associated fees.
    """
    BASIC = 100         # Basic membership with a fee of 100    
    PREMIUM = 200       # Premium membership with a fee of 200
    GOLD = 500         # Gold membership with a fee of 500

# Custom exception for when a book is not available
class BookNotAvailableError(Exception):
    """
    Exception raised when a book is not available for borrowing.
    """
    def __init__(self, message="The book is not available for borrowing."):
        super().__init__(message)

# Custom exception for late book returns
class LateReturnError(Exception):
    """
    Exception raised when a book is returned late.
    """
    def __init__(self, message="The book was returned late."):
        super().__init__(message)

# Custom exception for invalid membership levels
class InvalidMembershipError(Exception):
    """
    Exception raised when an invalid membership level is encountered.
    """
    def __init__(self, message="The membership level is invalid."):
        super().__init__(message)

# Book class to represent a book in the library
class Book:
    """
    Represents a book with a title, genre, and availability status.

    Attributes:
        title (str): The title of the book.
        genre (BookGenre): The genre of the book, must be an instance of `BookGenre`.
        is_available (bool): Availability status of the book, defaults to True.

    Methods:
        borrow(): Marks the book as borrowed. Raises `BookNotAvailableError` if the book is not available.
        return_book(is_late: bool): Marks the book as returned. Raises `LateReturnError` if the book is returned late.
    """
    def __init__(self, title: str, genre: BookGenre, is_available: bool = True):
        self.title = title

        if not isinstance(genre, BookGenre):
            raise AttributeError(f"{genre} must be an instance of BookGenre.")
        self.genre = genre
        self.is_available = is_available

    def borrow(self):
        """
        Marks the book as borrowed.
        Raises `BookNotAvailableError` if the book is not available.
        """
        if not self.is_available:
            raise BookNotAvailableError(f"The book '{self.title}' is currently not available.")
        self.is_available = False

    def return_book(self, is_late: bool) -> None:
        """
        Marks the book as returned.
        
        Args:
            is_late (bool): Indicates whether the book is returned late.
        
        Raises:
            LateReturnError: If the book is returned late.
        """
        self.is_available = True
        if is_late:
            raise LateReturnError(f"The book '{self.title}' was returned late. Late fees may apply.")

# Member class to represent a library member
class Member:
    """
    Represents a library member with a name and membership level.

    Attributes:
        name (str): The name of the member.
        membership_level (MembershipLevel): The membership level of the member, must be an instance of `MembershipLevel`.

    Methods:
        get_fee(): Returns the annual fee for the member based on their membership level.
    """
    def __init__(self, name: str, membership_level: MembershipLevel):
        self.name = name
        self.membership_level = membership_level

    def get_fee(self) -> float:
        """
        Returns the fee associated with the member's membership level.
        
        Raises:
            InvalidMembershipError: If the membership level is invalid.
        """
        if not isinstance(self.membership_level, MembershipLevel):
            raise InvalidMembershipError(f"Invalid membership level for member {self.name}")
        return self.membership_level.value 
    
