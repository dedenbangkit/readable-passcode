import unittest

from readable_passcode import passcode_generator


class TestGeneratePasscode(unittest.TestCase):
    def test_passcode_generator(self):
        passcode = passcode_generator(
            word=3,
            number=3,
            special_char=True,
        )
        self.assertIsInstance(passcode, str)
        self.assertTrue(len(passcode) > 0)


if __name__ == "__main__":
    unittest.main()
