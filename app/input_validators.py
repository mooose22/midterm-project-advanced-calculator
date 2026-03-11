from app.exceptions import ValidationError


def validate_numeric(value, max_input_value):

    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValidationError(f"Invalid numeric input: {value}")

    if abs(number) > max_input_value:
        raise ValidationError(
            f"Input {number} exceeds maximum allowed value of {max_input_value}"
        )

    return number