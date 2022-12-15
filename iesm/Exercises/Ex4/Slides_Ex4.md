---
title: Exercise Session 4
subtitle: IESM Fall 2022-2023 
date: November 11, 2022  
author: "Andrea Levy, Beatriz Bueno Mouriño, Simon Dürr, Sophia Johnson" 
output: beamer_presentation
---

# Course Reminders
* Welcome Simon!
* From this week we'll start to have **Lectures/Ex also on Fridays** with deadlines for exercise reports on morning of next exercise session 
* Friday lectures in BCH 4310
* Monday 14.11: mock written exam during the lecture time
* Friday 18.11: mock exam solutions and Q&A session (we'll gather questions on the moodle forum by Wednesday 16.11)
* **Monday 21.11:** written exam
* Friday 25.11: report for exercise 4 due by 9am; session for exercise 5

# Exercise 4 
The Hartree-Fock procedure in detail
(Reminder: you can download these slides from the [Exercise page](https://lcbc-epfl.github.io/iesm-public/Exercises/Ex4/IESM_Ex4b.html))

![](/data/iesm/img_slides/Ex4/ex4_goals.png) 

# Recap of HF Theory
**HF method = approximate many-body wavefunction to a single Slater determinant**
$$\boxed{ \Psi(\mathbf{r}_1, \mathbf{r}_2,\dots,\mathbf{r}_n)\approx\Psi_{HF}\equiv\frac{1}{\sqrt{N}}\left|\phi_1(\mathbf{r}_1) \phi_2(\mathbf{r}_2)\dots\phi_n(\mathbf{r}_n)\right| }$$

$\rightarrow \Psi_{HF}$ inserted into time-independent Schrödinger equation to find eigenvalue, i.e. $E = \left<\Psi_{HF}\middle|\hat{H}_{el}\middle|\Psi_{HF}\right>$. What is found is a **variational solution**, i.e. HF energy is always above true energy.

# Recap of SCF Method

HF equations (will be derived in detail during Lectures)
$$E_{HF} = \sum_i \left<\phi_i\middle|\hat{h}\middle|\phi_i\right> + \frac{1}{2}\sum_{i, j}\left(\left[\phi_i \phi_i\middle|\phi_j \phi_j\right] - \left[\phi_i \phi_j\middle|\phi_j \phi_i\right]\right) \quad\quad \forall\phi_i$$

where $\left[\dots\middle|\dots\right]$ integrals contain Coulomb and Exchange operators, whose action on orbital $\phi_i$ depends on all the other one-electron orbitals $\phi_j$. Hence, HF equations have to be solved iteratively until self-consistency (**self consistent field SCF method**)

![](/data/iesm/img_slides/Ex3/SCF_cycle.png)

# Hartree-Fock Roothaan Equations

* HF equations area set of coupled integro-differential equations to determine the HF molecular one-electron orbitals
* If we represent the orbitals in a basis (of AO-like orbitals), the HF equations transform into matrix equations that were first derived by **Roothaan**

$$\Rightarrow\mathbb{F}\mathbb{C}=\mathbb{S}\mathbb{C}\mathbb{E}$$

* Note: as you will see today, this problem can be recasted in an eigenvalue problem via a basis set transformation

$$\Rightarrow\mathbb{F}'\mathbb{C}'=\mathbb{C}'\mathbb{E}'$$

# Building the Fock Matrix
The HF method recasts into a pseudo-eigenvalue problem 
$$\mathbb{F}\mathbb{C}=\mathbb{S}\mathbb{C}\mathbb{E}$$
where: 

* $\mathbb{F} = \mathbb{H} + 2\mathbb{J} - \mathbb{K}$ is the **Fock matrix**
* $\mathbb{C}$ is the **wavefunction amplitude matrix**
* $\mathbb{S}$ is the **overlap matrix**
* and $\mathbb{E}$ is the **energy value matrix** 

The issue? $\mathbb{F}$ relies on an orbital solution in order to iteratively solve (with **SCF method**) for the "best" molecular orbitals which make a single Slater determinant description of the system wavefunction. We will begin with a guess and iteratively improve on the guess. 

# Performing HF Explicitly

![](/data/iesm/img_slides/Ex4/hf_cycle.png){height=90%}

# Overlap Matrix $\mathbb{S}$
$\mathbb{S}$, the overlap matrix, describes the inter-relationships of the basis set vectors. Other details about $\mathbb{S}$:

* The number of basis functions, $n$, defines the size and shape of $\mathbb{S}$($n$x$n$)
* $\mathbb{S}$ is an idenity matrix in the case of orthonormal basis set functions 
* By properly transforming the $\mathbb{S}$ matrix, we can ensure orthonormality 

# Implicit Einstein Summation
The einsum function in numpy allows for efficient matrix multiplication.

![](/data/iesm/img_slides/Ex4/summation.png){width=55%}
![](/data/iesm/img_slides/Ex4/einsum_examples.png)

# Exercise 4 - Tips
**Tips!**

* If needed, search for commands and variable types in the [Psi4 manual](https://psicode.org/psi4manual/master/index.html) 
* Some code blocks just need to be executed. Typically, we use a comment (#) in a code block to indicate where edits should be made. 
* Today's exercise includes details for the manipulation of matrices used in the HF procedure. As you work, try to consider why these transformations are necessary in order to run a HF method calculation. 
