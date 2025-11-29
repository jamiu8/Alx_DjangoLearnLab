from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from .models import Book, Author


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )

        # Create authors
        self.author1 = Author.objects.create(name="Chinua Achebe")
        self.author2 = Author.objects.create(name="Chimamanda Ngozi Adichie")

        # Create books
        self.book1 = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Purple Hibiscus",
            publication_year=2003,
            author=self.author2
        )

        # API client instance
        self.client = APIClient()

    # ---------------------------
    # Test List View
    # ---------------------------
    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ---------------------------
    # Test Detail View
    # ---------------------------
    def test_retrieve_book(self):
        url = reverse("book-detail", kwargs={"pk": self.book1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # ---------------------------
    # Test Create View
    # ---------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("book-create")
        data = {
            "title": "Americanah",
            "publication_year": 2013,
            "author": self.author2.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title="Americanah").publication_year, 2013)

    def test_create_book_unauthenticated(self):
        url = reverse("book-create")
        data = {
            "title": "Americanah",
            "publication_year": 2013,
            "author": self.author2.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------
    # Test Update View
    # ---------------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("book-update", kwargs={"pk": self.book1.id})
        data = {"title": "Things Fall Apart (Updated)"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart (Updated)")

    def test_update_book_unauthenticated(self):
        url = reverse("book-update", kwargs={"pk": self.book1.id})
        data = {"title": "Unauthorized Update"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------
    # Test Delete View
    # ---------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("book-delete", kwargs={"pk": self.book1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_delete_book_unauthenticated(self):
        url = reverse("book-delete", kwargs={"pk": self.book1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------
    # Test Filtering
    # ---------------------------
    def test_filter_books_by_title(self):
        url = reverse("book-list") + "?title=Things Fall Apart"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Things Fall Apart")

    # ---------------------------
    # Test Searching
    # ---------------------------
    def test_search_books_by_author(self):
        url = reverse("book-list") + "?search=Chimamanda"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Purple Hibiscus")

    # ---------------------------
    # Test Ordering
    # ---------------------------
    def test_order_books_by_publication_year_desc(self):
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.data[0]["publication_year"], 2003)
        self.assertEqual(response.data[1]["publication_year"], 1958)
