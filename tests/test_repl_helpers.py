from app.calculator import get_help_text


def test_help_text_contains_required_commands():
    help_text = get_help_text()

    assert "add <a> <b>" in help_text
    assert "subtract <a> <b>" in help_text
    assert "multiply <a> <b>" in help_text
    assert "divide <a> <b>" in help_text
    assert "power <a> <b>" in help_text
    assert "root <a> <b>" in help_text
    assert "modulus <a> <b>" in help_text
    assert "int_divide <a> <b>" in help_text
    assert "percent <a> <b>" in help_text
    assert "abs_diff <a> <b>" in help_text
    assert "history" in help_text
    assert "clear" in help_text
    assert "undo" in help_text
    assert "redo" in help_text
    assert "save" in help_text
    assert "load" in help_text
    assert "help" in help_text
    assert "exit" in help_text