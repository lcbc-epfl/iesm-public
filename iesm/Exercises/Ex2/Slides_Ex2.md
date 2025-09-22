---
title: Exercise Session 2
subtitle: IESM Fall 2025-2026
date: September 23, 2025
author: "Qihao, Salomé, Evan, Thibault" 
output: beamer_presentation
---

# Notebook Reminders
- If you're on our [exercise website](https://lcbc-epfl.github.io/iesm-public/intro.html) click the rocket button on the top right, choose JupyterHub ([noto.epfl.ch](https://noto.epfl.ch/))
		![](/data/iesm/img_slides/Ex1/notebooks.png) \
- Make sure to always activate (top right) the `Computational Chemistry` kernel
		![](/data/iesm/img_slides/Ex1/kernel.png) \

# Notebook Reminders
- `.iynb` files organized in cells
	- Markdown (text)
	- Code 
- You can edit the cells directly 
- Run a code cell by pressing `Play` button (or `Ctrl`+`Enter` or `Shift`+`Enter`)

	![](/data/iesm/img_slides/Ex1/jn_1.png) \

# Psi4 Introduction
- [Psi4 Manual](https://psicode.org/psi4manual/master/index.html)
- Open-Source *ab initio* electronic structure software package
- Allows for calculations such as: HF, CI, DFT, molecular energies/structures, reaction mechanisms, transition state search, vibrational frequencies, molecular orbitals/densities, geometry optimization, atomic charges, electrostatic potentials, NMR properties, and more 
- Other electronic structure software you may know: Gaussian, CP2K, CPMD, Quantum Espresso, ORCA, NWChem 

	![](/data/iesm/img_slides/Ex2/psi4.png){width=80%}  \
  
# Psi4 with Python
- We can use Psi4 as a python module with PsiAPI directly in Jupyter Notebooks 
- We import Psi4 and use the `psi4` directive to ask Psi4 to perform an action 

	![](/data/iesm/img_slides/Ex2/psi4_api.png){width=70%} \ 

# Viewing Output
- We often set an output file (usually a `.log` file) to store information from a calculation
- You can find them in the lefthand navigation directory 

	![](/data/iesm/img_slides/Ex2/output_example.png){width=95%}  \
	
# Linux & Terminal
- Linux bash commands in notebooks (cell starts with  **`!`**)

	![](/data/iesm/img_slides/Ex2/linux_commands.png){width=80%} \
- Linux commands (even Psi4 calculations) directly via a terminal view of your notebooks
	![](/data/iesm/img_slides/Ex2/terminal.png){width=80%} \ 

- Refresh your bash commands as needed online like [here](https://dev.to/awwsmm/101-bash-commands-and-tips-for-beginners-to-experts-30je)


# Jupyter Servers
- *"Noto can run up to 20 parallel Jupyter backend servers to provide a total of up to 320 GB of RAM and 320 CPU, shared between all users. Our current policy is to allocate up to a maximum of 2 GB of RAM and 2 CPUs per user." *

![](/data/iesm/img_slides/Ex2/HPC_architecture.png){width=90%} 
*(Images from [TACC HPC textbook](https://zenodo.org/record/49897)*)


# Exercise 2 - Basis Sets & Psi4
**First steps in Psi4** - [Exercise page](https://lcbc-epfl.github.io/iesm-public/Exercises/Ex2/IESM_Ex2.html)

* Understand what are basis functions
* Get familiar with basis function notation
* Basics of Psi4
* Get familiar with molecular geometries
![](/data/iesm/img_slides/Ex2/ex2_goals.png) \

# Exercise 2 - New exercise questions
**New exercise questions!**

* The two parts of the exercise on the helium atom (section 2.2.4) and on beryllium hydride (section 2.4) are new.
* Therefore, please let us now if something is unclear in the text, questions or the tasks we ask you to perform : )
* These modifications include questions 9, 13, and 14.
* **Total of 14 questions**
* **Due date for the written report next Tuesday (September 30, 10am)**

# Exercise 2 - Tips
**Tips!**

* Please focus on understanding basis sets well first and then getting familiar with Psi4 : ) 
* Practice single-point calculations for an single atom and simple molecule with `psi4.energy()` commands
	* Requires input geometry (Z-matrix or Cartesian coordinates)
	* Psi4 finds lowest energy combination of wavefunction coefficients for the given geometry
	* By comparing energy values with different basis sets we can discuss the effect of basis set selections on accuracy and cost (Additional note: is the total energy always meaningful? -- think about that expecially in the H$_2$O exercise)
	* We will compute the energy of the system with the selected basis set **and** a method of choice, here only UHF (unrestricted Hartree Fock). But don't worry too much about it for now: you will get familiar with this and other methods in the next lectures/exercises!
