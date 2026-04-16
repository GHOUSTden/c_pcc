# Add a constructor to the class Vehicle
class Vehicle:
    name: str

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    # Assign the needed value to the variable `c`
    # to make the script work without errors
    c = Vehicle(name = "Mercedes")

    assert isinstance(c, Vehicle)
    assert c.name == "Mercedes"
