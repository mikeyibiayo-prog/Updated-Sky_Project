from django.test import TestCase
from django.contrib.auth.models import User

class LoginTests(TestCase):

    def test_login_positive(self):
        User.objects.create_user(
            username="test@xyz.com",
            password="test12345"
        )

        login = self.client.login(
            username="test@xyz.com",
            password="test12345"
        )

        self.assertTrue(login)

    def test_login_negative(self):
        User.objects.create_user(
            username="test@xyz.com",
            password="test12345"
        )

        login = self.client.login(
            username="test@xyz.com",
            password="wrongpassword"
        )

        self.assertFalse(login)


class RegisterTests(TestCase):

    def test_register_positive(self):
        user = User.objects.create_user(
            username="new@xyz.com",
            password="test12345"
        )

        self.assertEqual(user.username, "new@xyz.com")

    def test_register_negative(self):
        User.objects.create_user(
            username="test@xyz.com",
            password="test12345"
        )

        with self.assertRaises(Exception):
            User.objects.create_user(
                username="test@xyz.com",
                password="test12345"
            )