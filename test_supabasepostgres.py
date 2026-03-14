# test_supabasepostgres.py
"""
Tests for SupabasePostgres module.
"""

import unittest
from supabasepostgres import SupabasePostgres

class TestSupabasePostgres(unittest.TestCase):
    """Test cases for SupabasePostgres class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SupabasePostgres()
        self.assertIsInstance(instance, SupabasePostgres)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SupabasePostgres()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
