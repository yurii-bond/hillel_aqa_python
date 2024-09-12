import pytest


@pytest.fixture(params=[1, 2, 3])
def fixture(request):
    param_value = request.param
    print('Param value', param_value)
    return param_value * 2

def test_using_params_fixture(fixture):
    print('Fixture', fixture)
    assert fixture % 2 == 0

