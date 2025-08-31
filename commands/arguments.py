import argparse
from argparse import Namespace

from commands.trade_command import start_trading


def parse_args(args: list[str] | None) -> Namespace:
    if args is None:
        raise ValueError("The program need arguments to run...")

    parser = argparse.ArgumentParser(
        description="Algo Trader for crypto and stocks",
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    trade_cmd = subparsers.add_parser(
        "trade", help="Start trading"
    )

    parsed_args = parser.parse_args(args)

    trade_cmd.set_defaults(func=start_trading(vars(parsed_args)))

    return parser.parse_args()
