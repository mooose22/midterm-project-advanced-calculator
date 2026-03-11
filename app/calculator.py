from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento
from app.exceptions import HistoryError
from app.input_validators import validate_numeric
from app.operations import OperationFactory


class Calculator:
    def __init__(self, max_input_value=1000000, precision=2):
        self.history = []
        self.undo_stack = []
        self.redo_stack = []
        self.max_input_value = max_input_value
        self.precision = precision

    def _save_state(self):
        self.undo_stack.append(CalculatorMemento(self.history))
        self.redo_stack.clear()

    def perform_operation(self, operation_name, a, b):
        operand1 = validate_numeric(a, self.max_input_value)
        operand2 = validate_numeric(b, self.max_input_value)

        operation = OperationFactory.create_operation(operation_name)
        result = round(operation.execute(operand1, operand2), self.precision)

        self._save_state()

        calculation = Calculation(
            operation=operation_name,
            operand1=operand1,
            operand2=operand2,
            result=result,
        )

        self.history.append(calculation)
        return result

    def get_history(self):
        return self.history[:]

    def clear_history(self):
        self._save_state()
        self.history.clear()

    def undo(self):
        if not self.undo_stack:
            raise HistoryError("Nothing to undo.")
        self.redo_stack.append(CalculatorMemento(self.history))
        self.history = self.undo_stack.pop().get_state()

    def redo(self):
        if not self.redo_stack:
            raise HistoryError("Nothing to redo.")
        self.undo_stack.append(CalculatorMemento(self.history))
        self.history = self.redo_stack.pop().get_state()