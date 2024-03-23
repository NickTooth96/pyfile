import pytest
import src.parse as parse


print(parse.string_distance("hello", "world")) 

# The test_string_distance function is a parameterized test that tests the string_distance function with different inputs.
@pytest.mark.parametrize("test_input_0,test_input_1,expected", 
                         [("hello", "world", 4), 
                          ("hello", "hello", 0), 
                          ("", "hello", 5)])
def test_string_distance(test_input_0,test_input_1, expected):
    assert parse.string_distance(test_input_0,test_input_1) == expected