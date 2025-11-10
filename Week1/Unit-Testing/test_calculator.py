# Pytest expects certain conventions for easy test discovery
# Name the file with your tests for a specific module 
# "test_module.py" OR "module_test.py" - otherwise it might have trouble
# finding your tests automatically

# In order to write tests with pytest, I need to import atleast 2 things:
# 1. pytest itself
# 2. the code from the module you are testing

# Unit tests directly call the code under test. This introduces
# some considerations when your code talks to other outside systems
# like APIs or databases. For now we keep it simple. 

import pytest
from calculator import add, subtract, multiply, divide

# Within our test.py module/file - we want to keep respecting naming conventions
# These are just python methods. But we name them as follows
# test_{method-name}_{what-you're-testing-for}
def test_divide_success():
    
    # Unit tests generally follow the A-A-A pattern
    # Arrange, Act, Assert
    
    # Arrange - any variables or test data that we need to set up
    # is created in this step
    x = 4
    y = 2
    
    # Act - Here is where we actually call the code under test
    result = divide(x, y)
    
    # Assert - We know what data we fed in, we know what we SHOULD get back
    # we assert that we got our expected result back
    assert result == 2
    
    
def test_divide_divide_by_zero_exception():
    
    # Arrange
    x = 400
    y = 0 # Intentionally dividing by zero
    
    # Act - Assert
    with pytest.raises(ValueError) as ex: 
        divide(x, y) # Inside this with - we call the method
        
    # Casting ex.value as a string, to allow for easy comparison
    assert str(ex.value) == "Cannot divide by zero"
    
def test_add():
    
    # Arrange
    x = 4
    y = 6
    # Act
    result = add(x, y)
    
    # Assert
    assert result == 10