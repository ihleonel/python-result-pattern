import unittest
from create_user import CreateUser
from success import Success
from error import Error
from user import User


class TestCreateUser(unittest.TestCase):

    def setUp(self):
        self.create_user = CreateUser()

    def test_successful_user_creation_with_valid_data(self):
        user_id = 1
        name = "Juan Pérez"
        email = "juan@example.com"

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Success)
        self.assertTrue(result.is_success())
        self.assertFalse(result.is_error())

        user = result.get_value()
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, user_id)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)

    def test_error_with_invalid_id_zero(self):
        user_id = 0
        name = "Juan Pérez"
        email = "juan@example.com"

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        self.assertFalse(result.is_success())
        self.assertTrue(result.is_error())

        errors = result.get_errors()
        self.assertIsInstance(errors, dict)
        self.assertIn('id', errors)
        self.assertEqual(errors['id'], "El campo 'id' debe ser un número positivo")

    def test_error_with_negative_id(self):
        user_id = -5
        name = "Juan Pérez"
        email = "juan@example.com"

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        errors = result.get_errors()
        self.assertIn('id', errors)
        self.assertEqual(errors['id'], "El campo 'id' debe ser un número positivo")

    def test_error_with_empty_name(self):
        user_id = 1
        name = ""
        email = "juan@example.com"

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        errors = result.get_errors()
        self.assertIn('name', errors)
        self.assertEqual(errors['name'], "El campo 'name' no puede ser nulo o estar vacío")

    def test_error_with_whitespace_only_name(self):
        user_id = 1
        name = "   "
        email = "juan@example.com"

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        errors = result.get_errors()
        self.assertIn('name', errors)
        self.assertEqual(errors['name'], "El campo 'name' no puede ser nulo o estar vacío")

    def test_error_with_empty_email(self):
        user_id = 1
        name = "Juan Pérez"
        email = ""

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        errors = result.get_errors()
        self.assertIn('email', errors)
        self.assertEqual(errors['email'], "El campo 'email' no puede ser nulo o estar vacío")

    def test_error_with_whitespace_only_email(self):
        user_id = 1
        name = "Juan Pérez"
        email = "   "

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        errors = result.get_errors()
        self.assertIn('email', errors)
        self.assertEqual(errors['email'], "El campo 'email' no puede ser nulo o estar vacío")

    def test_error_with_email_without_at_symbol(self):
        user_id = 1
        name = "Juan Pérez"
        email = "juan.example.com"

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        errors = result.get_errors()
        self.assertIn('email', errors)
        self.assertEqual(errors['email'], "El campo 'email' debe tener un formato válido")

    def test_multiple_validation_errors_are_collected(self):
        user_id = -1
        name = ""
        email = "invalid-email"

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        errors = result.get_errors()

        self.assertEqual(len(errors), 3)
        self.assertIn('id', errors)
        self.assertIn('name', errors)
        self.assertIn('email', errors)

        self.assertEqual(errors['id'], "El campo 'id' debe ser un número positivo")
        self.assertEqual(errors['name'], "El campo 'name' no puede ser nulo o estar vacío")
        self.assertEqual(errors['email'], "El campo 'email' debe tener un formato válido")

    def test_all_fields_empty_or_invalid(self):
        user_id = 0
        name = "   "
        email = "   "

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        errors = result.get_errors()

        self.assertEqual(len(errors), 3)
        self.assertIn('id', errors)
        self.assertIn('name', errors)
        self.assertIn('email', errors)

    def test_email_validation_precedence_empty_over_format(self):
        user_id = 1
        name = "Juan Pérez"
        email = ""

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Error)
        errors = result.get_errors()
        self.assertIn('email', errors)
        self.assertEqual(errors['email'], "El campo 'email' no puede ser nulo o estar vacío")

    def test_minimal_valid_email_with_at_symbol(self):
        user_id = 1
        name = "Juan Pérez"
        email = "a@b"

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Success)
        user = result.get_value()
        self.assertEqual(user.email, "a@b")

    def test_name_with_leading_trailing_spaces_but_content(self):
        user_id = 1
        name = "  Juan Pérez  "
        email = "juan@example.com"

        result = self.create_user(user_id, name, email)

        self.assertIsInstance(result, Success)
        user = result.get_value()
        self.assertEqual(user.name, "  Juan Pérez  ")

    def test_return_type_is_result_interface(self):
        result_success = self.create_user(1, "Juan", "juan@example.com")
        self.assertTrue(hasattr(result_success, 'is_success'))
        self.assertTrue(hasattr(result_success, 'is_error'))

        result_error = self.create_user(-1, "", "")
        self.assertTrue(hasattr(result_error, 'is_success'))
        self.assertTrue(hasattr(result_error, 'is_error'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
