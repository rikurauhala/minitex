import unittest
from utils import validators

class TestValidators(unittest.TestCase):
    def testValidateStringAttributes(self):
        validation = validators.validate_attribute_string(
            "This_is_a_string", "test_string"
        )
        self.assertTrue(validation)

    def testNotValidStringAttribute(self):
        with self.assertRaises(TypeError):
            validators.validate_attribute_string(
                True, "test"
            )

        with self.assertRaises(ValueError):
            validators.validate_attribute_string(
                "", "empty_string"
            )