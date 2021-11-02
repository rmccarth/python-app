import unittest
from app.main import stringify

class TestStringMethod(unittest.TestCase):
    def test_stringify(self):
        self.assertEqual(stringify(1), '1')

if __name__=='__main__':
    unittest.main()
        
