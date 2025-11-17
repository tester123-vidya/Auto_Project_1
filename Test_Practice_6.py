import pytest


@pytest.fixture
def set_up():
    print("enter user name")
    print("enter password")
    yield
    print("logout")
    print("Close the browser")

def test_login(set_up):
    print("Used logged in successfully")

