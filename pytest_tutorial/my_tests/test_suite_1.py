import pytest


@pytest.mark.login
@pytest.mark.smoke
def test_login_page_valid_user():
    print("login with valid user")
    print("function : aaa")


@pytest.mark.login
def test_login_page_wrong_password():
    print("login with wrong password")
    print("function : bbbb")
    assert 1 == 2, 'one is not two'
