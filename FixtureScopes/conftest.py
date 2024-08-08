import pytest


# After creating this file, we don't need to write code for setup and teardown code


# @pytest.fixture(autouse=True,scope="function")  # function is default

@pytest.fixture(autouse=True,scope="session")  # The setup code is run only once.



def setup():
    print("Launch Browser")
    print("Open Application URL in browser")
    yield        # This is used to run the below code after the test
    print("Logout from application")
    print("Close Browser")



# When we use  @pytest.fixture(autouse=True)
# We don't need to pass the conftest  method name in other testcase as a attribute.

#     def test_register_with_mandatory_fields(setup):   # setup
#     print("Testing test_register_with_mandatory_fields")