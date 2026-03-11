from copy import deepcopy


class CalculatorMemento:
    def __init__(self, history):
        self._history = deepcopy(history)

    def get_state(self):
        return deepcopy(self._history)