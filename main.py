from lib import Cli, Gui
from tests import *
import argparse
import unittest

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the program.')
    parser.add_argument('interface', nargs='?', default='cli', help='The interface to use')
    args = parser.parse_args()
    if args.interface == 'cli':
        app = Cli()
        app.menu()
    elif args.interface == 'gui':
        app = Gui()
    elif args.interface == 'tests':
        unittest.main(argv=['first-arg-is-ignored'])
    else:
        raise ValueError("Wrong type of interface")
