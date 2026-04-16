# Use `while` loop to calculate the number
# of digits in a number `n`
def count_digits(n: int) -> int:
    if not n:
        return 1

    cnt = 0
    while n > 0:
        n //= 10
        cnt += 1
    return cnt


# Do not change the below's code
if __name__ == "__main__":
    assert count_digits(0) == 1
    assert count_digits(134) == 3
    assert count_digits(54) == 2
    assert count_digits(55678) == 5
