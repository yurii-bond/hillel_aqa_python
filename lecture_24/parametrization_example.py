import pytest

def add(x, y):
    return x + y

### FIXTURE PARAMS
@pytest.fixture(params=[(1, 2), (5, 5), (10, -5)])
def input_data(request):
    return request.param

def test_addition(input_data):
    x, y = input_data
    result = x + y
    assert add(x, y) == result

#### PARAMETRIZE
@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (10, -5, 5)
    ]
)
def test_add_func(x, y, expected):
    assert add(x, y) == expected

#### INDIRECT

@pytest.fixture
def data(request):
    return request.param * 2

@pytest.mark.parametrize("data", [1, 2, 3], indirect=True)
def test_even(data):
    assert data % 2 == 0