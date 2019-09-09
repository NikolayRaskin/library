from django.test import TestCase
from django.test import Client
from base.models import User_Profile
from user_profile.models import Book
from django.contrib.auth.models import User
from django.urls import reverse, resolve

import datetime

class TestViewUser_Profile(TestCase):
    def setUp(self):
        date = datetime.date.today() - datetime.timedelta(days=111)
        user = User.objects.create_user('testUser', 'test@gmail.com', 'pass')
        self.thisUser = User_Profile.objects.create(user = user, birth_date = date)
        self.book = Book.objects.create(owner = self.thisUser, title = 'testBook', author = 'testAuthor')
    
    def test_uses_correct_template(self):
        login = self.client.login(username='testUser', password='pass')

        response = self.client.get(reverse('user_profile', kwargs={'id': self.thisUser.id}))
        self.assertTemplateUsed(response, 'user_profile/user_profile.html')

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testUser', password='pass')

        response = self.client.get(reverse('user_profile', kwargs={'id': self.thisUser.id}))
        self.assertEqual(response.status_code, 200)

    def test_removeBook(self):
        response = self.client.delete(self.book.id)
        self.assertTrue(response)

