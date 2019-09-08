from django.test import TestCase

from base.models import User_Profile
from user_profile.models import Book
from django.contrib.auth.models import User
import datetime
class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        date = datetime.date.today() - datetime.timedelta(days=111)
        user = User.objects.create_user('testUser', 'test@gmail.com', 'pass')
        self.thisUser = User_Profile.objects.create(user = user, birth_date = date)
        self.book = Book.objects.create(owner = self.thisUser, title = 'testBook', author = 'testAuthor')

    def test_first_name_max_length(self):
        book = Book.objects.get(id=self.book.id)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        book = Book.objects.get(id=self.book.id)
        max_length = book._meta.get_field('author').max_length
        self.assertEquals(max_length, 100)