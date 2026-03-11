from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Calculation:
    operation: str
    operand1: float
    operand2: float
    result: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "operation": self.operation,
            "operand1": self.operand1,
            "operand2": self.operand2,
            "result": self.result,
            "timestamp": self.timestamp,
        }

    def __str__(self) -> str:
        return f"{self.operation}({self.operand1}, {self.operand2}) = {self.result}"