import pytest


@pytest.fixture()
def fixture():
    data = {'key': 'value'}
    yield data

def test_using_fixture(fixture):
    assert 'key' in fixture
    assert fixture['key'] == 'value'

