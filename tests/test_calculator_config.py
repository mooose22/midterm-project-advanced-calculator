from app.calculator_config import CalculatorConfig


def test_config_defaults():
    config = CalculatorConfig()

    assert config.max_history_size > 0
    assert config.precision >= 0
    assert config.max_input_value > 0
    assert config.default_encoding == "utf-8"