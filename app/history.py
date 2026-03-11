import pandas as pd

from app.calculation import Calculation
from app.exceptions import PersistenceError


class HistoryManager:

    @staticmethod
    def save_to_csv(history, file_path, encoding="utf-8"):
        try:
            df = pd.DataFrame([calc.to_dict() for calc in history])
            df.to_csv(file_path, index=False, encoding=encoding)
        except Exception as e:
            raise PersistenceError(f"Failed to save history: {e}")

    @staticmethod
    def load_from_csv(file_path, encoding="utf-8"):
        try:
            df = pd.read_csv(file_path, encoding=encoding)

            history = []
            for _, row in df.iterrows():
                history.append(
                    Calculation(
                        operation=row["operation"],
                        operand1=row["operand1"],
                        operand2=row["operand2"],
                        result=row["result"],
                        timestamp=row["timestamp"],
                    )
                )

            return history

        except Exception as e:
            raise PersistenceError(f"Failed to load history: {e}")