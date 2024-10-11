import sys
from enum import Enum

from commands.user_management import register


class Commands(Enum):
    REGISTER = 'register'


def main():
    if Commands.REGISTER.value in sys.argv:
        register()


if __name__ == '__main__':
    main()




