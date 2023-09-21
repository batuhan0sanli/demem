from .structure.struct import Struct
from .options.options import Options


class FEMEM:
    def __init__(self, structure: {Struct, list}, femem_options: Options = Options()):
        """
        A Python Library for Finite Element Analysis of Truss Systems with Energy Minimization

        positive x-axis is towards the right
        positive y-axis is towards the top
        positive z-axis is towards the front

        units are in (N - MM - MPa) or (kN - m - GPa)

        Positive elongation means the bar is longer than the member.

        :param structure: Structure object or list
        :param femem_options: Options object
        """
        self.struct = structure
        self.options = femem_options

        self.iter_num = 0
        self.eval_num = 0
        self.csv_list = []
        self.frame_list = []

        self.joints = None
        self.bars = None
        self.loads = None
        self.potential = None

        self.result = None

        self.constructor()

    def constructor(self):
        pass

    def run(self):
        """
        Runs the analysis
        """
        pass

    def run_all(self):
        """
        Runs the analysis and saves the results in csv and draw files
        """
        pass

    def encode_elements(self):
        pass

    def define_elements(self, joints, bars, loads):
        pass

    def struct_constructor(self):
        pass

    def cost(self, disp):
        pass

    def callback(self, x):
        pass

    def optimize(self):
        pass

    def save_csv(self):
        pass

    def save_draw(self):
        pass
