import atexit
import json
import logging
import logging.config
import os
import pathlib

from constants import PROJECT_ROOT


def setup_logging() -> None:
    config_file_path = PROJECT_ROOT / "system" / "logging_config.json"
    log_path = PROJECT_ROOT / "log"

    os.makedirs(log_path, exist_ok=True)
    config_file = pathlib.Path(config_file_path)

    with open(config_file) as f:
        config = json.load(f)

    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")

    if queue_handler:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)
        print("Logger setup successfully")


if __name__ == '__main__':
    setup_logging()
