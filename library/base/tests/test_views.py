from django.test import TestCase
from django.test import Client
from base.models import User_Profile
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

class TestViewBase(TestCase):
    def setUp(self):
        date = datetime.date.today() - datetime.timedelta(days=111)
        self.user = User.objects.create_user('testUser', 'test@gmail.com', 'pass')
        thisUser = User_Profile.objects.create(user = self.user, birth_date = date)
        self.user.save()
        thisUser.save()

    def test_login_redirect(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_login(self):
        user_login = self.client.login(username="testUser", password="pass")
        self.assertTrue(user_login)

    def test_uses_correct_template(self):
        user_login = self.client.login(username="testUser", password="pass")        
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'base/index.html')
    
    def test_view_url_exists_at_desired_location(self):
        user_login = self.client.login(username="testUser", password="pass")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_removeUser(self):
        response = self.client.delete(self.user)
        self.assertTrue(response)

