# test_pytorchcore.py
"""
Tests for PyTorchCore module.
"""

import unittest
from pytorchcore import PyTorchCore

class TestPyTorchCore(unittest.TestCase):
    """Test cases for PyTorchCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PyTorchCore()
        self.assertIsInstance(instance, PyTorchCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PyTorchCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
