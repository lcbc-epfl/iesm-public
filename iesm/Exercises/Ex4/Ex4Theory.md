
# Møller-Plesset Perturbation Theory


An accurate description of thermochemical properties, such as reaction
enthalpies, will usually call for a more accurate energy than the
Hartree-Fock energy. Møller-Plesset perturbation theory is often precise
enough to describe such processes, and will therefore be the method of
choice especially for larger systems, where other, more elaborate
methods become computationally untractable.



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
(*cf.* chapter 5.4 of the course script), one concludes that only
doubly-excited Slater determinants can contribute to the second- and
third-order term. Only the fourth-order energy will include up to
quadruply excited determinants. By truncating the expansion at second
order, one arrives at the MP2 expression for the energy, where electron
correlation is now included as a perturbation to the uncorrelated
Hartree-Fock wavefunction: 

$$\begin{aligned}
E_0^{(2)} = \frac{1}{4} \sum_a \sum_b \sum_r \sum_s \frac{\left|\Bra{ab}\Ket{rs}\right|^2}{\epsilon_a+\epsilon_b-\epsilon_r-\epsilon_s},\end{aligned}$$


where $a,b$ denote occupied, $r,s$ denote virtual orbitals and
$\epsilon$ are the respective energy eigenvalues. The total energy is
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