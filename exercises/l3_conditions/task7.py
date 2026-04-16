# Write the body of the function to make the script work without errors
def grade(score: int) -> str:
    if score >= 95:
        return "A"
    elif score >= 85:
        return "B"
    elif score >= 75:
        return "C"
    elif score >= 65:
        return "D"
    else:
        return "F"



if __name__ == "__main__":
    # Do not change the below asserts
    assert grade(95) == "A"
    assert grade(85) == "B"
    assert grade(75) == "C"
    assert grade(65) == "D"
    assert grade(50) == "F"
