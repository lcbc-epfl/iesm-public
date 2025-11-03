# Post-Hartree Fock Methods: Theory Recap
This section give a brief summary of the theory behind two *Post-Hartree-Fock methods*: *Configuration
Interaction* (CI) and *Møller Plesset Perturbation Theory* (MPn, where $n$ indicates the order of MP theory).

## Configuration Interaction Theory
Of all the *ab initio* methods, CI is probably the easiest to understand, and perhaps one of the
hardest to implement efficiently on a computer! The basic idea of CI is to improve the HF solution by increasing the space 
of all possible many-electron wavefunctions from a single Slater determinant (as in HF theory), to a set of many, in principle infinite, Slater determinants.

An arbitrary $N$-electron wavefunction $\left|\Psi_j\right>$ can be expanded as a linear combination of $N$-electron basis functions $\left|\Phi_i\right>$

$$\begin{aligned}
\left|\Psi_j\right>=\sum_{i=1}^M c_{ij}\left|\Phi_j\right>
\end{aligned}
$$

In the case of HF theory, this expansion had a single element ($M=1$), i.e. a single Slater determinant made of the occupied HF one-electron orbitals.
In general, there are $M$ possible $N$-electron basis functions to be used, where a complete basis is reached if $M$ is infinite.

To better understand the idea behind CI theory, we can express the $N$-electron basis function as an expansion of "excitations" from the HF "reference" determinant:



$$\begin{aligned}
\left| \Psi_j \right> = c_0 \left|\Phi_0 \right> +\sum_{ra} c_{a}^{r}\left|\Phi_{a}^{r}\right>+\sum_{a<b,r<s} c_{ab}^{rs}\left|\Phi_{ab}^{rs}\right> + \dots
\end{aligned}$$

where $\left|\Phi_{a}^{r}\right>$ indicates the Slater determinants formed by replacing the spin-orbital $a$ in $\left|\Phi_0\right>$ with the spin orital $r$, and so on. Every $N$-electron Slater determinant can be described by the set of $N$ spin orbitals from which it is formed, and this set is often referred to as **configuration**. Thus, the **configuration interaction** methods is nothing more than the matrix solution of the time-independent non-relativistic Schrödinger equation, using the (truncated) expression for $\left|\Psi_j\right>$, as expressed above.

In practice, the CI expansion is typically truncated according to excitation level for computational tractability. **CIS** will include all excitations where one electron is promoted from an occupied orbital to an unoccupied one. Similarly, **CISD** will include all single and double excitations, and so on for **CISDT**, **CISDTQ**, etc. If all possible $N$-electrons excitations are taken into account, the porocedure is called **full CI**. If the one-electron basis is also complete (never in practice since we are using a computer, but it may be in theory), we have **complete CI**.

In practice, Full CI has been performed for very small molecules for benchmarks studies. CIS is sometimes used for approximate excited state calculations, while otherwise CI method is not often used because it is too expensive  and other methods give results of comparable quality at lower cost.



## Møller-Plesset Perturbation Theory
Perturbation methods assume that the problem under investigation only differs slightly from a problem which has already been solved, exactly or approximately.
In quantum mechanics, perturbation methods can be used to add corrections to solutions which employ an independent particle approximation, and the theoretical framework is then called Many-Body Perturbation Theory (MBPT).

According to Rayleigh-Schrödinger perturbation theory, an instantaneous
perturbation of a system described by a Hamiltonian $\hat{\mathrm{H}}_0$
is described by the perturbed Hamiltonian 

$$\begin{aligned}
\hat{\mathrm{H}} = \hat{\mathrm{H}}_0 + \lambda V.\end{aligned}$$

 For a
sufficiently weak perturbation, the eigenstates and eigenvalues may then
be expanded in a power series: 

$$\begin{aligned}
& \bra{\Psi} = \bra{\Psi^{(0)}} + \lambda\bra{\Psi^{(1)}} + \lambda^2 \bra{\Psi^{(2)}} + \dots\\
 & E_\Psi = E_\Psi^{(0)} + \lambda E_\Psi^{(1)} + \lambda^2 E_\Psi^{(2)} + \dots\end{aligned}$$


The perturbing operator $\hat{\mathrm{V}}$ which is introduced in
Møller-Plesset perturbation theory is the difference between the true
ground state Hamiltonian and the Hartree-Fock Hamiltonian; hence, the
perturbation may be written in terms of excited Slater determinants
(which also imposes orthonormality). By carrying out the expansion,
collecting terms of the same order and applying the Slater-Condon rules
(see chapter 5.4 of the course script), one concludes that only
doubly-excited Slater determinants can contribute to the second- and
third-order term. Only the fourth-order energy will include up to
quadruply excited determinants. By truncating the expansion at second
order, one arrives at the MP2 expression for the energy, where electron
correlation is now included as a perturbation to the uncorrelated
Hartree-Fock wavefunction: 

$$\begin{aligned}
E_0^{(2)} = \frac{1}{4} \sum_a \sum_b \sum_r \sum_s \frac{\left|\Bra{ab}\Ket{rs}\right|^2}{\epsilon_a+\epsilon_b-\epsilon_r-\epsilon_s},\end{aligned}$$


where $a,b$ denote occupied, $r,s$ denote virtual orbitals and
$\epsilon$ are the respective energy eigenvalues. 

The total energy is
given by the perturbative contribution and the Hartree-Fock energy:

$$\begin{aligned}
E_0^{total} = E_0^{HF} + \sum_{n=1} E_0^{(n)}.\end{aligned}$$

 (We note
*en passant* that the first-order Møller Plesset energy is nothing but
the expression for the total Hartree Fock energy, such that the
zero-order term is given by a sum over orbital eigenvalues.) The MP
approach is often accurate enough; however, it is not variational,
*i.e.* the resulting MPn energy may be lower than the true ground-state
energy.