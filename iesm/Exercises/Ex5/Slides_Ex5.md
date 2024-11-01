---
title: Exercise Session 5
subtitle: IESM Fall 2024-2025 
date: November 5, 2024
author: "Yuri, Qihao, Junwu, Salomé, Andrea, Sophia" 
output: beamer_presentation
---

# Exercise 5 - Post-Hartree Fock Methods: CI and MPn


![](/data/iesm/img_slides/Ex5/ex5_goals.png) 


# Exercise 5 - Post-Hartree Fock Methods: Theory

* HF method neglects correlation between electrons (consequence of using a single Slater determinant)
* We defined **correlation energy** the difference between the total and the HF energy (in the complete basis set limit)

$$E^{total} = E^{HF}_{CBS} + E^{corr} $$

* Inclusion of correlation can be based on e.g. **Post-Hartree-Fock methods**, such as: 
	* *Configuration Interaction* (**CI**) 
	* *Møller Plesset Perturbation Theory* of *n* order (**MPn**)
	* *Coupled cluster* (**CC**) 

* In this set of exercises, you will compare the performance of HF, CI and MPn (and CC) in describing bond dissociation energy and structural parameters 

# CI basics
* **idea**: instead of using a single Slater determinant (HF like), a linear combination of $M$ $N$-electron basis functions can be used
$$\begin{aligned}
\left|\Psi_j(\mathbf{r}_1, \mathbf{r}_2,\dots,\mathbf{r}_N)\right>=\sum_{i=1}^M c_{ij}\left|\Phi_j(\mathbf{r}_1, \mathbf{r}_2,\dots,\mathbf{r}_N)\right>
\end{aligned}
$$
* The expansion can be expressed in terms of "excitations" from the HF "reference" determinant
$$\left| \Psi_j \right> = c_0 \left|\Phi_0 \right> +\sum_{ra} c_{a}^{r}\left|\Phi_{a}^{r}\right>+\sum_{a<b,r<s} c_{ab}^{rs}\left|\Phi_{ab}^{rs}\right> + \dots$$
* CI method is nothing more than the matrix solution of the time-independent non-relativistic Schrödinger equation, using the (truncated) expression for $\left|\Psi_j\right>$ (CIS, CISD, CISDT, \dots, FullCI).

# CI basics 
* **in practice**: 
	* Number of determinats grows extremely fast
	* Full CI performed for very small molecules for benchmarks studies
	* CIS sometimes used for approximate excited state calculations
	* In general, CI method not often used because it is too expensive and other methods give results of comparable quality at lower cost

# MPn basics
* MPn is a **perturbation method**, i.e. the problem under investigation is assumed to only differ slightly from a problem which has already been solved, exactly or approximately
* In QM, the perturbation of a system with Hamiltonian $\hat{\mathrm{H}}_0$
is described by the perturbed Hamiltonian 
$$\hat{\mathrm{H}} = \hat{\mathrm{H}}_0 + \lambda \hat{\mathrm{V}}$$
For a sufficiently weak perturbation, the eigenstates and eigenvalues may then
be expanded in a power series
* In MPn theory, $\hat{\mathrm{V}}$ is the difference between the true
ground state Hamiltonian and the Hartree-Fock Hamiltonian; hence, the perturbation may be written in terms of excited Slater determinants

# MPn basics
Energy correction terms can be computed, due to different excitations
$$E_0^{total} = E_0^{HF} + \sum_{n=1} E_0^{(n)}$$

* **in practice**:
	* The corrections are truncated to a certain $n$, setting the order of the MP calculation (hence the MPn notation)
	* The computational cost will increase with MPn order, usually calculations are not performed with order higher than MP4
	* MPn approach is often less expensive than CI (for sure FCI) and accurate enough
	* MPn is **not variational**, i.e. the resulting MPn energy may be lower than the true ground-state energy. The series is not necessarily converging.

# Exercise 5 - Boron atom

![](/data/iesm/img_slides/Ex5/boron.png){width=95%} 

* You'll need to perform many different calculations (not taking that long for a single atom)
* Keywords for each method can be found in [Psi4 manual](https://psicode.org/psi4manual/master/energy.html)
* Options should be already set correctly with \texttt{psi4.set\_options}

# Exercise 5 - C-F bond cleavage
* influence of correlation on the BDE in a radical process by comparing HF to MPn results
$$
\begin{aligned}
CH_3F \quad \rightarrow \quad H_3C\cdot \quad + \quad F\cdot\end{aligned}
$$
$$
\begin{aligned}
E^{BDE} =  E^{H_3C\cdot} + E^{F\cdot} - E^{CH_3F}\end{aligned}
$$
![](/data/iesm/img_slides/Ex5/CF.png){width=80%} 

*Note: these calculations may take some time!* 


# Exercise 5 - HNO3 geometry
* influence of correlation on electron correlation on structural parameters, such as bond lengths and angles
![](/data/iesm/img_slides/Ex5/HNO3.png){width=100%}
 
*Note: also these calculations may take some time!* 


# Exercise 5 - Tips
**Tips!**

* MPn theory will be treated in detail during lectures 
* Same for CC method used for B atom - take it as just *another* post-HF  method for now
* This is probably the first exercise where calculations are completed in minutes and not second - it is always a good idea to monitor their status, this can be done using the terminal \texttt{tail -f} command

![](/data/iesm/img_slides/Ex5/tailcommand.png){width=90%}


