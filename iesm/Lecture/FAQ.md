# FAQ
<!--
TEMPLATE FOR Q AND A


:::{admonition} Question
:class: tip, dropdown
Answer
:::
-->

:::{admonition} What is the role of self-interaction in DFT?
:class: tip, dropdown
One of the key failings of Kohn–Sham density functional theory with approximate density functionals in common use is self-interaction error.

The energy is a functional of the single-particle density, so there is no way to precisely distinguish two-body Coulomb interactions from self-interaction: the interaction of each electron with the entire electron density (including its own density) is considered as a Coulomb energy. The removal of the self-interaction energy from the Coloumb energy is done by the exchange correlation functional, but since this functional can be only approximated, DFT always suffers from self-interaction.

J. P. Perdew and A. Zunger proposed a self-interaction correction scheme (PZ-SIC, [Physical Review B, 1981](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.23.5048)) which subtracts, orbital by orbital, the contribution that the Hartree and the Exchange Correlation
functionals would make if there was only one electron in the system. However, this correction is not able to account for all the SIE. 

Extension of PZ-SIC and other correction methods have been proposed, but in general it is recognized that approximate density functionals in common use do not totally remove the SIE.
(Further reading by [Tsuneda, T. & Hirao, K.](https://aip.scitation.org/doi/10.1063/1.4866996) )
:::