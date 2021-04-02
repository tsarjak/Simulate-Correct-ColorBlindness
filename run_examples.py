from recolor import Core


def main():
    # Simulating Protanopia with diagnosed degree of 0.9 and saving the image to file.
    Core.simulate(input_path='Examples_Check/ex_original.jpg',
                  return_type='save',
                  save_path='Examples_Check/ex_simulate_protanopia.png',
                  simulate_type='protanopia',
                  simulate_degree_primary=0.9)

    # Simulating Deutranopia with diagnosed degree of 0.9 and saving the image to file.
    Core.simulate(input_path='Examples_Check/ex_original.jpg',
                  return_type='save',
                  save_path='Examples_Check/ex_simulate_deutranopia.png',
                  simulate_type='deutranopia',
                  simulate_degree_primary=0.9)

    # Simulating Tritanopia with diagnosed degree of 0.9 and saving the image to file.
    Core.simulate(input_path='Examples_Check/ex_original.jpg',
                  return_type='save',
                  save_path='Examples_Check/ex_simulate_tritanopia.png',
                  simulate_type='tritanopia',
                  simulate_degree_primary=0.9)

    # Simulating Hybrid (Protanomaly + Deutranomaly) with diagnosed degree of 0.9 and 1.0 and saving the image to file.
    Core.simulate(input_path='Examples_Check/ex_original.jpg',
                  return_type='save',
                  save_path='Examples_Check/ex_simulate_hybrid.png',
                  simulate_type='hybrid',
                  simulate_degree_primary=0.5,
                  simulate_degree_sec=0.5)

    # Correcting Image for Protanopia with diagnosed degree of 1.0 and saving the image to file.
    Core.correct(input_path='Examples_Check/ex_original.jpg',
                 return_type='save',
                 save_path='Examples_Check/ex_corrected_protanopia.png',
                 protanopia_degree=0.9,
                 deutranopia_degree=0.0)

    # Also simulate the corrected image to see difference.
    Core.simulate(input_path='Examples_Check/ex_corrected_protanopia.png',
                  return_type='save',
                  save_path='Examples_Check/ex_simulate_corrected_protanopia.png',
                  simulate_type='protanopia',
                  simulate_degree_primary=0.9)

    # Correcting Image for Deutranopia with diagnosed degree of 1.0 and saving the image to file.
    Core.correct(input_path='Examples_Check/ex_original.jpg',
                 return_type='save',
                 save_path='Examples_Check/ex_corrected_deutranopia.png',
                 protanopia_degree=0.0,
                 deutranopia_degree=1.0)

    # Also simulate the corrected image to see difference.
    Core.simulate(input_path='Examples_Check/ex_corrected_deutranopia.png',
                  return_type='save',
                  save_path='Examples_Check/ex_simulate_corrected_deutranopia.png',
                  simulate_type='deutranopia',
                  simulate_degree_primary=0.9)

    # Correcting Image for Hybrid with diagnosed degree of 1.0 for both protanopia and
    # deutranopia and saving the image to file.
    Core.correct(input_path='Examples_Check/ex_original.jpg',
                 return_type='save',
                 save_path='Examples_Check/ex_corrected_hybrid.png',
                 protanopia_degree=0.5,
                 deutranopia_degree=0.5)

    # You can also use different return types and get numpy array or PIL.Image for further processing.
    # See recolor.py
    return


if __name__ == '__main__':
    main()
