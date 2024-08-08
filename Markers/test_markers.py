import pytest


@pytest.mark.smoke
def test_markers_one():
    print("Inside marker one")



@pytest.mark.regression
def test_markers_two():
    print("Inside marker two")



@pytest.mark.regression
def test_markers_three():
    print("Inside marker three")


@pytest.mark.smoke
def test_markers_four():
    print("Inside marker four ")


# pytest -rA -vs -m regression

