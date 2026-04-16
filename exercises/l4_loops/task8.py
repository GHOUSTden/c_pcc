# Use `for` loop to calculate the amount
# of positive number in a list of integers `n`
def count_positive(n: list[int]) -> int:
    cnt = 0
    for v in n:
        if v > 0:
            cnt += 1
    return cnt

# Do not change the below's code
if __name__ == "__main__":
    assert count_positive([1, 2, -3, -4]) == 2
    assert count_positive([-1, -2, -3]) == 0
    assert count_positive([4, 5, 4, 3]) == 4
