from lib import Cli#, Gui
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the program.')
    parser.add_argument('interface', default='cli', help='The interface to use')
    args = parser.parse_args()
    if args.interface == 'cli':
        app = Cli()
        app.show_all()
    # elif args.interface == 'gui':
    #     app = Gui()
    else:
        raise ValueError("Wrong type of interface")
