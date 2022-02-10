import unittest

# import one level up to access the validator
from validator import Validator


class TestValidator(unittest.TestCase):
    def test_it_will_reject_username_if_too_long(self):
        # assume
        username = 'InvalidTooLongInvalidTooLongInvalidTooLong'
        validator = Validator()
        # Action
        result = validator.username_is_valid(username)
        # Assert
        self.assertFalse(result)
