import pytest


@pytest.fixture()
def setup():
    print("Launch Browser")
    print("Open Application URL in browser")
    yield        # This is used to run the below code after the test
    print("Logout from application")
    print("Close Browser")





def test_login_with_valid_credentials(setup):
    print("Testing test_login_with_valid_credentials")



def test_login_with_valid_email_and_invalid_password(setup):
    print("Testing test_login_with_valid_email_and_invalid_password ")

