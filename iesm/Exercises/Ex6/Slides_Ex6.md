---
title: Exercise Session 6
subtitle: IESM Fall 2022-2023
date: December 02, 2022
author: "Andrea Levy, Beatriz Mouriño, Simon Dürr, Sophia Johnson" 
output: beamer_presentation
---

# Exercise 6 - DFT vs (Post) HF Methods


![](/data/iesm/img_slides/Ex6/goals.png) 


# Exercise 6 - DFT vs (Post) HF Methods: Theory

* (Post) HF methods are wavefunction-based (we need to find the wavefunction)
* DFT shifts the focus: we need to find the ground-state charge density
* Why? For N electrons, wavefunction is a complex function of 3N variables, but the ground-state charge density is a function of 3 variables

* The universal functional of DFT is not known, but proven to exist
* Everything that is unknown is contained in $E_{XC}$
$$E(\rho) = T_{0}(\rho) + J(\rho) + \int v_{ext}\rho + E_{XC}$$
* Each functional will treat the XC part differently

# Exercise 6 - DFT (continued)

DFT is the workhorse of electronic structure methods: 

![](/data/iesm/img_slides/Ex6/papermountain.png){width=80%}

* In the [top 100](https://www.nature.com/news/the-top-100-papers-1.16224) most cited papers (ever!!) in the scientific community, 12 are on DFT 



# Comments on DFT

* Kohn-Sham formulation: ficticious molecular orbitals (non-interacting)
* If the exact XC functional is known - ground state energies, charge densities and HOMO (Koopman's theorem) are known
* Usually fast and widely available
* What can DFT do?
	* Atomic and cell geometries (fixed V,P)
	* Formation energy
	* Properties related to ground state

# Comments on DFT - downsides

* DFT also has some downsides - we will see this in practice
	* Difficulties with dispersion
	* Band gap problem - LUMO cannot be associated with KS orbitals (derivative discontinuity, deviation from piecewise linearity) [ref](https://pubs.acs.org/doi/full/10.1021/ct2009363)

![](/data/iesm/img_slides/Ex6/pwl.jpeg){width=100%}


# Comments on orbitals

* Orbitals are spatial wavefunctions/probability amplitudes
* We work with approximations, orbitals are mathematical formulations that approximate reality
* *"Dyson orbitals"* show how electronic distribution varies with ionization
	* Can be measured in some ionization experiments
* Koopman's theorem associates the Dyson orbital of an ionization process with the canonical HF orbital of the unionized state (for systems where we don't have static correlation)
* Dyson and canonical HF orbitals can even disagree qualitatively (*the same goes for KS orbitals*)

**TAKE-HOME MESSAGE: be careful with overinterpreting orbitals!**


# Exercise 6.1 - Methylcyclohexane A-value

![](/data/iesm/img_slides/Ex6/MeC6H11conformers.png){width=75%}

* You will perform calculations with HF and MP2 and different DFT functionals, add results to [collaborative spreadsheet](https://docs.google.com/spreadsheets/d/1Yv4AvdKp-8laRF9-oGNbqaUAOvYGqgJF-sCjOWPguEw/edit#gid=0) (linked also on Moodle)
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
	* Changes in a chemical transformation


# Exercise 6 - Tips
**Tips!**

* DFT will be further explored during lectures and the next exercises
* Here we used as reference papers that can be useful for further understanding [DFT1](https://www.nature.com/articles/s41563-021-01013-3), [DFT2](https://aip.scitation.org/doi/10.1063/1.4869598#_i15), [orbitals](https://onlinelibrary.wiley.com/doi/full/10.1002/anie.201904609)
* Calculations for Exercise 6.1 will be done in a collaborative way to speed up the exercise, add your results to [collaborative spreadsheet](https://docs.google.com/spreadsheets/d/1Yv4AvdKp-8laRF9-oGNbqaUAOvYGqgJF-sCjOWPguEw/edit#gid=0) (linked also on Moodle)
