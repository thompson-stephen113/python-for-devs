from django.test import TestCase
from .models import Book

# Create your tests here.
class BookModelTest(TestCase):
    # Creates test data
    def setUpTestData():
        # Sets up non-modified objects used by all test methods
        Book.objects.create(
            name = "Pride and Prejudice",
            author_name = "Jane Austen",
            genre = "classic",
            book_type = "hardcover",
            price = "23.71"
        )

    # Defines test for the book name
    def test_book_name(self):
        # Gets a book object to test
        book = Book.objects.get(id=1)

        # Gets the metadata for the "name" field and uses it to query its data
        field_label = book._meta.get_field("name").verbose_name

        # Compares value to expected result
        self.assertEqual(field_label, "name")

    # Defines test for the book author name
    def test_author_name_max_length(self):
        # Gets a book object to test
        book = Book.objects.get(id=1)

        # Gets the metadata for the "author_name" field and uses it to query its data
        max_length = book._meta.get_field("author_name").max_length

        # Compares value to expected result
        self.assertEqual(max_length, 120)
