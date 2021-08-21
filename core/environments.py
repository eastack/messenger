from enum import Enum, unique, auto


@unique
class Environments(Enum):
    DEVELOPMENT = auto()
    TESTING = auto()
    STAGING = auto()
    PRODUCTION = auto()
