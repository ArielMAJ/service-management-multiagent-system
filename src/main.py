import argparse

from src.algorithms import options
from src.simulation import Simulation


def main():
    parser = argparse.ArgumentParser(
        description="Simulation of edge computing algorithms"
    )
    parser.add_argument(
        "--algorithm",
        "-a",
        choices=options.keys(),
        help="Select algorithm",
        required=True,
    )
    args = parser.parse_args()

    Simulation(options[args.algorithm]).run()


if __name__ == "__main__":
    main()
