import pytest

from app.exceptions import OperationError
from app.operations import (
    AbsoluteDifferenceOperation,
    AddOperation,
    DivideOperation,
    IntegerDivideOperation,
    ModulusOperation,
    MultiplyOperation,
    OperationFactory,
    PercentageOperation,
    PowerOperation,
    RootOperation,
    SubtractOperation,
)


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        (AddOperation(), 2, 3, 5),
        (SubtractOperation(), 8, 3, 5),
        (MultiplyOperation(), 4, 5, 20),
        (DivideOperation(), 10, 2, 5),
        (PowerOperation(), 2, 3, 8),
        (RootOperation(), 27, 3, 3),
        (ModulusOperation(), 10, 3, 1),
        (IntegerDivideOperation(), 10, 3, 3),
        (PercentageOperation(), 25, 200, 12.5),
        (AbsoluteDifferenceOperation(), 4, 10, 6),
    ],
)
def test_operations(operation, a, b, expected):
    assert operation.execute(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(OperationError, match="Cannot divide by zero."):
        DivideOperation().execute(10, 0)


def test_root_degree_zero():
    with pytest.raises(OperationError, match="Root degree cannot be zero."):
        RootOperation().execute(16, 0)


def test_even_root_negative_number():
    with pytest.raises(OperationError, match="Cannot take an even root of a negative number."):
        RootOperation().execute(-16, 2)


def test_fractional_root_negative_number():
    with pytest.raises(OperationError, match="Cannot take a fractional root of a negative number."):
        RootOperation().execute(-16, 2.5)


def test_modulus_by_zero():
    with pytest.raises(OperationError, match="Cannot take modulus by zero."):
        ModulusOperation().execute(10, 0)


def test_integer_divide_by_zero():
    with pytest.raises(OperationError, match="Cannot integer divide by zero."):
        IntegerDivideOperation().execute(10, 0)


def test_percent_by_zero():
    with pytest.raises(OperationError, match="Cannot calculate percentage with denominator zero."):
        PercentageOperation().execute(10, 0)


def test_factory_valid_operation():
    operation = OperationFactory.create_operation("add")
    assert isinstance(operation, AddOperation)


def test_factory_invalid_operation():
    with pytest.raises(OperationError, match="Invalid operation: fake"):
        OperationFactory.create_operation("fake")


def test_get_supported_operations():
    operations = OperationFactory.get_supported_operations()

    assert "add" in operations
    assert "subtract" in operations
    assert "multiply" in operations
    assert "divide" in operations
    assert "power" in operations
    assert "root" in operations
    assert "modulus" in operations
    assert "int_divide" in operations
    assert "percent" in operations
    assert "abs_diff" in operations