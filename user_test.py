import unittest
from user import User

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('OwitiCharles','XyZ3thf1')

    def test_init(self):
        """
        test case to check if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'OwitiCharles')
        self.assertEqual(self.new_user.password,'XyZ3thf1')

if __name__ == "__main__":
    unittest.main()
