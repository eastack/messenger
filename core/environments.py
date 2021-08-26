from enum import Enum, unique, auto

import requests


@unique
class Environments(Enum):
    DEVELOPMENT = auto()
    TESTING = auto()
    STAGING = auto()
    PRODUCTION = auto()


current = Environments.PRODUCTION


def session():
    if current == Environments.DEVELOPMENT:
        development = requests.Session()
        development.headers.update({'hello': 'world'})

        return development
    elif current == Environments.TESTING:
        development = requests.Session()
        development.headers.update({'hello': 'world'})

        return development
    elif current == Environments.STAGING:
        development = requests.Session()
        development.headers.update({'hello': 'world'})

        return development
    elif current == Environments.PRODUCTION:
        development = requests.Session()
        development.headers.update({'hello': 'world'})

        return development


def server():
    if current == Environments.DEVELOPMENT:
        return "https://httpbin.org"
    elif current == Environments.TESTING:
        return "https://httpbin.org"
    elif current == Environments.STAGING:
        return "https://httpbin.org"
    elif current == Environments.PRODUCTION:
        return "https://httpbin.org"
