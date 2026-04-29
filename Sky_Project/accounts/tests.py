# Imports Django's testing tools.
from django.test import TestCase

# Imports Django's built-in User model for creating test users.
from django.contrib.auth.models import User


# Tests login functionality.
class LoginTests(TestCase):

    def test_login_positive(self):
        # Creates a valid test user.
        User.objects.create_user(
            username="test@xyz.com",
            password="test12345"
        )

        # Attempts to log in using the correct password.
        login = self.client.login(
            username="test@xyz.com",
            password="test12345"
        )

        # Checks that login is successful.
        self.assertTrue(login)

    def test_login_negative(self):
        # Creates a valid test user.
        User.objects.create_user(
            username="test@xyz.com",
            password="test12345"
        )

        # Attempts to log in using an incorrect password.
        login = self.client.login(
            username="test@xyz.com",
            password="wrongpassword"
        )

        # Checks that login fails.
        self.assertFalse(login)


# Tests registration functionality.
class RegisterTests(TestCase):

    def test_register_positive(self):
        # Creates a new user account.
        user = User.objects.create_user(
            username="new@xyz.com",
            password="test12345"
        )

        # Checks the correct username was saved.
        self.assertEqual(user.username, "new@xyz.com")

    def test_register_negative(self):
        # Creates a user with an existing username.
        User.objects.create_user(
            username="test@xyz.com",
            password="test12345"
        )

        # Checks that creating another user with the same username causes an error.
        with self.assertRaises(Exception):
            User.objects.create_user(
                username="test@xyz.com",
                password="test12345"
            )