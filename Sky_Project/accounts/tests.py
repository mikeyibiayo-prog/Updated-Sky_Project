# Imports Django's testing tools.
from django.test import TestCase

# Imports Django's built-in User model for creating test users.
from django.contrib.auth.models import User

# Import Message model from the messages app (fixed import path)
from messages.models import Message


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


# Tests message creation.
class MessageTests(TestCase):

    def setUp(self):
        # Create two users for messaging
        self.user1 = User.objects.create_user(
            username="user1@test.com",
            password="test12345"
        )
        self.user2 = User.objects.create_user(
            username="user2@test.com",
            password="test12345"
        )

    def test_create_message(self):
        # Create a message
        message = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            subject="Test Subject",
            body="Test Message",
            is_draft=False
        )

        # Check message saved correctly
        self.assertEqual(message.subject, "Test Subject")
        self.assertEqual(message.sender, self.user1)

    def test_create_draft(self):
        # Create a draft message
        draft = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            subject="Draft",
            body="Draft Message",
            is_draft=True
        )

        # Check it is saved as draft
        self.assertTrue(draft.is_draft)


# Tests updating a draft (CRUD Update)
class DraftTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1@test.com",
            password="test12345"
        )
        self.user2 = User.objects.create_user(
            username="user2@test.com",
            password="test12345"
        )

    def test_edit_draft(self):
        # Create draft
        draft = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            subject="Old Subject",
            body="Old Message",
            is_draft=True
        )

        # Update draft
        draft.subject = "Updated Subject"
        draft.save()

        # Check update worked
        self.assertEqual(draft.subject, "Updated Subject")


# Tests deleting messages (CRUD Delete)
class DeleteMessageTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1@test.com",
            password="test12345"
        )
        self.user2 = User.objects.create_user(
            username="user2@test.com",
            password="test12345"
        )

    def test_delete_message(self):
        # Create message
        message = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            subject="Delete Me",
            body="Test",
            is_draft=False
        )

        # Delete message
        message.delete()

        # Check it was removed
        self.assertEqual(Message.objects.count(), 0)


# Tests searching messages
class SearchTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1@test.com",
            password="test12345"
        )
        self.user2 = User.objects.create_user(
            username="user2@test.com",
            password="test12345"
        )

        # Create message for search
        Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            subject="Hello World",
            body="Test message",
            is_draft=False
        )

    def test_search_message(self):
        # Simple search check
        results = Message.objects.filter(subject__icontains="Hello")

        # Check one result found
        self.assertEqual(results.count(), 1)