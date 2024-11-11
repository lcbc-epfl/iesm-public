---
title: Exercise Session 6
subtitle: IESM Fall 2024-2025 
date: November 12, 2024
author: "Yuri, Qihao, Junwu, Salomé, Andrea, Sophia" 
output: beamer_presentation
---

<!-- # Last Week's Annoucement

* As mentioned last week, during your work on exercises for this course you have the opportunity to help Zhenyu Cai, a PhD student in the CHILI lab who is developing new teaching tools. It's your decision to participate and there is no influence on your grades in any way. We will remain unaware of your consent status. If you previously said "no" but wish to change your response, let him know so he can re-launch your permissions. Thanks for considering!
* More details about the project: https://drive.google.com/file/d/1GNR9NSpvh3s0nmvWXwMBONjNC3mAAW53/view?usp=sharing
* Consent form (if you agree to participate): https://forms.gle/hc6K8f5yRUA5T9Lz9  -->

# Exercise 6 - DFT vs (Post) HF Methods


![](/data/iesm/img_slides/Ex6/goals.png) 


# Exercise 6 - DFT vs (Post) HF Methods: Theory

* (Post) HF methods are wavefunction-based (we need to find the wavefunction)
* DFT shifts the focus: we need to find the ground-state charge density
* Why? For N electrons, wavefunction is a complex function of 3N variables, but the ground-state charge density is a function of 3 variables

* The universal functional not known, but proven to exist
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
	* Difficulties with capturing systems dispersion
	* Band gap problem - LUMO cannot be associated with KS orbitals (derivative discontinuity, deviation from piecewise linearity)
 	* No magic solutions :( we must make approximations and test our decisions


# Comments on orbitals

* Orbitals are spatial wave functions, essentially probability amplitudes
* In practice, our calculated orbitals are mathematical formulations which approximate our true system
* Different calculations of orbtials (KS orbitals, canoncial HF orbitals, Dyson orbitals) can disagree qualitatively 
* Be careful with overinterpreting orbitals


# Exercise 6.1 - Methylcyclohexane A-value

![](/data/iesm/img_slides/Ex6/MeC6H11conformers.png){width=75%}

* You will perform calculations with HF and MP2 and different DFT functionals, add results to [collaborative spreadsheet](https://docs.google.com/spreadsheets/d/16xyftdQZjgV0bFaluMygytFDtQgICnYbcYRPQMqzPB8/edit?usp=sharing) (linked also on Moodle)
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
* Calculations for Exercise 6.1 will be done in a collaborative way to speed up the exercise, add your results to [collaborative spreadsheet](https://docs.google.com/spreadsheets/d/16xyftdQZjgV0bFaluMygytFDtQgICnYbcYRPQMqzPB8/edit?usp=sharing) (linked also on Moodle)
* You can monitor your calculations by opening a terminal window in noto and typing "tail -f name_output_log"
* DFT will be further explored during lectures and the next exercises
* Here we used as reference papers that can be useful for further understanding [DFT1](https://www.nature.com/articles/s41563-021-01013-3), [DFT2](https://aip.scitation.org/doi/10.1063/1.4869598#_i15), [orbitals](https://onlinelibrary.wiley.com/doi/full/10.1002/anie.201904609)
