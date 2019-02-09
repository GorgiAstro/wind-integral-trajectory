# Description
This python script retrieves the trajectory of the WIND and Integral spacecrafts and plots them using Matplotlib.
The WIND data located in the folder wind_trajectory was downloaded from ftp://spdf.gsfc.nasa.gov/pub/data/wind/orbit/pre_or/

# Install Conda environment
`conda env create -f environment.yml`

# Install Jupyter Lab extensions
## Recommended extensions
I recommend the following two extensions:
* Table of contents: `jupyter labextension install @jupyterlab/toc`
* Variable inspect: `jupyter labextension install @lckr/jupyterlab_variableinspector`

# Run program in Conda environment
- Enter the conda environment:
  - In Linux: `source activate wind-integral`
  - In Windows: `activate wind-integral`
- Start Jupyter lab by typing `jupyter lab`