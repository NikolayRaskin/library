from django.test import TestCase

from base.models import User_Profile
from django.contrib.auth.models import User
import datetime
class BookModelTest(TestCase):
   
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user('testUser', 'test@gmail.com', 'pass')        

    def test_birt_date_today_and_in_future(self):
        date = datetime.date.today()
        self.thisUser = User_Profile.objects.create(user = self.user, birth_date = date)
        self.assertFalse(self.thisUser.save())