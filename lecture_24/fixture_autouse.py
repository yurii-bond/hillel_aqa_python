import time
from time import sleep

import pytest


@pytest.fixture(scope='function', autouse=True)
def fixture():
    print('Start of the fixture')
    data = {'key': 'value'}
    print(time.time())
    sleep(2)
    yield


class TestClass:


    def test_first(self):
        print(time.time())
        assert True

    def test_second(self):
        print(time.time())
        assert True