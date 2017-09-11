"""
Tests for building queries
"""

import unittest

import graspy

example_class = """
class Hello:

    def say(self):
        print("Hello World")

"""

class TestQuery(unittest.TestCase):
    """Test query.py

    """

    def test_search_finds_class(self):
        results = graspy.query.search(example_class, "class-def")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Hello")

if __name__ == "__main__":
    unittest.main()
