# unit testing for Assignment 5
# updated to work for object oriented code

import pytest


def test_sum():
    from Assignment05 import List
    List1 = List([1,3,5,7,9])
    List2 = List([-2,-5,-6,-1])
    List3 = List([4,-6,9,-1])
    List4 = List([2.2, 5.1 ,9.1, 1.2])
    List5 = List([-1.1, -5.2, -1.4, -3.8])
    List6 = List([-1.1,2.2,-3.1])
    assert List1.get_sum() == 25 
    assert List2.get_sum() == -14
    assert List3.get_sum() == 6
    assert List4.get_sum() == pytest.approx(17.6)
    assert List5.get_sum() == pytest.approx(-11.5)
    assert List6.get_sum() == pytest.approx(-2)
    # check to see if List.getsum gives a None to see if Type Error was raised
    assert List(['hello','hi', 'test']).get_sum() == None   
    assert List([]).get_sum() == None    
    
# Second function
def test_return_min_max():
    from Assignment05 import List
    test_input_list = ([-1,5,8,100],[5,-8,9,45,88,34,65],[-5,8.234,-99023,342,9.452])
    test_output_values = ((100,-1),(88,-8),(342,-99023))

    for count, elem in enumerate(test_input_list):   #enuerate itirate and gives the index
        TempList = List(elem)
        min_max_output = TempList.min_max()
        assert min_max_output == test_output_values[count]
        assert isinstance(min_max_output, tuple) == True 

def test_return_min_max_exceptions():
    from Assignment05 import List
    assert List(['hello', 'hi', 'test']).min_max() == None
    assert List([]).min_max() == None


def test_max_diff():
    from Assignment05 import List
    test_input_list = [[10, 8, 5, 17, 16], [2, -7, 1.5]]
    test_output_value = [12, 9]
    for n, t in enumerate(test_input_list):
        TestList = List(t)
        test_output = TestList.max_diff()
        assert test_output == test_output_value[n]
    
    assert List(['hello', 'hi', 'test']).max_diff() == None
    # type error check
    assert List([1]).max_diff() == None
    #  value error check    
    with pytest.raises(ImportError):  # Test ImportError?
        import scipy
        


