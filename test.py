import unittest
from main import st_response

class TestIsOdd(unittest.TestCase):

  def test_st_response(self):
      self.assertTrue(st_response(3))
  def test_build(self):
        self.assertTrue(True)




if __name__ == '__main__':
    unittest.main()