import pytest

# Function to test for square of a number
def square(x):
    return x * x

# Function to test for cube of a number
def cube(x):
    return x * x * x

# Function to test for power of a number
def power(base, exponent):
    return base ** exponent

def test_square():
    assert square(2) == 4, "Test failed: 2 squared should be 4"
    assert square(-3) == 9, "Test failed: -3 squared should be 9"
    assert square(0) == 0, "Test failed: 0 squared should be 0"

def test_cube():
    assert cube(2) == 8, "Test failed: 2 cubed should be 8"
    assert cube(-3) == -27, "Test failed: -3 cubed should be -27"
    assert cube(0) == 0, "Test failed: 0 cubed should be 0"

def test_power():
    assert power(2, 3) == 8, "Test failed: 2 raised to the power of 3 should be 8"
    assert power(3, 2) == 9, "Test failed: 3 raised to the power of 2 should be 9"
    assert power(5, 0) == 1, "Test failed: Any number raised to the power of 0 should be 1"
    assert power(0, 5) == 0, "Test failed: 0 raised to any positive power should be 0"
    assert power(-2, 3) == -8, "Test failed: -2 raised to the power of 3 should be -8"

# Test for invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        power("a", 2)  # Base is a string
    with pytest.raises(TypeError):
        power(2, "b")  # Exponent is a string
    with pytest.raises(TypeError):
        power(None, 2)  # Base is None
    with pytest.raises(TypeError):
        power(2, None)  # Exponent is None