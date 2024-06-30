# tests/test_console.py

import unittest
from console import HBNBCommand
from models import storage
from models.state import State

class TestConsoleCreate(unittest.TestCase):
    """Unit tests for the console"""

    def setUp(self):
        """Set up the test"""
        self.cli = HBNBCommand()

    def test_create_with_params(self):
        self.cli.onecmd('create State name="California"')
        states = storage.all(State)
        self.assertIn('California', [state.name for state in states])

if __name__ == "__main__":
    unittest.main()

