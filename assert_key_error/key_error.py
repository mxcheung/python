import unittest

class TestMandatoryFields(unittest.TestCase):
    def test_missing_firstname(self):
        data = {
            'lastname': 'Doe',
            'phonenumber': '123-456-7890'
        }
        with self.assertRaises(KeyError) as context:
            check_mandatory_fields(data)
        self.assertIn('firstname', str(context.exception))

    def test_missing_lastname(self):
        data = {
            'firstname': 'John',
            'phonenumber': '123-456-7890'
        }
        with self.assertRaises(KeyError) as context:
            check_mandatory_fields(data)
        self.assertIn('lastname', str(context.exception))

    def test_missing_phonenumber(self):
        data = {
            'firstname': 'John',
            'lastname': 'Doe'
        }
        with self.assertRaises(KeyError) as context:
            check_mandatory_fields(data)
        self.assertIn('phonenumber', str(context.exception))

    def test_all_fields_present(self):
        data = {
            'firstname': 'John',
            'lastname': 'Doe',
            'phonenumber': '123-456-7890'
        }
        # No exception should be raised when all fields are present
        self.assertTrue(check_mandatory_fields(data))

if __name__ == '__main__':
    unittest.main()
