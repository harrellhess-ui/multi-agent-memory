"""A small Celsius-to-Fahrenheit command-line program."""

import argparse
import math


def celsius_to_fahrenheit(celsius):
    """Convert a finite Celsius value; raise ValueError for invalid ranges."""
    if not math.isfinite(celsius):
        raise ValueError('temperature must be finite')
    fahrenheit = celsius * 1.8 + 32
    if not math.isfinite(fahrenheit):
        raise ValueError('converted temperature is out of range')
    return fahrenheit


def main():
    parser = argparse.ArgumentParser(description='Convert Celsius to Fahrenheit.')
    parser.add_argument('celsius', type=float, help='temperature in Celsius')
    args = parser.parse_args()
    try:
        result = celsius_to_fahrenheit(args.celsius)
    except ValueError as error:
        parser.error(str(error))
    print(f'{args.celsius:.2f} C = {result:.2f} F')


if __name__ == '__main__':
    main()
