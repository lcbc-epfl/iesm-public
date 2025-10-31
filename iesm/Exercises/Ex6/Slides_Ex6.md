---
title: Exercise Session 6
subtitle: IESM Fall 2025-2026 
date: November 11, 2025
author: "Qihao, Salomé, Evan, Thibault" 
output: beamer_presentation
---

# Exercise 6 - DFT vs (Post) HF Methods


![](/data/iesm/img_slides/Ex6/goals.png) 


# Exercise 6 - DFT vs (Post) HF Methods: Theory

* (Post) HF methods are wavefunction-based (we need to find the system (many-electrons) wavefunction)
* DFT shifts the focus: we need to find the electron density
* Why? For N electrons, the system wavefunction is a complex function of 3N variables, but the electron density is a function of 3 variables

* The universal functional not known, but proven to exist
* Everything that is unknown is contained in $E_{XC}$
$$E[\rho] = T_{0}[\rho] + J[\rho] + \int v_{ext}(r)\rho(r)dr + E_{XC}[\rho]$$
* Each computational functional will treat the XC part differently

# Exercise 6 - DFT (continued)

DFT is the workhorse of electronic structure methods: 

![](/data/iesm/img_slides/Ex6/papermountain.png){width=80%}

* In the [top 100](https://www.nature.com/news/the-top-100-papers-1.16224) most cited papers (ever!!) in the scientific community, 12 are on DFT 



# Comments on DFT

* Kohn-Sham formulation: ficticious molecular orbitals (non-interacting)
* If the exact XC functional is known - ground-state energies, electron/charge density and HOMO (Koopman's theorem) are known
* Usually fast and widely available
* What can DFT do?
	* Atomic and cell geometries (fixed V,P)
	* Formation energy
	* Properties related to the ground state

# Comments on DFT - downsides

* DFT also has some downsides - we will see this in practice
	* Difficulties capturing systems with dispersion
	* Band gap problem - LUMO cannot be associated with KS orbitals (derivative discontinuity, deviation from piecewise linearity)
 	* No magic solutions :( we must make approximations and test our decisions


# Comments on orbitals

* Orbitals are spatial wavefunctions, essentially probability amplitudes
* In practice, our calculated orbitals are mathematical formulations which approximate our true system
* Different calculations of orbtials (KS orbitals, canoncial HF orbitals, Dyson orbitals) can disagree qualitatively 
* Be careful with overinterpreting orbitals


# Exercise 6.1 - Methylcyclohexane A-value

![](/data/iesm/img_slides/Ex6/MeC6H11conformers.png){width=75%}

* You will perform calculations with HF and MP2 and different DFT functionals, add results to [collaborative spreadsheet](https://docs.google.com/spreadsheets/d/1hRvOyKqIaylOZ2Wi_LpAPN8oX3J3SucC7WuGmkPImn0/edit?usp=sharing) (link also on Moodle)
* Points of comparison: 
	* $\psi$ or $\rho$ based? 
	* how accurate (w.r.t. experimental reference)?
	* computational time

* DFT is a world on its own - depending on the functional chosen you can go from cheap, very off calculations to expensive and more reliable ones


# Exercise 6.2 - Geometric properties: $NO_{3}$ radical

![](/data/iesm/img_slides/Ex6/no3.png){width=30%}

* Calculate N-O bond lengths and O-N-O bond angles
	* Experiments: $D_{3}^{h}$, N-O 1.24 $\AA$ and O-N-O 120&deg;

* Compare results (HF, MP2 vs DFT)

* You will visualize the KS orbitals - what can they tell us?
	* Changes in the electronic structure between different species 
	* General size, shape of expected one-electron orbitals (hopefully)


# Exercise 6 - Tips
* Calculations for Exercise 6.1 will be done in a collaborative way to speed up the exercise, add your results to [collaborative spreadsheet](https://docs.google.com/spreadsheets/d/1hRvOyKqIaylOZ2Wi_LpAPN8oX3J3SucC7WuGmkPImn0/edit?usp=sharing) (linked also on Moodle)
* You can monitor your calculations by opening a terminal window in noto and typing "tail -f name_output_log"
* DFT will be further explored during lectures and the next exercises
* Here we used as reference papers that can be useful for further understanding [DFT1](https://www.nature.com/articles/s41563-021-01013-3), [DFT2](https://aip.scitation.org/doi/10.1063/1.4869598#_i15), [orbitals](https://onlinelibrary.wiley.com/doi/full/10.1002/anie.201904609)
