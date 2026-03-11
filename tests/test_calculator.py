import pytest

from app.calculator import AutoSaveObserver, Calculator, LoggingObserver
from app.calculator_config import CalculatorConfig
from app.exceptions import HistoryError, OperationError, ValidationError


@pytest.fixture
def config(tmp_path):
    return CalculatorConfig()


@pytest.fixture
def calculator():
    calc = Calculator()
    calc.register_observer(LoggingObserver(calc.logger))
    return calc


def test_perform_operation_add(calculator):
    result = calculator.perform_operation("add", 2, 3)

    assert result == 5
    assert len(calculator.history) == 1
    assert calculator.history[0].operation == "add"


def test_perform_operation_divide(calculator):
    result = calculator.perform_operation("divide", 10, 2)

    assert result == 5


def test_invalid_operation(calculator):
    with pytest.raises(OperationError, match="Invalid operation: fake"):
        calculator.perform_operation("fake", 2, 3)


def test_invalid_numeric_input(calculator):
    with pytest.raises(ValidationError, match="Invalid numeric input"):
        calculator.perform_operation("add", "hello", 3)


def test_input_exceeds_max_value():
    calculator = Calculator()
    calculator.config.max_input_value = 100

    with pytest.raises(ValidationError, match="exceeds maximum allowed value"):
        calculator.perform_operation("add", 101, 2)


def test_clear_history(calculator):
    calculator.perform_operation("add", 1, 2)
    calculator.perform_operation("multiply", 3, 4)

    calculator.clear_history()

    assert calculator.history == []


def test_get_history_returns_copy(calculator):
    calculator.perform_operation("add", 1, 2)

    history = calculator.get_history()
    history.append("fake")

    assert len(calculator.history) == 1


def test_undo(calculator):
    calculator.perform_operation("add", 1, 2)
    calculator.perform_operation("multiply", 3, 4)

    calculator.undo()

    assert len(calculator.history) == 1
    assert calculator.history[0].operation == "add"


def test_redo(calculator):
    calculator.perform_operation("add", 1, 2)
    calculator.perform_operation("multiply", 3, 4)

    calculator.undo()
    calculator.redo()

    assert len(calculator.history) == 2
    assert calculator.history[-1].operation == "multiply"


def test_undo_without_history_raises(calculator):
    with pytest.raises(HistoryError, match="Nothing to undo."):
        calculator.undo()


def test_redo_without_history_raises(calculator):
    with pytest.raises(HistoryError, match="Nothing to redo."):
        calculator.redo()


def test_autosave_observer(tmp_path):
    calculator = Calculator()
    calculator.config.auto_save = True
    calculator.config.history_file = tmp_path / "history.csv"
    calculator.register_observer(AutoSaveObserver(calculator))

    calculator.perform_operation("add", 5, 5)

    assert calculator.config.history_file.exists()