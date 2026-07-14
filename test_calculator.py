import unittest
import calculator

class TestCalculator(unittest.TestCase):

    # Reproduction test from Step 5
    def test_add(self):
        """Test that calculator.add() correctly adds two numbers."""
        result = calculator.add(2, 3)
        assert result == 5, f"Expected 5, but got {result}"

    def test_add_negative(self):
        """Test addition of negative integers."""
        result = calculator.add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_zero(self):
        """Test addition involving zero."""
        result = calculator.add(0, 5)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
