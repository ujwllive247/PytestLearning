


def test_flags_one():
    print("Inside flag one ")

def test_flags_two():
    print("Inside flag two")
    # assert False  # intentionally , we failed the test case (pytest -v or pytest -rA

def test_flags_three():
    print("Inside sample three")


# for details information of result - pytest -v  {v stands for verbose)
# To take output in the console -  command -   pytest -rA
# pytest -k "one or two"   (method 1 and 2 are running remaining deselected)

# pytest -k "not one"  (test 1 is deselected and remaining will be run)