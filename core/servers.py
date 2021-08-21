import configurations
from core.environments import Environments


def server():
    match configurations.ENV:
        case Environments.DEVELOPMENT:
            return "https://httpbin.org/"
        case Environments.TESTING:
            return "https://httpbin.org/"
        case Environments.STAGING:
            return "https://httpbin.org/"
        case Environments.PRODUCTION:
            return "https://httpbin.org/"
