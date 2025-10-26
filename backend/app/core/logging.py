import os
import logging
from pythonjsonlogger import jsonlogger
from logging.handlers import RotatingFileHandler


def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_file = os.getenv("LOG_FILE", "logs/app.log")
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Create rotating file handler (5 MB per file, 5 backups)
    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=5
    )

    # JSON formatter for structured logs (good for ELK / Loki / Grafana)
    json_formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    rotating_handler.setFormatter(json_formatter)

    # Console handler for local dev
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    console_handler.setFormatter(console_formatter)

    # Apply configuration
    logging.basicConfig(level=log_level, handlers=[
                        rotating_handler, console_handler])

    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)

    logging.info("✅ Logging initialized successfully")
