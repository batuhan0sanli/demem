# FEMEM v1.0.0 with Example Code


## Requeriments
- [numpy](https://pypi.org/project/numpy/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [scipy](https://pypi.org/project/scipy/)
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
The unit system is designed to be user-selectable. The system operates without units. For compatibility, it is recommended to use one of the following two unit systems:
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
The structure is defined by specifying the properties of material, node, support, section, member, load, and deformation in order.

- **Material:** Material begin by defining whether they are linear or non-linear. Then specify the modulus of elasticity and input the unit weight.
- **Joints:** Nodes are defined with a unique node number first, followed by their X, Y, and -if applicable- Z coordinates.
- **Supports:** Supports are defined with a unique node number first, followed by the support conditions in the X, Y, and -if applicable- Z directions. The support conditions are defined as follows:
    - 0: free
    - 1: fixed
- **Sections:** Sections can be listed in the desired order within a list.
- **Bars:** Bars are defined by their unique member number first, followed by the associated section, and then the start and end node numbers.
- **Loads:** Loads are defined by indicating the corresponding node first, followed by the values of the load in the X, Y, and -if applicable- Z directions.
- **Elongations:** Elongations are defined by indicating the relevant member first, followed by the deformation amount. "+" denotes elongation, and "-" denotes contraction.



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
