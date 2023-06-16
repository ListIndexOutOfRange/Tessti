import argparse


def add(a: int, b: int) -> int:
    print(f'Inputs: {a=}, {b=}')
    print(f'Output: {a+b=}')
    return a + b


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser('Demo')
    parser.add_argument('-a', type=int, required=True)
    parser.add_argument('-b', type=int, required=True)
    return parser.parse_args()


if __name__ == '__main__':
    add(**vars(parse_args()))
