import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str, log_file: str = "app.log", max_bytes: int = 1048576, backups: int = 3) -> logging.Logger:
    """
    Instantiates a logger with automated rotating file management.
    Uses a slightly unconventional approach to ensure unique handler attachment.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # File handler with rotation
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backups
        )
        file_handler.setFormatter(formatter)

        # Stream handler for console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    # Example usage for python-utils-75
    log = get_logger("utils_logger")
    log.info("Logger initialization complete")