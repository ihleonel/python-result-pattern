import unittest
from application.user_updater import UserUpdater
from domain.user import User
from result import Error, Success
from user_repository_fake import UserRepositoryFake


class TestUserUpdater(unittest.TestCase):

    def setUp(self):
        self.user_repository = UserRepositoryFake()
        self.user_updater = UserUpdater(self.user_repository)

    def test_successful_user_update_with_valid_data(self):
        user_id = 1
        name = "Juan Pérez"
        email = "juan@example.com"

        result = self.user_updater(user_id, name, email)

        self.assertIsInstance(result, Success)
        assert isinstance(result, Success)

        user: User = result.value
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, user_id)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)

    def test_update_user_with_invalid_id(self):
        user_id = -1
        name = "Juan Pérez"
        email = "juan@example.com"
        result = self.user_updater(user_id, name, email)

        self.assertIsInstance(result, Error)
        assert isinstance(result, Error)
        errors = result.error
        assert isinstance(errors, dict)

        self.assertIn("id", errors)
        self.assertEqual(errors["id"], f"Invalid user ID: {user_id}")

    def test_update_user_with_empty_name(self):
        user_id = 1
        name = ""
        email = "juan@example.com"

        result = self.user_updater(user_id, name, email)

        self.assertIsInstance(result, Error)
        assert isinstance(result, Error)

        errors = result.error
        assert isinstance(errors, dict)
        self.assertIn("name", errors)
        self.assertEqual(errors["name"], "Name is required")

    def test_update_user_with_invalid_email(self):
        user_id = 1
        name = "Juan Pérez"
        email = "invalid-email"

        result = self.user_updater(user_id, name, email)

        self.assertIsInstance(result, Error)
        assert isinstance(result, Error)

        errors = result.error
        assert isinstance(errors, dict)
        self.assertIn("email", errors)
        self.assertEqual(errors["email"], "Email is invalid")

    def test_update_user_with_existing_email(self):
        user_id = 1
        name = "Juan Sanchez"
        email = "carlos@example.com"

        result = self.user_updater(user_id, name, email)

        self.assertIsInstance(result, Error)
        assert isinstance(result, Error)

        errors = result.error
        assert isinstance(errors, dict)
        self.assertIn("email", errors)
        self.assertEqual(errors["email"], "Email already exists")


if __name__ == '__main__':
    unittest.main()
