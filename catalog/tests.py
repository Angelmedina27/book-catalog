from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from .models import Publisher, Book

class BookCatalogTests(TestCase):
    def test_book_appears_on_books_page(self):
        
        test_publisher = Publisher.objects.create(name="Test Publisher House")
        unique_title = "The journey through CIDM 3312"
        Book.objects.create(title=unique_title, price=19.99, publisher=test_publisher)

        response = self.client.get(reverse('book_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, unique_title)