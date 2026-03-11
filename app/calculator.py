from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.calculator_memento import CalculatorMemento
from app.exceptions import HistoryError
from app.history import HistoryManager
from app.input_validators import validate_numeric
from app.logger import setup_logger
from app.operations import OperationFactory


class LoggingObserver:
    def __init__(self, logger):
        self.logger = logger

    def update(self, calculation):
        self.logger.info(
            "Calculation performed | operation=%s operand1=%s operand2=%s result=%s",
            calculation.operation,
            calculation.operand1,
            calculation.operand2,
            calculation.result,
        )


class AutoSaveObserver:
    def __init__(self, calculator):
        self.calculator = calculator

    def update(self, calculation):
        if self.calculator.config.auto_save:
            self.calculator.save_history()


class Calculator:
    def __init__(self, config=None):
        self.config = config or CalculatorConfig()
        self.logger = setup_logger(self.config.log_file)
        self.history = []
        self.undo_stack = []
        self.redo_stack = []
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, calculation):
        for observer in self.observers:
            observer.update(calculation)

    def _save_state(self):
        self.undo_stack.append(CalculatorMemento(self.history))
        self.redo_stack.clear()

    def perform_operation(self, operation_name, a, b):
        operand1 = validate_numeric(a, self.config.max_input_value)
        operand2 = validate_numeric(b, self.config.max_input_value)

        operation = OperationFactory.create_operation(operation_name)
        result = round(operation.execute(operand1, operand2), self.config.precision)

        self._save_state()

        calculation = Calculation(
            operation=operation_name,
            operand1=operand1,
            operand2=operand2,
            result=result,
        )

        self.history.append(calculation)

        if len(self.history) > self.config.max_history_size:
            self.history = self.history[-self.config.max_history_size :]

        self.notify_observers(calculation)
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

    def save_history(self):
        HistoryManager.save_to_csv(
            self.history,
            self.config.history_file,
            self.config.default_encoding,
        )

    def load_history(self):
        self._save_state()
        self.history = HistoryManager.load_from_csv(
            self.config.history_file,
            self.config.default_encoding,
        )

def get_help_text():
    return "\n".join(
        [
            "Available commands:",
            "add <a> <b>",
            "subtract <a> <b>",
            "multiply <a> <b>",
            "divide <a> <b>",
            "power <a> <b>",
            "root <a> <b>",
            "modulus <a> <b>",
            "int_divide <a> <b>",
            "percent <a> <b>",
            "abs_diff <a> <b>",
            "history",
            "clear",
            "undo",
            "redo",
            "save",
            "load",
            "help",
            "exit",
        ]
    )

def run_repl():  # pragma: no cover
    calculator = Calculator()
    calculator.register_observer(LoggingObserver(calculator.logger))
    calculator.register_observer(AutoSaveObserver(calculator))

    print("Advanced Calculator REPL")
    print("Type 'help' to see available commands.")

    while True:
        try:
            user_input = input(">>> ").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                print("Goodbye.")
                break

            if command == "help":
                print(get_help_text())
                continue

            if command == "history":
                if not calculator.history:
                    print("No calculation history.")
                else:
                    for index, calculation in enumerate(calculator.history, start=1):
                        print(f"{index}. {calculation}")
                continue

            if command == "clear":
                calculator.clear_history()
                print("History cleared.")
                continue

            if command == "undo":
                calculator.undo()
                print("Undo successful.")
                continue

            if command == "redo":
                calculator.redo()
                print("Redo successful.")
                continue

            if command == "save":
                calculator.save_history()
                print("History saved.")
                continue

            if command == "load":
                calculator.load_history()
                print("History loaded.")
                continue

            if command in OperationFactory.get_supported_operations():
                if len(parts) != 3:
                    print("This command requires exactly two numeric inputs.")
                    continue

                result = calculator.perform_operation(command, parts[1], parts[2])
                print(f"Result: {result}")
                continue

            print(f"Unknown command: {command}")

        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":  # pragma: no cover
    run_repl()   