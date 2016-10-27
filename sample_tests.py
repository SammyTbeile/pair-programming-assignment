from app import app
import unittest
import tempfile

class SampleTest(unittest.TestCase):

    def test_sammy(self):
        tester = app.test_client(self)
        response = tester.get('/sammy')
        self.assertIn(b'Birthday: August 13th', response.data)

    def test_natalia(self):
        tester = app.test_client(self)
        response = tester.get('/natalia')
        self.assertIn(b'Birthday: July 5th', response.data)


if __name__ == '__main__':
    unittest.main()
