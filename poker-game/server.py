"""
Poker Game Server
=================
"""
from flask import Flask

app = Flask(__name__)


def main(args):
    app.run(
        host='0.0.0.0',
        port=args.port,
        threaded=False,
        debug=args.debug)


if(__name__ == "__main__"):
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-p', '--port',
        help="Port that the server will run on.",
        type=int,
        default=8080)
    parser.add_argument(
        '-d', '--debug',
        help="Whether or not to run in debug mode.",
        default=True,
        action='store_true')

    args = parser.parse_args()
    main(args)
