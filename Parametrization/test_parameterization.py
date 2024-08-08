import pytest


@pytest.mark.parametrize("username, password",[("Varun","1234"),("Tarun","12345"),("Arun","53342")])
def test_parametrization_01(username,password):
    print(username+" "+password)
