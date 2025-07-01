import database
import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(description="Add a new session", dest="session", required=True)
session_command = subparser.add_parser("session", help="Add a new session")
session_command.add_argument("-s", "--seconds", help="The amount of seconds", type=int, required=True)
session_command.add_argument("-l", "--learned", help="What you learned", type=str, required=True)


args = parser.parse_args()


