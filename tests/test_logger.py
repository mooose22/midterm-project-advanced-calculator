from app.logger import setup_logger


def test_setup_logger_creates_logger(tmp_path):
    log_file = tmp_path / "calculator.log"
    logger = setup_logger(log_file)

    logger.info("test log message")

    assert log_file.exists()