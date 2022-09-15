import pytest

@pytest.fixture()
def get_str_fixture():
    """
    Returns a String
    """
    return "Return String"

@pytest.fixture(scope='module')
def get_list_fixture():
    """
    Yields a list and cleans after
    """
    l = ['a', 'b']
    print(f"\nSETUP: i have list {l}")
    yield l
    l.clear()
    print(f"\nTEARDOWN: i have list {l}")


def test_list(get_list_fixture):
    assert isinstance(get_list_fixture, list)
    assert get_list_fixture[0] == 'a'
    assert get_list_fixture[1] == 'b'

def test_str(get_str_fixture):
    assert isinstance(get_str_fixture, str)
    assert get_str_fixture == 'Return String'

