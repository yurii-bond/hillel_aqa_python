import pytest


class TestClass:
    @pytest.fixture(scope='class')
    def fixture(self):
        print('Start of the fixture')
        data = {'key': 'value'}
        yield data

    def test_first(self, fixture):
        assert 'key' in fixture
        assert fixture['key'] == 'value'

    def test_second(self, fixture):
        assert 'key' in fixture
        assert fixture['key'] == 'value'