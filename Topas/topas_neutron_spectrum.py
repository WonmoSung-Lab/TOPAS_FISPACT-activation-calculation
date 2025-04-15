import pandas as pd
import numpy as np
import os


def convert_to_spectrum_txt(input_dir: str, output_dir: str):
    """
    Convert neutron fluence data from CSV files to a formatted spectrum text file.

    Args:
        input_dir (str): Directory containing input CSV files.
        output_dir (str): Directory where output .txt files will be saved.
    """
    # List all files in the input directory
    files = os.listdir(input_dir)

    # Remove macOS-specific hidden file if present
    if ".DS_Store" in files:
        files.remove(".DS_Store")

    # Set NumPy print options for scientific notation
    np.set_printoptions(formatter={"float": "{:e}".format})

    for file_name in files:
        # Load CSV file with tab separator
        df = pd.read_csv(os.path.join(input_dir, file_name), sep="\t", engine="python")

        # Energy bin settings (units: eV)
        Ebinmin = 1e-5  # Minimum energy (eV)
        Ebinmax = 1e9  # Maximum energy (eV)
        Ebin = 708  # Number of bins
        step = (Ebinmax - Ebinmin) / Ebin  # Bin width
        unit = 1e2  # Area conversion factor (mm² to cm²)

        # Extract neutron fluence values from the 8th row (index 7)
        raw_values = df.loc[7].str.split(",")
        flat_values = sum(raw_values, [])
        Neutron_fluence = list(
            map(float, flat_values[1:-2])
        )  # Remove headers and trailing elements

        # Convert fluence to flux by scaling with unit area
        Neutron_flux = np.round(np.array(Neutron_fluence) * unit, 5)
        Neutron_flux_sum = np.sum(Neutron_flux)

        # Reverse list for output format
        flux_list = list(map(str, Neutron_flux[::-1]))

        # Calculate energy bin edges and reverse for descending order
        Neutron_Energy = np.arange(Ebinmin, Ebinmax + step, step)[::-1]
        energy_list = list(map(str, Neutron_Energy))

        # Prepare output file name
        output_filename = f"{os.path.splitext(file_name)[0]}_spectrum.txt"
        output_path = os.path.join(output_dir, output_filename)

        # Write energy values to file
        with open(output_path, "w") as f:
            for energy in energy_list:
                f.write(energy + "\n")

        # Append flux values and additional metadata
        with open(output_path, "a") as f:
            f.write("\n")
            for flux in flux_list:
                f.write(flux + "\n")
            f.write("1.0\n")
            f.write(f"Topas spectrum total flux={Neutron_flux_sum}")
