from .base import BaseException


class ConfigException(BaseException):
    """
    Exception for options errors
    """
    pass


class ConfigNotFoundException(ConfigException):
    """
    Exception for options not found errors
    """
    pass


class ConfigNotValidException(ConfigException):
    """
    Exception for options not valid errors
    """
    pass
