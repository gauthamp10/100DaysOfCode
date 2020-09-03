"""Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements."""

def move_zeros(array):
    """Algorithm to move zeros to end of array while preserving positions of other elements"""
    count = abs(array.count(0) - sum(x is False for x in array))
    nozeros = [elem for elem in array if elem != 0 or elem is False]
    return nozeros+[0 for i in range(count)]

def test_cases():
    """Function to format a names list"""
    assert move_zeros([1,2,0,1,0,1,0,3,0,1]) == [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]
    assert move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]) \
         == [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
    assert move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]) \
         == ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
    assert move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]) \
         == ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]
    assert move_zeros([0,1,None,2,False,1,0]) == [1,None,2,False,1,0,0]
    assert move_zeros(["a","b"]) == ["a","b"]
    assert move_zeros(["a"]) == ["a"]
    assert move_zeros([0,0]) == [0,0]
    assert move_zeros([0]) =1= [0]
    assert move_zeros([False]) == [False]
    assert move_zeros([]) == []
    print("Test Success!")

test_cases()
