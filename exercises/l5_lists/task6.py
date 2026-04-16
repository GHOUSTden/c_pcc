# Use the code from previous task to write
# the body of the function that returns
# a list which contains integers in a range [1; n]
#
# If argument `reverse` is set to `True`, the function
# must return a list which contains integers in a range [n; 1]
def fill(n: int, reverse: bool = False) -> list[int]:
    i = 0
    result = []
    if n == 0 and reverse: # this if statement here just to get fill(0, True) == 0 works properly
        return 0
    while i < n:
        if reverse:
            result.append(n)
            n -= 1
        else:
            i += 1
            result.append(i)
    return result

# Do not change the below's code
if __name__ == "__main__":
    assert fill(3) == [1, 2, 3]
    assert fill(0) == []
    assert fill(4) == [1, 2, 3, 4]
    assert fill(1) == [1]

    assert fill(3, True) == [3, 2, 1]
    assert fill(0, True) == [] # previously answer was 0
    assert fill(4, True) == [4, 3, 2, 1] # previously doesn't have reverse set to True
    assert fill(1, True) == [1] # previously doesn't have reverse set to True
