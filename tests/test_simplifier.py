import pytest

from news360_demo_task.simplifier import simplify


class TestSimplify:
    """simplify"""

    @pytest.mark.parametrize('input, output', [
        ('x^2 + 3.5xy + y = y^2 - xy + y', 'x^2 + 4.5xy - y^2 = 0'),
        ('X^2 + x = 10', '- 10.0 + X^2 + x = 0'),
        ('(10 + x) - y^2 = 11', '- 1.0 + x - y^2 = 0'),
        ('(10 + xy) - xy^2 = 11', '- 1.0 + xy - xy^2 = 0'),
        ('(10 + xy) - x^2y^2 = 11', '- 1.0 - x^2y^2 + xy = 0'),
    ])
    def test_ok(self, input, output):
        """возвращает упрощенную форму уравнения."""
        assert simplify(input) == output

    @pytest.mark.parametrize('input, message', [
        ('(10 + x) - (y^2 = 11', 'Unpaired parentheses'),
        (')10 + x - y^2 = 11', 'Unpaired parentheses'),
        ('x = y = z', 'x = y = z is not valid equation'),
        ('52x12y = 10', 'Invalid addendum 52x12y'),
        ('52xy^hello = 10', 'Invalid addendum 52xy^hello'),
    ])
    def test_not_ok(self, input, message):
        """возвращает SyntaxError, если уравнение некорректно."""
        with pytest.raises(SyntaxError) as excinfo:
            simplify(input)
        assert str(excinfo.value) == message
