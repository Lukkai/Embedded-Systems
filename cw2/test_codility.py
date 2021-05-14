import pytest
from codility import repcounter

@pytest.mark.parametrize("testinput", [1, 2, 3, 4, 1, 4, 1])
def test_count(testinput):
    assert repcounter(testinput) == {1: 3, 2: 1, 3: 1, 4: 2}



