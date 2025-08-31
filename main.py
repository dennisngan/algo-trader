import logging
from typing import Any

from commands import arguments
from system import *

logger = logging.getLogger("algo-trader")


def main(sysarg: list[str] | None = None) -> None:
    # default return code = 1 (default failure)
    return_code: Any = 1

    try:
        setup_logging()
        stepup_asyncio()

        args = arguments.parse_args(args=sysarg)

        if "func" in args:
            return_code = args["func"](args)

    except SystemExit as e:
        print(e)
        return_code = e
    except KeyboardInterrupt:
        print("Interrupted by user")
        return_code = 0
    except Exception as e:
        logger.exception(e)

    finally:
        return return_code


if __name__ == '__main__':
    main(["trade"])
