import pytest

from app.calculator import Calculator
from app.exceptions import HistoryError, OperationError, ValidationError


def test_perform_operation_add():
    calculator = Calculator()
    result = calculator.perform_operation("add", 2, 3)

    assert result == 5
    assert len(calculator.history) == 1
    assert calculator.history[0].operation == "add"


def test_perform_operation_divide():
    calculator = Calculator()
    result = calculator.perform_operation("divide", 10, 2)

    assert result == 5


def test_invalid_operation():
    calculator = Calculator()

    with pytest.raises(OperationError, match="Invalid operation: fake"):
        calculator.perform_operation("fake", 2, 3)


def test_invalid_numeric_input():
    calculator = Calculator()

    with pytest.raises(ValidationError, match="Invalid numeric input"):
        calculator.perform_operation("add", "hello", 3)


def test_input_exceeds_max_value():
    calculator = Calculator(max_input_value=100)

    with pytest.raises(ValidationError, match="exceeds maximum allowed value"):
        calculator.perform_operation("add", 101, 2)


def test_clear_history():
    calculator = Calculator()
    calculator.perform_operation("add", 1, 2)
    calculator.perform_operation("multiply", 3, 4)

    calculator.clear_history()

    assert calculator.history == []


def test_get_history_returns_copy():
    calculator = Calculator()
    calculator.perform_operation("add", 1, 2)

    history = calculator.get_history()
    history.append("fake")

    assert len(calculator.history) == 1


def test_undo():
    calculator = Calculator()
    calculator.perform_operation("add", 1, 2)
    calculator.perform_operation("multiply", 3, 4)

    calculator.undo()

    assert len(calculator.history) == 1
    assert calculator.history[0].operation == "add"


def test_redo():
    calculator = Calculator()
    calculator.perform_operation("add", 1, 2)
    calculator.perform_operation("multiply", 3, 4)

    calculator.undo()
    calculator.redo()

    assert len(calculator.history) == 2
    assert calculator.history[-1].operation == "multiply"


def test_undo_without_history_raises():
    calculator = Calculator()

    with pytest.raises(HistoryError, match="Nothing to undo."):
        calculator.undo()


def test_redo_without_history_raises():
    calculator = Calculator()

    with pytest.raises(HistoryError, match="Nothing to redo."):
        calculator.redo()