import time
import femem_package.femem as femem
import example_structures

NUM_ATTEMPTS = 1
METHODS = ['BFGS', 'SLSQP', 'CG', 'Powell', 'TNC']
STRUCTURE_LIST = {
    'example1a': example_structures.example1a,
    'example1b': example_structures.example1b,
    'example2a': example_structures.example2a,
    'example2b': example_structures.example2b,
    'example3a': example_structures.example3a,
    'example3b': example_structures.example3b,
    'example5a': example_structures.example5a,
    'example6a': example_structures.example6a,
    'example7a': example_structures.example7a,
}


def run_one(structure, attempt, name, method):
    options = femem.Options()
    options.optimization.method = method
    options.draw.save_path = 'exports/draw/'
    options.csv.save_path = 'exports/csv/'
    options.general.name = name
    options.general.attempt = attempt
    options.draw.draw_first_case = True
    options.draw.draw_last_case = False
    options.draw.draw_animation = True
    options.draw.draw_ghost_case = True
    options.draw.x_label_name = 'X Ekseni (m)'
    options.draw.y_label_name = 'Y Ekseni (m)'
    options.draw.z_label_name = 'Z Ekseni (m)'

    if name in ['example6a', 'example7a']:
        options.draw.x_label_name = 'X Ekseni (mm)'
        options.draw.y_label_name = 'Y Ekseni (mm)'
        options.draw.z_label_name = 'Z Ekseni (mm)'

    femem.FEMEM(structure).run_all()


def run():
    toc = time.time()
    for name, structure in STRUCTURE_LIST.items():
        for attempt in range(1, NUM_ATTEMPTS+1):
            for method in METHODS:
                print(f'------------------ Started {name} with {method} - {attempt}/{NUM_ATTEMPTS} ------------------')
                run_one(structure, attempt, name, method)
                print(f'----------------- Finished {name} with {method} - {attempt}/{NUM_ATTEMPTS} ------------------')
                print()
    tic = time.time()
    print(f"------------------ Finished all runs in {(tic - toc):.4f} seconds ------------------")


if __name__ == '__main__':
    run()
