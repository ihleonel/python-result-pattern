import unittest
from application.update_user import UpdateUser
from success import Success
from error import Error
from domain.user import User
from user_repository_fake import UserRepositoryFake


class TestUpdateUser(unittest.TestCase):

    def setUp(self):
        self.user_repository = UserRepositoryFake()
        self.update_user = UpdateUser(self.user_repository)

    def test_successful_user_update_with_valid_data(self):
        user_id = 1
        name = "Juan Pérez"
        email = "juan@example.com"

        result = self.update_user(user_id, name, email)

        self.assertIsInstance(result, Success)
        self.assertTrue(result.is_success())
        self.assertFalse(result.is_error())

        user = result.get_value()
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, user_id)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)

    def test_error_when_updating_user_with_invalid_id(self):
        user_id = -1  # Invalid ID
        name = "Juan Pérez"
        email = "juan@example.com"

        result = self.update_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        self.assertTrue(result.is_error())
        self.assertFalse(result.is_success())
        self.assertEqual(result.get_errors(), f"Invalid user ID: {user_id}")

if __name__ == '__main__':
    unittest.main()
