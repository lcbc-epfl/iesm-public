# FAQ
<!--
TEMPLATE FOR Q AND A


:::{admonition} Question
:class: tip, dropdown
Answer
:::
-->


:::{admonition} What are multi-reference systems?
:class: tip, dropdown
In this course we often discuss systems in which a single electronic configuration, aka a single Slater Determinant like we use in HF, can accurately describe the system in a particular state (ground state or a specific excited state). However, there are many systems in which a single configuration (single Slater Determinant) does not accurately capture the system at a particular state and we refer to such systems as multi-reference. We would expect to find that these systems have strong static correlation energy contributions because static correlation is the contribution of correlation energy due to degenerate and near-degenerate electronic configurations. In these cases, we can employ other methods to better describe our systems, like multi-reference configuration interaction (MRCI). No need to worry about which multi-reference methods you could choose at this moment, but it is helpful to know what is meant by multi-reference and how the term multi-reference relates to static correlation energy. 

Here we present three examples in which multi-reference methods should be considered:

**Ozone:**
* Ozone absorbs in visible and near-infrared pointing to low-lying, near-in-energy excited states
* Ozone has a good amount of diradical character and isn't represented accurately by a single electronic configuration. 
* Why does this matter? We can't assume that small molecules are "safe" to represent with single Slater determinant. If we observe near-degenerate electronic configurations for a system's ground or low-lying excited states, we should consider pursuing multi-reference calculation methods.
* Further reading: [T. Tsuneda, H. Nakano and K. Hirao](https://aip.scitation.org/doi/pdf/10.1063/1.470378) and [Y. Zhao et al.](https://pubs.acs.org/doi/10.1021/jp811054n). Only need to skim over the beginning of introductions and abstracts. 

**Transition Metals:**
* Due to partially unoccupied d-orbitals transition metal-systems typically have many near-degenerate electronic configurations. Strong dynamic and static correlation in these systems!
* Why does this matter? Transition metal chemistry is critical to understand (many enzymes include them) and in order to study these systems we must find methods which accurately capture their multi-reference character. 
* Further reading: [A. Khedkar and M. Roemelt](https://pubs.rsc.org/en/content/articlehtml/2021/cp/d1cp02640b). See Figure 9 near end of this review paper.

**Making/Breaking Bonds:**
* In reactions where bonds are being broken and made we need to be able to represent a system as it exists partially through these electron configuration rearrangements in which two configurations of the electrons might be close in energy
* $N_2$ dissociation is a classic test case system for new multi-reference approach 
* Why does this matter? For obvious reasons we want to understand the molecular systems involved in chemical reactions : ) Being able to adequately model systems in which electrons are in the process of rearranging requires flexibility to represent multiple configurations near in energy. 
* Further reading: [J. Almlöf et al.](https://onlinelibrary.wiley.com/doi/epdf/10.1002/qua.560360838). This is a 1989 paper discussing challenge of $N_2$ dissociation energy calculations. [D. Kats](https://aip.scitation.org/doi/10.1063/1.4892792). You only need to skim beginning of Results section where they test several multi-reference methods against $N_2$ dissociation. 

**In sum:**
Systems which have near-degenerate electronic configurations or which are in the process of making/breaking bonds are not adequately represented by a single Slater Determinant for a given state, such as the ground state. We call these kinds of systems "multi-reference" because multiple electron configurations represent a given state, ground or excited. These systems experience strong static correlation and require treatment with post-HF methods which incorporate multi-reference representations! 
:::


:::{admonition} Why might one perform a Configuration Interaction Singles (CIS) calculation?
:class: tip, dropdown
We commonly dicuss truncated confguration interaction using the CISD method, which incorporates single and double excitations. Due to [Brillouin's theorem](https://en.wikipedia.org/wiki/Brillouin%27s_theorem) we understand that its only with the onset of double excitations that we recover correlation energy for our ground state wavefunction. So is there any value in preforming a CIS calculation with only single excitations included? Yes! CIS is helpful in excited state studies in particular. Below are some additional details.

**Pros for CIS:**
* Fast and therefore applicable to larger systems 
* Can calculate interesting properties such as vertical excitation energies, charge densities because we can calculate the excited state with analytical gradients 
* CI methods are variational 

**Cons for CI methods in general, including CIS:**
* If you use HF as the reference wavefunction you need a system that can be well-represented by a single reference wave function (If we need to represent systems with multireference nature we might choose a different method)
* Like the reference HF system, CIS does not include electron correlation for the excited states and will overestimate excitation energies

**Pro or Con depending on your study:**
* According to Brillouin's theorem, singly excited determinants do not interact directly with reference HF determinant (see proof here) and therefore CIS does not provide improvements to the ground state energy. However, CIS does improve the energies of the excited states. So if you're interested in excited stated CIS can be useful for your study!

Response based on these resources:
University of California Santa Barbara course pages: [one](https://people.chem.ucsb.edu/kahn/kalju/chem126/public/elspect_cis.html) and [two](https://people.chem.ucsb.edu/kahn/kalju/chem226/public/task2C.html) 
And writings from Professor Sherrill from Georgia Institute of Technology [here](http://vergil.chemistry.gatech.edu/notes/cis/cis.pdf)
:::


:::{admonition} What is the difference between Configuration Interaction Method and the Coupled Cluster Method?
:class: tip, dropdown
In the configuration interaction (CI) methods, we define our many electron wavefunction as a linear combination of Slater determinants of electronic configurations describing excitations from a reference ground state determinant. In practice, 1) we do not have a complete, infinite basis set so complete CI with an infinite basis set is out the window AND 2) we usually have to truncate the expansion at singles and doubles (CISD) for computational reasons meaning Full CI with infinite excitations for a selected one-electron basis is often not tangible either. However, CISD can still be very useful for recovering some of the correlation energy. Furthermore, since CI-methods are variational we can happily minimize the total energy with respect to the coefficients in front of the sums of the different excited Slater determinants.  

```{math}
     |\Psi^{CI} \rangle = C_{0} |\Phi_{0} \rangle + \sum_{a}\sum_{r} C^{r}_{a} |\Phi^{r}_{a} \rangle + \sum_{a} \sum_{b} \sum_{r} \sum_{s} C^{rs}_{ab} |  \Phi^{rs}_{ab} \rangle + \cdots.
``` 


In coupled cluster (CC) we adopt a similar mindset to CI in the sense of including excited states from a reference (usually HF), however, we do so in an exponential expansion of cluster operators. This provides a very nice advantage! CC includes all excitations of a given type (S, D, T, etc) to infinite order. In reality, the excitations are physically finite due to number of MOs/excitations possible. When we expand our cluster operators as a Taylor expansion, we see a non-linear parameterization which allows us to efficiently capture multiple excitations: $\hat{T}_2$\hat{T}_2$ recovers quadruple excitations for example. Herein lies the power of CC. These non-linear terms allow for the inclusion of higher excitations even when we truncate at double excitations enabling this method to be size-consistent and convergent very quickly to a Full CI limit. We recommend reading more about CC on our page about its theory and application [here](https://lcbc-epfl.github.io/iesm-public/Lecture/CC.html)

   ```{math}
    \exp(\hat{T}) | \Phi_0 \rangle = (1 + \hat{T} + \frac{1}{2!} \hat{T}^2
     + \frac{1}{3!} \hat{T}^3 + \cdots ) | \Phi_0 \rangle.
```

**Key Similarities:**
* CI and CC are both wavefunction based post-HF methods aimed to recover the correlation energy missing from HF.
* CI and CC both take into account excited electronic configurations from a reference (usually ground state HF) in linear combinations, but differ in how they handle these linear combinations. 

**Key Differences:**
* CI is variational, CC is NOT variational.
* Truncated CI (like CISD) is not size-consistent or size-extensive, CC is size-extensive and size-consistent as long as the reference wavefunction is size consistent.
* CI's ansatz exhibits a linear combination of sums of Slater determinants describing excitations from a reference wavefunction. CC's ansatz uses exponential cluster operators to generate excited states from a reference wavefunction.
* While CCSD is slightly more expensive than CISD, CCSD is size-consistent method and it is more accurate at capturing electron correlation at the S and D truncation level than CISD.
:::



:::{admonition} What is the normal ordering in Coupled Cluster theory?
:class: tip, dropdown
A product of creation and and annihilation operators in second quantization is said to be normal ordered when all creation operators are to the left of all annihilation operators in the product. Concerning the Couple Cluster theory, the cluster operator $\hat{T}$ is written as a sum of excitation operators $\hat{T}_1$,  $\hat{T}_2$,  $\hat{T}_3$, $\dots$ corresponding to all single, double, triple, ... excitations, and these operators can be expressed as normal-ordered products of creation and annihilation operators. 

$$
\begin{aligned}
\hat{T}_1 &= \sum_a \sum_r t_a^r \hat{a}^\dagger_r\hat{a}_a\\
\hat{T}_2 &= \sum_{a,b} \sum_{r,s} t_{ab}^{rs} \hat{a}^\dagger_s\hat{a}^\dagger_r\hat{a}_b\hat{a}_a\\
        &\dots
\end{aligned}
$$

Where the sum corresponding to the annihilation operators is restricted to the occupied states of the system ($a$,$b$,$c$,$\dots$), and the one for the creation operators to the unoccupied states ($r$,$s$,$t$,$\dots$).

Additional note (**more detailed discussion**):
Note that by restricting the sum as above, it turns out that the only difference that the ordering would make is in the phase of the wavefunction. For example in the case of he elements of $\hat{T}_1$:

$$
\begin{aligned}
\hat{a}^\dagger_r\hat{a}_a \Ket{a b c d \dots} &= \hat{a}^\dagger_r \Ket{b c d \dots} = \Ket{r b c d \dots} \\
\hat{a}_a \hat{a}^\dagger_r\Ket{a b c d \dots} &= \hat{a}_a \Ket{r a b c d \dots} = - \Ket{r b c d \dots} \\
\end{aligned}
$$

where the $-$ sign comes from the commutation relations. However, in the general case such as when deriving the equations for Coupled Cluster theory, the sums run over all the possible states and there it is fundamental to express the operators as normal ordered products.
:::


:::{admonition} What is the role of self-interaction in DFT?
:class: tip, dropdown
One of the key failings of Kohn–Sham density functional theory with approximate density functionals in common use is self-interaction error.

The energy is a functional of the single-particle density, so there is no way to precisely distinguish two-body Coulomb interactions from self-interaction: the interaction of each electron with the entire electron density (including its own density) is considered as a Coulomb energy. The removal of the self-interaction energy from the Coloumb energy is done by the exchange correlation functional, but since this functional can be only approximated, DFT always suffers from self-interaction.

J. P. Perdew and A. Zunger proposed a self-interaction correction scheme (PZ-SIC, [Physical Review B, 1981](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.23.5048)) which subtracts, orbital by orbital, the contribution that the Hartree and the Exchange Correlation
functionals would make if there was only one electron in the system. However, this correction is not able to account for all the SIE. 

Extension of PZ-SIC and other correction methods have been proposed, but in general it is recognized that approximate density functionals in common use do not totally remove the SIE.
(Further reading by [Tsuneda, T. & Hirao, K.](https://aip.scitation.org/doi/10.1063/1.4866996) )
:::


