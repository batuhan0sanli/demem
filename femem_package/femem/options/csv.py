class CsvGeneralOptions:
    save_csv: bool = True
    save_path: str = "./"
    delimiter: str = ","


class NameOptions:
    file_name_modules: list = ['prefix', 'method', 'attempt', 'runtime']  # Fields: prefix, suffix, method, attempt, runtime, date, iteration, evaluation, potential, weight
    separator: str = "_"
    extension: str = ".csv"
    prefix: str = 'general_name'
    suffix: str = ""


class CsvFormatOptions:
    runtime_format: str = '%.2f'
    attempt_format: str = '%04d'
    iteration_format: str = '%04d'
    evaluation_format: str = '%04d'
    potential_format: str = '%04d'
    weight_format: str = '%04d'
    date_format: str = '%Y-%m-%d-%H-%M-%S'


class CsvOptions(
    CsvGeneralOptions,
    NameOptions,
    CsvFormatOptions
):
    pass