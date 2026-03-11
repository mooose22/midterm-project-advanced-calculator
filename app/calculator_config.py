import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class CalculatorConfig:
    def __init__(self):
        self.log_dir = Path(os.getenv("CALCULATOR_LOG_DIR", "logs"))
        self.history_dir = Path(os.getenv("CALCULATOR_HISTORY_DIR", "history"))
        self.log_file = Path(os.getenv("CALCULATOR_LOG_FILE", self.log_dir / "calculator.log"))
        self.history_file = Path(
            os.getenv("CALCULATOR_HISTORY_FILE", self.history_dir / "calculations.csv")
        )
        self.max_history_size = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))
        self.auto_save = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
        self.precision = int(os.getenv("CALCULATOR_PRECISION", "2"))
        self.max_input_value = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1000000"))
        self.default_encoding = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.history_dir.mkdir(parents=True, exist_ok=True)