from app.calculation import Calculation


def test_calculation_to_dict():
    calculation = Calculation("add", 2, 3, 5, "2026-03-10T12:00:00")

    result = calculation.to_dict()

    assert result["operation"] == "add"
    assert result["operand1"] == 2
    assert result["operand2"] == 3
    assert result["result"] == 5
    assert result["timestamp"] == "2026-03-10T12:00:00"


def test_calculation_str():
    calculation = Calculation("multiply", 4, 5, 20, "2026-03-10T12:00:00")

    assert str(calculation) == "multiply(4, 5) = 20"