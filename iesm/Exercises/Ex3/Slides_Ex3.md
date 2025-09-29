---
title: Exercise Session 3
subtitle: IESM Fall 2025-2026 
date: September 30, 2025  
author: "Salomé, Qihao, Thibault, Evan" 
output: beamer_presentation
---

# Reports Feedback
Interviews:

* You should have received a detailed feedback on Moodle for reports of Ex1
* If everything is correct, simple checkmarks are added
* Comments added when something is wrong/unclear/uncomplete
* Overall comment added to the report

# Exercise 3 
Large Basis Sets, Dissociation Energy and Geometry Optimisation
(Reminder: you can download these slides from the [Exercise page](https://github.com/lcbc-epfl/iesm-public/blob/gh-pages/Exercises/Ex3/Slides_Ex3.md.pdf))

![](/data/iesm/img_slides/Ex3/ex3_goals.png) \

# Influence of basis set 
* System under study: H$_2$ molecule at equilibrium bondlength (H--H distance 0.7414Å)

	![](/data/iesm/img_slides/Ex3/H2mol.png){width=64px} \ 

* You will compute the equilibrium energy of the molecule using different basis sets
	* 6-31G 
	* 6-311G 
	* aug-cc-pVTZ (Dunning’s correlation-consistent basis, defined such that systematic improvement over total energies and molecular properties is possible)


# Introduction to HF Theory
* We will use HF theory (which will be treated in detail during Lectures and next Exercise session) to calculate energies 
* In this exercise, you will qualitatively see the differences between RHF and UHF

**HF method = approximate many-body wavefunction to a single Slater determinant**
$$\boxed{ \Psi(\mathbf{r}_1, \mathbf{r}_2,\dots,\mathbf{r}_n)\approx\Psi_{HF}\equiv\frac{1}{\sqrt{N}}\left|\phi_1(\mathbf{r}_1) \phi_2(\mathbf{r}_2)\dots\phi_n(\mathbf{r}_n)\right| }$$

$\rightarrow \Psi_{HF}$ inserted into time-independent Schrödinger equation to find eigenvalue, i.e. $E = \left<\Psi_{HF}\middle|\hat{H}_{el}\middle|\Psi_{HF}\right>$. What is found is a **variational solution**, i.e. HF energy is always above true energy.

# SCF method

HF equations (will be derived in detail during Lectures)
$$E_{HF} = \sum_i \left<\phi_i\middle|\hat{h}\middle|\phi_i\right> + \frac{1}{2}\sum_{i, j}\left(\left[\phi_i \phi_i\middle|\phi_j \phi_j\right] - \left[\phi_i \phi_j\middle|\phi_j \phi_i\right]\right) \quad\quad \forall\phi_i$$

where $\left[\dots\middle|\dots\right]$ integrals contain Coulomb and Exchange operators, whose action on orbital $\phi_i$ depends on all the other one-electron orbitals $\phi_j$. Hence, HF equations have to be solved iteratively until self-consistency (**selfconsistent field SCF method**)

![](/data/iesm/img_slides/Ex3/SCF_cycle.png) \

# RHF and UHF methods

* So far we did not discuss spin components! MO are composed of a MO spatial wavefunction ($\phi_i(\mathbf{r}_i)$) and a MO spin wavefunction ($\alpha$ or $\beta$, i.e. $\uparrow$ or $\downarrow$ spin)
* In practice, different HF implementations are possible:
	* **RHF** (Restricted HF): each spatial MO $\phi_i(\mathbf{r}_i)$ is used twice, once multiplied by a $\alpha$ spin and the other by the $\beta$ spin $\Rightarrow$ same spatial component! This is reasonable for **closed-shell systems** (even number of electrons), where spatial MO is fully occupied.
	*  **UHF** (Unrestricted HF): different spatial MO used for $\alpha$ and $\beta$ spins. This allow to describe **open-shell sytems** (odd number of electrons), **but** a single Slater determinant of different orbitals for different spins is not an eigenfunction of the total spin operator $\mathbf{\hat{S}}^2$ (this produced the so-called *spin contamination*, where the ground state is *contaminated* by excited states).

# RHF vs UHF

![[[Image source](http://www.chemgapedia.de/vsengine/vlu/vsc/de/ch/15/thc/quantenspek/eprspek/tc060_eprpek.vlu/Page/vsc/de/ch/15/thc/quantenspek/eprspek/mspek_53.vscml.html)] Note that here $\Psi$ is a MO!](/data/iesm/img_slides/Ex3/RHF_UHF.png){width=80%} 

* RHF suitable for closed-shell systems, UHF for open-shell 
* UHF doubles the spatial orbitals, hence it is more computationally expensive

In this exercise you will record the dissociation curve for H$_2$ molecule - what is the effect of using RHF vs UHF?

# Geometry optimization

* Until now **single-point calculations** (nuclear positions fixed)
	`psi4.energy(method/basisset, molecule)`
* **Geometry optimization**: starting from an initial configuration, you can follow the curvature on the PES down to the minimum, i.e find the equilibrium geometry
	`psi4.optimize(method/basisset, molecule)`
![](/data/iesm/img_slides/Ex3/energy_optimization.png){width=50%} [[Image source](https://www.sciencedirect.com/science/article/pii/B9780323902649000234)]

# Exercise 3 - Tips
**Tips!**

* You'll need to edit some code cells and having a look at code in Ex2 may be helpful 
* You'll use `matplotlib` to make plots, more information on it can be found [here](https://matplotlib.org/stable/users/index)
* HF method will be treated in detail in next Lectures and Exercises, for today make sure to have understood the general idea. [Psi4 manual](https://psicode.org/psi4manual/master/scf.html) has also a quick theory introduction on HF and is useful to get familiar with different HF methods/keywords.
* Make sure to understand the difference between a single-point calculation and a geometry optimization (you will see it in practice in Ex3.3)!
