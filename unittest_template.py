#!/usr/bin/env python3

# Internal Libs
import unittest
from unittest.mock import patch

# External/Installed Libs

# Custom classes/files/libs (import test files and classes here)


class TestTemplate(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    """
    Runs before testing is started
    """
    pass
  
  @classmethod
  def tearDownClass(cls):
    """
    Clean-up after all tests complete
    """
    pass
  
  def setUp(self):
    """
    Runs before each test
    """
    pass
  
  def tearDown(self):
    """
    Clears up after each test
    """
    pass
  
  # Individual tests go here
  def test_working(self):
    """
    An example of how each individual test should look like.
    All tests must start with 'test_'
    """
    working = None
    self.assertEqual(None, working)
    
    
if __name__ == "__main__":
  uniitest.main()
  
  
# Table of assertions: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
