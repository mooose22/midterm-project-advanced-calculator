from abc import ABC, abstractmethod
from app.exceptions import OperationError


class Operation(ABC):

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass


class AddOperation(Operation):

    def execute(self, a: float, b: float) -> float:
        return a + b


class SubtractOperation(Operation):

    def execute(self, a: float, b: float) -> float:
        return a - b


class MultiplyOperation(Operation):

    def execute(self, a: float, b: float) -> float:
        return a * b


class DivideOperation(Operation):

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a / b


class PowerOperation(Operation):

    def execute(self, a: float, b: float) -> float:
        return a ** b


class RootOperation(Operation):

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Root degree cannot be zero.")

        if a < 0:
            if not float(b).is_integer():
                raise OperationError("Cannot take a fractional root of a negative number.")
            if int(b) % 2 == 0:
                raise OperationError("Cannot take an even root of a negative number.")
            return -((-a) ** (1 / b))

        return a ** (1 / b)


class ModulusOperation(Operation):

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot take modulus by zero.")
        return a % b


class IntegerDivideOperation(Operation):

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot integer divide by zero.")
        return a // b


class PercentageOperation(Operation):

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot calculate percentage with denominator zero.")
        return (a / b) * 100


class AbsoluteDifferenceOperation(Operation):

    def execute(self, a: float, b: float) -> float:
        return abs(a - b)


class OperationFactory:

    _operations = {
        "add": AddOperation,
        "subtract": SubtractOperation,
        "multiply": MultiplyOperation,
        "divide": DivideOperation,
        "power": PowerOperation,
        "root": RootOperation,
        "modulus": ModulusOperation,
        "int_divide": IntegerDivideOperation,
        "percent": PercentageOperation,
        "abs_diff": AbsoluteDifferenceOperation,
    }

    @classmethod
    def create_operation(cls, operation_name: str) -> Operation:
        operation_class = cls._operations.get(operation_name.lower())
        if operation_class is None:
            raise OperationError(f"Invalid operation: {operation_name}")
        return operation_class()

    @classmethod
    def get_supported_operations(cls) -> list[str]:
        return list(cls._operations.keys())