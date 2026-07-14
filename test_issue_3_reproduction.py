import calculator

def test_add():
    """Test that calculator.add() correctly adds two numbers."""
    result = calculator.add(2, 3)
    assert result == 5, f"Expected 5, but got {result}"

if __name__ == "__main__":
    test_add()
    print("All tests passed.")
