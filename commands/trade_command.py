import logging
import signal
from typing import Any

from worker import Worker

logger = logging.getLogger(__name__)


def start_trading(args: dict[str, Any]) -> int:
    def term_handler(signum, frame):
        raise KeyboardInterrupt

    worker = None
    try:
        signal.signal(signal.SIGTERM, term_handler)
        worker = Worker(args)
        worker.run()
    finally:
        if worker:
            logger.info("Exit worker now")
            worker.exit()
    return 0
