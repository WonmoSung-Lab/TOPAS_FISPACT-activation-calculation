import pandas as pd
import numpy as np
import os


def convert_to_spectrum_txt(input_dir: str, output_dir: str):
    """
    Convert particle fluence data (e.g., protons or other particles) from CSV files to a formatted spectrum text file.

    Args:
        input_dir (str): Directory containing input CSV files.
        output_dir (str): Directory to save the converted TXT spectrum files.
    """

    # Get a list of files in the input directory
    files = os.listdir(input_dir)
    print("Files found:", files)

    # Remove macOS-specific hidden file if present
    if ".DS_Store" in files:
        files.remove(".DS_Store")

    # Set NumPy output format for scientific notation
    np.set_printoptions(formatter={"float": "{:e}".format})

    for file_name in files:
        # Read the CSV file with tab separator
        df = pd.read_csv(os.path.join(input_dir, file_name), sep="\t", engine="python")

        # Energy bin configuration (proton example)
        Ebinmin = 1e4  # Minimum energy (10 keV)
        Ebinmax = 1e9  # Maximum energy (1 GeV)
        Ebin = 161  # Number of bins
        step = (Ebinmax - Ebinmin) / Ebin
        unit = 1e2  # Convert mm² to cm²

        # Extract particle fluence values from 8th row (index 7)
        raw_values = df.loc[7].str.split(",")
        flat_values = sum(raw_values, [])
        particle_fluence = list(
            map(float, flat_values[1:-2])
        )  # Remove headers and trailing commas

        # Convert fluence to flux (fluence per cm²)
        particle_flux = np.round(np.array(particle_fluence) * unit, 5)
        total_flux = np.sum(particle_flux)

        # Prepare for writing: reverse order as required by TOPAS
        flux_list = list(map(str, particle_flux[::-1]))

        # Generate descending energy bin list
        energy_bins = np.arange(Ebinmin, Ebinmax + step, step)[::-1]
        energy_list = list(map(str, energy_bins))

        # Output file name
        output_filename = f"{os.path.splitext(file_name)[0]}_spectrum.txt"
        output_path = os.path.join(output_dir, output_filename)

        # Write energy values
        with open(output_path, "w") as f:
            for energy in energy_list:
                f.write(energy + "\n")

        # Append flux values and total flux info
        with open(output_path, "a") as f:
            f.write("\n")
            for flux in flux_list:
                f.write(flux + "\n")
            f.write("1.0\n")
            f.write("Topas spectrum total flux = %.5e\n" % total_flux)
