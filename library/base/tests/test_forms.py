from django.test import TestCase
from base.regForm import RegForm
import datetime

class RegFormTest(TestCase):
    # Valid Form Data
    def test_RegForm_valid(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RegForm(data={'user_name': "Test", 'user_email': "test@gmail.com", 
                              'user_firstname': "UserFirstName", 'user_lastname': 'UserLastName',
                              'birth_date':date, 'password':'qwe', 'confirm_password':'qwe'})
        self.assertTrue(form.is_valid())
    # Invalid Birth date
    def test_RegForm__birth_date_invalid(self):
        date = datetime.date.today()
        form = RegForm(data={'user_name': "Test", 'user_email': "test@mail.ru", 
                              'user_firstname': "UserFirstName", 'user_lastname': 'UserLastName',
                              'birth_date':date, 'password':'', 'confirm_password':''})
        self.assertFalse(form.is_valid())