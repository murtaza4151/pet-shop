from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

def add(a,b):
    return a+b
class userTest(TestCase):

    def test_add(self):
        self.assertEqual(add(5,5),12)

    def set_up_user(self):
        User.objects.create(username="Testuser",first_name="TestFname",lastname="Testlastname",email="TestUser@123",passwod="User@123")

        def test_create_user(self):
            User.objects.get(username="TestUser")
            self.assertEqual(User.email,self.user.email)
        def test_update_user(self):
            User=User.objects.get(username="Testuser")
            oldEmail=user.email
            User.email="updatedemail@gmail.com"
            User.save()

            user=user.objects.get(username="Testuser")
            self.assertNotEqual(oldEmail)
        


