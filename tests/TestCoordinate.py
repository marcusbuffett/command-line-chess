import pytest

from src.Coordinate import Coordinate


@pytest.mark.parametrize(
    ['coords', 'other', 'expected'],
    [
        [(1, 1), (1, 1), (2, 2)],
        [(0, 1), (2, 3), (2, 4)],
    ],
)
def testAddition(coords, other, expected):
    assert Coordinate(*coords) + Coordinate(*other) == Coordinate(*expected)


@pytest.mark.parametrize(
    ['coords', 'other', 'expected'],
    [
        [(1, 1), (1, 1), (0, 0)],
        [(0, 1), (2, 3), (-2, -2)],
    ],
)
def testSubtraction(coords, other, expected):
    assert Coordinate(*coords) - Coordinate(*other) == Coordinate(*expected)


@pytest.mark.parametrize(
    ['coords', 'other'],
    [
        [(1, 1), (1, 1)],
        [(0, 1), 42],
    ],
)
def testInvalidInput(coords, other):
    with pytest.raises(Exception):
        _ = Coordinate(*coords) - other
