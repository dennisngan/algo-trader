import logging
from typing import Any

logger = logging.getLogger(__name__)


class Worker:
    def __init__(self, args: dict[str, Any]):
        self.args = args

    def run(self):
        pass

    def exit(self):
        pass
