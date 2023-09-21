class DrawGeneralOptions:
    fps: int = 15
    dpi: int = 300
    # screen_width: int = 800
    # screen_height: int = 600
    # screen_title: str = ''
    save_path: str = './'
    temp_path: str = './'


class FirstCaseOptions:
    draw_first_case: bool = False
    first_case_name: str = 'FirstCase'


class LastCaseOptions:
    draw_last_case: bool = False
    last_case_name: str = 'LastCase'


class GhostCaseOptions:
    draw_ghost_case: bool = True
    ghost_case_name: str = 'GhostCase'


class AnimationOptions:
    draw_animation: bool = False
    animation_name: str = 'Animation'


class GridOptions:
    draw_grid: bool = True


class CustomGridOptions:
    draw_custom_grid: bool = False
    custom_grid_x: list = []
    custom_grid_y: list = []
    custom_grid_z: list = []


class AxisOptions:
    x_label_name: str = 'X Axis'
    y_label_name: str = 'Y Axis'
    z_label_name: str = 'Z Axis'
    axis_label_font_family: str = 'Times New Roman'


class JointsOptions:
    draw_joints: bool = True
    joints_color: str = 'red'
    joints_order: int = 4


class BarsOptions:
    draw_bars: bool = True
    bars_color: str = 'orange'
    bars_order: int = 3


class LoadsOptions:
    draw_loads: bool = True
    loads_color: str = 'green'
    loads_order: int = 5
    loads_scale: float = 30


class AnnotateOptions:
    draw_annotate: bool = True
    annotate_color: str = 'black'
    annotate_order: int = 7


class NameOptions:
    file_name_modules: list = ['prefix', 'method', 'attempt', 'runtime', 'case_name']  # Fields: prefix, suffix, method, attempt, runtime, date, iteration, evaluation, potential, weight, case_name
    separator: str = "_"
    image_extension: str = ".png"
    animation_extension: str = ".gif"
    prefix: str = 'general_name'
    suffix: str = ""


class ImageFormatOptions:
    runtime_format: str = '%.2f'
    attempt_format: str = '%04d'
    iteration_format: str = '%04d'
    evaluation_format: str = '%04d'
    potential_format: str = '%04d'
    weight_format: str = '%04d'
    date_format: str = '%Y-%m-%d-%H-%M-%S'


class DrawOptions(
    DrawGeneralOptions,
    FirstCaseOptions,
    LastCaseOptions,
    GhostCaseOptions,
    AnimationOptions,
    GridOptions,
    CustomGridOptions,
    AxisOptions,
    JointsOptions,
    BarsOptions,
    LoadsOptions,
    AnnotateOptions,
    NameOptions,
    ImageFormatOptions
):
    pass
