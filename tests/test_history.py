from pathlib import Path

import pytest

from app.calculation import Calculation
from app.exceptions import PersistenceError
from app.history import HistoryManager


def test_save_and_load_history(tmp_path: Path):
    history = [
        Calculation("add", 2, 3, 5, "2026-03-10"),
        Calculation("multiply", 4, 5, 20, "2026-03-10"),
    ]

    file_path = tmp_path / "history.csv"

    HistoryManager.save_to_csv(history, file_path)

    loaded_history = HistoryManager.load_from_csv(file_path)

    assert len(loaded_history) == 2
    assert loaded_history[0].operation == "add"
    assert loaded_history[1].operation == "multiply"


def test_load_history_missing_file_raises():
    with pytest.raises(PersistenceError, match="Failed to load history"):
        HistoryManager.load_from_csv("missing_file.csv")


def test_save_history_invalid_path_raises():
    history = [Calculation("add", 1, 2, 3, "2026-03-10")]

    with pytest.raises(PersistenceError, match="Failed to save history"):
        HistoryManager.save_to_csv(history, "/invalid_path/history.csv")