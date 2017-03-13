import unittest


class HelloWorldTestCase(unittest.TestCase):
    def test_hello_world(self):
        """Should return 'Hello World'."""
        self.assertEqual(hello_world(), "Hello World")
