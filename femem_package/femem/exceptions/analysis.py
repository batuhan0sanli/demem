from .base import BaseException


class AnalysisException(BaseException):
    """
    Analysis Exception
    """
    pass


class AnalysisNotReadyException(AnalysisException):
    """
    Analysis is not ready
    """
    pass


class AnalysisNotRunException(AnalysisException):
    """
    Analysis has not been run
    """
    pass
