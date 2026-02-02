"""Tests for example module."""

import pytest
from src.example import hello, add


class TestHello:
    """Tests for hello function."""
    
    def test_hello_with_name(self):
        """Test hello returns correct greeting."""
        assert hello("World") == "Hello, World!"
    
    def test_hello_with_empty_string(self):
        """Test hello with empty string."""
        assert hello("") == "Hello, !"


class TestAdd:
    """Tests for add function."""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-2, -3) == -5
    
    def test_add_mixed_numbers(self):
        """Test adding mixed numbers."""
        assert add(-5, 10) == 5
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add(5, 0) == 5
