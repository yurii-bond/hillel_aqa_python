import pytest


@pytest.mark.usefixtures('database_prep', 'config_prep')
class TestClass:
    def test_1(self):
        print('Test 1')

    def test_2(self):
        print('Test 2')
