from .base import BaseException


class StructException(BaseException):
    """
    Base exception class for all structure exceptions.
    """
    pass


class NotDefinedException(StructException):
    """
    Exception raised when a variable is not defined.
    """
    def __init__(self, variable_name):
        message = "Variable not defined: " + variable_name
        super().__init__(message)


class NotValidException(StructException):
    """
    Exception raised when a variable is not valid.
    """
    def __init__(self, variable_name, actual, expected):
        message = "Variable not valid: " + variable_name + " (actual: " + str(actual) + ", expected: " + str(expected) + ")"
        super().__init__(message)


class NotValidTypeException(StructException):
    """
    Exception raised when a variable is not valid.
    """
    def __init__(self, variable_name, variable_type):
        message = "Variable not valid: " + variable_name + " (" + variable_type + ")"
        super().__init__(message)


class NotUniqueException(StructException):
    """
    Exception raised when a variable is not unique.
    """
    def __init__(self, variable_name):
        message = "Variable ID not unique: " + variable_name
        super().__init__(message)

class NotFoundException(StructException):
    """
    Exception raised when a variable is not found.
    """
    def __init__(self, variable_name, variable_id):
        message = "Variable not found: " + variable_name + " with id: " + str(variable_id)
        super().__init__(message)


class DimensionError(StructException):
    """
    Exception raised when a variable has a wrong dimension.
    """
    def __init__(self, variable1_name, variable1_dimension, variable2_name, variable2_dimension):
        message = "Variable dimension error: " + variable1_name + " (" + str(variable1_dimension) + ") and " + variable2_name + " (" + str(variable2_dimension) + ")"
        super().__init__(message)


# class CoordinateException(StructException):
#     """
#     Exception for invalid coordinates.
#     """
#     def __init__(self, message):
#         super().__init__(message)
