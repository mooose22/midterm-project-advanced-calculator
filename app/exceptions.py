class CalculatorError(Exception):
    pass


class OperationError(CalculatorError):
    pass


class ValidationError(CalculatorError):
    pass


class HistoryError(CalculatorError):
    pass


class PersistenceError(CalculatorError):
    pass