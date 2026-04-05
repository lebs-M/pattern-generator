import pytest
from io import StringIO
import sys
from patterns import (
    triangle,
    increasing_triangle,
    decreasing_triangle,
    hollow_triangle,
    square,
    grid,
    hollow_grid,
)


def capture(func, *args):
    captured = StringIO()
    sys.stdout = captured
    func(*args)
    sys.stdout = sys.__stdout__
    return captured.getvalue().splitlines()


class TestTriangle:
    def test_row_count(self):
        assert len(capture(triangle, 5)) == 5

    def test_last_row_length(self):
        lines = capture(triangle, 5)
        assert len(lines[-1]) == 5

    def test_custom_symbol(self):
        lines = capture(triangle, 3, "#")
        assert lines[0] == "#"
        assert lines[2] == "###"


class TestIncreasingTriangle:
    def test_row_count(self):
        assert len(capture(increasing_triangle, 4)) == 4

    def test_last_row_is_widest(self):
        lines = capture(increasing_triangle, 4)
        widths = [len(line.strip()) for line in lines]
        assert widths == sorted(widths)


class TestDecreasingTriangle:
    def test_row_count(self):
        assert len(capture(decreasing_triangle, 4)) == 4

    def test_first_row_is_widest(self):
        lines = capture(decreasing_triangle, 4)
        widths = [len(line.strip()) for line in lines]
        assert widths == sorted(widths, reverse=True)


class TestHollowTriangle:
    def test_row_count(self):
        assert len(capture(hollow_triangle, 5)) == 5

    def test_first_row_is_single_symbol(self):
        lines = capture(hollow_triangle, 5)
        assert lines[0] == "*"

    def test_last_row_is_full(self):
        lines = capture(hollow_triangle, 5)
        assert lines[-1] == "*****"


class TestSquare:
    def test_row_count(self):
        assert len(capture(square, 4)) == 4

    def test_all_rows_equal_length(self):
        lines = capture(square, 4)
        assert all(len(line) == 4 for line in lines)


class TestGrid:
    def test_row_count(self):
        assert len(capture(grid, 4)) == 4

    def test_alternating_pattern(self):
        lines = capture(grid, 4)
        assert lines[0][0] == "*"
        assert lines[0][1] == " "


class TestHollowGrid:
    def test_row_count(self):
        assert len(capture(hollow_grid, 5)) == 5

    def test_first_and_last_rows_full(self):
        lines = capture(hollow_grid, 5)
        assert lines[0] == "*****"
        assert lines[-1] == "*****"

    def test_middle_rows_hollow(self):
        lines = capture(hollow_grid, 5)
        for line in lines[1:-1]:
            assert line[0] == "*"
            assert line[-1] == "*"
            assert line[1:-1] == "   "
