# Description
This python script retrieves the trajectory of the WIND and Integral spacecrafts and plots them using Matplotlib.
The WIND data located in the folder wind_trajectory was downloaded from ftp://spdf.gsfc.nasa.gov/pub/data/wind/orbit/pre_or/

# Install Conda environment
`conda env create -f environment.yml`

# Run program in Conda environment
- Enter the conda environment:
  - In Linux: `source activate wind-integral`
  - In Windows: `activate wind-integral`
- `python main.py`