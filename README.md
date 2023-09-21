# FEMEM v1.0.0

FEMEM (Finite Element Method with Energy Minimization) is a customized finite element solver designed for civil
engineering applications but adaptable to various engineering disciplines. This powerful tool is based on the energy
minimization method, tailored to solve complex engineering problems. Additionally, it serves as a master's thesis
project, offering valuable insights to engineering students and professionals alike.

## Features

- 2D and 3D structures
- Linear and non-linear materials
- Section properties
- Elongations and contractions
- Visualization
- Export to GIF
- Export to PNG
- Export to CSV

### Notes

This project has been precompiled for Python 3.8 on `x86_64 Linux`, `MacOS` and `amd64 Windows`.

All examples solved in the thesis are defined in the `example_structures` folder. The results of the examples are
located in the `thesis_results` folder. The results of the examples can be reproduced by running
the `run_for_thesis_with_example_structures.py` file in the main folder.

The `example_structures` folder contains the following examples:

- **Example 1a**: 11 bar, 2 Support 2D Stable Structure
- **Example 1b**: 11 bar, 1 Support 2D Unstable Structure
- **Example 2a**: 15 bar, 4 Support 2D Stable Structure
- **Example 2b**: 15 bar, 1 Support 2D Unstable Structure
- **Example 3a**: 32 bar, 2 Support 2D Stable Structure
- **Example 3b**: 32 bar, 1 Support 2D Unstable Structure
- **Example 5a**: 16 bar, 4 Support 3D Stable Structure
- **Example 6a**: 12 bar, 1 Support 3D Unstable Structure
- **Example 7a**: 48 bar, 1 Support 3D Unstable Structure

## Example

|                                                                                                     |                                                                                                        |                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ![Structure](./thesis_results/draws/example1a_method(BFGS)_attempt(0001)_runtime(0.29)_FirstCase.png) | ![ResultDraw](./thesis_results/draws/example1a_method(BFGS)_attempt(0001)_runtime(0.29)_GhostCase.png) | <p align="center">[Click to see animation](./thesis_results/animations/example1a_method(BFGS)_attempt(0001)_runtime(0.29)_Animation.gif)</p>     |
| <p align="center">Structure 1a</p>                                                                  | <p align="center">Result 1a (Draw)</p>                                                                 | <p align="center">Result 1a (Animation)</p>                                                                                                  |
| ![Structure](./thesis_results/draws/example1b_method(BFGS)_attempt(0001)_runtime(0.51)_FirstCase.png) | ![ResultDraw](./thesis_results/draws/example1b_method(BFGS)_attempt(0001)_runtime(0.51)_GhostCase.png) | <p align="center">[Click to see animation](./thesis_results/animations/example1b_method(BFGS)_attempt(0001)_runtime(0.51)_Animation.gif)</p> |
| <p align="center">Structure 1b</p>                                                                  | <p align="center">Result 1b (Draw)</p>                                                                 | <p align="center">Result 1b (Animation)</p>                                                                                                  |

---

# Installation

## Requeriments

- [Python 3.8](https://www.python.org/downloads/release/python-380/)
- [NumPy](https://pypi.org/project/numpy/)
- [Matplotlib](https://pypi.org/project/matplotlib/)
- [SciPy](https://pypi.org/project/scipy/)
- [imageio](https://pypi.org/project/imageio/)

## Install

For installation, please follow the instructions below:

1. Install the latest version of FEMEM from local repository.

```
$ pip install ./femem_package
```

2. Ensure that the `femem` package is installed.

```
$ python -c "import femem"
```

3. Enjoy!

## Define Structure

### Unit System

The unit system is designed to be user-selectable. The system operates without units. For compatibility, it is
recommended to use one of the following two unit systems:

- N - mm - MPa
- kN - m - GPa

### Direction

The direction of the structure is defined as follows:
In the case of a 2D structure, the direction is defined as follows:

- **x:** horizontal direction (left to right)
- **y:** vertical direction (bottom to top)

In the case of a 3D structure, the direction is defined as follows:

- **x:** horizontal direction (left to right)
- **y:** depth direction (front to back)
- **z:** vertical direction (bottom to top)

### Structure

The structure is defined by specifying the properties of material, node, support, section, member, load, and deformation
in order.

- **Material:** Material begin by defining whether they are linear or non-linear. Then specify the modulus of elasticity
  and input the unit weight.
- **Joints:** Nodes are defined with a unique node number first, followed by their X, Y, and -if applicable- Z
  coordinates.
- **Supports:** Supports are defined with a unique node number first, followed by the support conditions in the X, Y,
  and -if applicable- Z directions. The support conditions are defined as follows:
    - 0: free
    - 1: fixed
- **Sections:** Sections can be listed in the desired order within a list.
- **Bars:** Bars are defined by their unique member number first, followed by the associated section, and then the start
  and end node numbers.
- **Loads:** Loads are defined by indicating the corresponding node first, followed by the values of the load in the X,
  Y, and -if applicable- Z directions.
- **Elongations:** Elongations are defined by indicating the relevant member first, followed by the deformation
  amount. "+" denotes elongation, and "-" denotes contraction.

## Usage

### Basic Usage

Run analysis.

```
from femem import FEMEM

structure = [..., ..., ...]

res = FEMEM(structure).run()
print(res.result)
```

### Advanced Usage

Run analysis with different parameters.

```
import femem

structure = [..., ..., ...]

options = Options()
options.optimization.method = 'L-BFGS-B'
options.optimization.max_iterations = 100

res = femem.FEMEM(structure, options).run()
print(res.result)
```

### Save Result

Save the result to a file.

```
import femem

structure = [..., ..., ...]

options = Options()
options.draw.save_path = './exports/draw/'
options.csv.save_path = './exports/csv/'
options.draw.draw_animation = True

FEMEM(structure).run_all()
```
