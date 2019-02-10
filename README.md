# Description
This python script retrieves the trajectory of the WIND and Integral spacecrafts and plots them using Matplotlib.
The WIND data located in the folder wind_trajectory was downloaded from ftp://spdf.gsfc.nasa.gov/pub/data/wind/orbit/pre_or/

# Install Conda environment
If running for the first time:
`conda env create -f environment.yml`

If the environment already exists, update it using:
`conda env update -f environment.yml`

# Install Jupyter Lab extensions
## Mandatory extensions
The following extensions are required to use Plotly offline in notebooks:
```
# Enter conda environment
source activate wind-integral

# Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build

# FigureWidget support
jupyter labextension install plotlywidget --no-build

# offline iplot support
jupyter labextension install @jupyterlab/plotly-extension --no-build

# JupyterLab chart editor support (optional)
jupyter labextension install jupyterlab-chart-editor --no-build

# Build extensions (must be done to activate extensions since --no-build is used above)
jupyter lab build
```

## Recommended extensions
I recommend the following two extensions:
* Table of contents: `jupyter labextension install @jupyterlab/toc`
* Variable inspect: `jupyter labextension install @lckr/jupyterlab_variableinspector`

# Run program in Conda environment
- Enter the conda environment:
  - In Linux: `source activate wind-integral`
  - In Windows: `activate wind-integral`
- Start Jupyter lab by typing `jupyter lab`