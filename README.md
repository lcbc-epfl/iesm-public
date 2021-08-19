[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

[Link to course website](https://lcbc-epfl.github.io/iesm-public/intro.html)

# Introduction to Electronic Structure Methods

An interactive introduction to electronic structure methods (HF, post-HF and DFT methods) given at EPFL by Prof. Ursula Roethlisberger. 

Over the years many people have contributed to this material: 

* Manuel Doemer 
* Elisabeth Brunk
* Martin Bircher 
* Ariadni Boziki 
* Esra Bozkurt 
* Nicholas Browning 
* Thibaud von Erlach 
* Franccois Mouvet
* Justin Villard
* Simon Duerr
* Andrea Levy


## How to use it (easy)

These notebooks are made to be run on [noto.epfl.ch](https://noto.epfl.ch), the EPFL JupyterHub. Select the Quantum Chemistry environment and click on the 🚀 icon on the course website to automatically get the latest notebook for this particular exercise. Changes will be automatically saved in your account and you can pick up where you left off. Note, that noto limits usage to 2 CPUs per User. 


## How to use it (hard)

This should only be done if you plan to adopt these notebooks for your own course or if you want to run the notebooks offline. 

### Creating an Conda Environment

You can install the required packages in any linux environment using miniconda.

1. `conda env create -f environment.yml`
2. `conda activate iesm`
3. `python -m ipykernel install --user --name iesm`

## Building a Jupyter Book

Run the following command in your terminal:

```bash
jb build iesm/
```

If you would like to work with a clean build, you can empty the build folder by running:

```bash
jb clean iesm/
```

If jupyter execution is cached, this command will not delete the cached folder. 

To remove the build folder (including `cached` executables), you can run:

```bash
jb clean --all iesm/
```

To preview the book navigate to `iesm/_build/html`

