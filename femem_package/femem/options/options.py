from .general import GeneralOptions
from .draw import DrawOptions
from .optimization import OptimizationOptions
from .csv import CsvOptions


class Options:
    general = GeneralOptions()
    draw = DrawOptions()
    optimization = OptimizationOptions()
    csv = CsvOptions()
