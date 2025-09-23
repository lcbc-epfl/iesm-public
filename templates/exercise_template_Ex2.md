# Exercise 2

Student:  Firstname Lastname    Sciper: 000000

:::{admonition} Please use this template to submit your answers. 

If you had to modify code from the notebook, please include the modified code in your submission either as screenshot or in a 

```
\begin{lstlisting}[language=Python]
\end{lstlisting}
```


environment. 

You only need to include the code cells that you modified.

Note, that references to other parts of the documents aren't resolved in this template and will show as `??`. Check the text of the exercises on website for the reference

:::

```{admonition} Exercise 1
:class: exercise 
A minimal basis set...\
    a) ...always gives the lowest energy.\
    b) ...is optimized for small molecules.\
    c) ...contains one basis function for each atomic orbital only.
```

Your answer here

```{admonition} Exercise 2
:class: exercise 
A split-valence basis set...\
    a) ...contains two basis functions for each valence atomic orbital.\
    b) ...doubles the CPU time of the calculation.\
    c) ...attributes a different number of basis functions to valence and
    core orbtials.
```

Your answer here

```{admonition} Exercise 3
:class: exercise 
Which of the following basis sets does not contain polarization functions?\
    a) 6-31G$^\ast$\
    b) 6-31G(d,p)\
    c) 3-21+G\
    d) DZP
```

Your answer here

```{admonition} Exercise 4
:class: exercise 
Diffuse functions are added to a basis set to...\
    a) ...save CPU time.\
    b) ...better represent electronic effects at larger distances from the nuclei.\
    c) ...take polarization into account.\
    d) ...enhance the description of core orbitals.
```

Your answer here

```{admonition} Exercise 5
:class: exercise 
Using the information given about the 3-21G contraction coefficients:\
    a) Give the basis functions corresponding to the 1s, 2s and 2p orbitals of Carbon (**Hint**: use information from **Fig. 2.2** ).\
    b) If we wish to construct a single molecular orbital $\phi_m(\mathbf{r}_m)$ (which is a one-particle molecular orbital) for a carbon atom with a spin multiplicity *S=5* using the 3-21G basis set (so that our 1s, 2s, and 2p orbitals are all occupied), how many coefficients and exponants coming from contracted GTOs are fixed, and which expansion coefficients will vary for the calculation of the Hartree-Fock energy? 
```

Your answer here

```{admonition} Exercise 6
:class: exercise 
You wish to calculate the wavefunction of acetylene C$_2$H$_2$ using the 6-31G\* basis. \
   Indicate the number of basis functions and the number of Gaussian primitives that will be used in the calculation.
```

Your answer here

```{admonition} Exercise 7
:class: exercise 
Include a table of the the calculated energies using the three different basis sets, specifying for each of them the number of basis functions used. Compare the energies with the analytical value for the H atom, given by the analytical expression: 

$$
 E = -\frac{1}{2} m_e c^2\alpha^2,
$$

where $\alpha$ is the fine structure constant. 

$$\begin{align}
m_e = 0.910953\cdot10^{-30} kg\\
c = 2.99792458\cdot10^8 m s^{-1}\\
\alpha = 7.2973525376\cdot10^{-3}\\
N_A = 6.0221367\cdot10^{23}mol^{-1}
\end{align}$$
Pay attention to the units - use atomic units or kcal$\cdot$mol$^{-1}$ throughout!
```

Your answer here

```{admonition} Exercise 8
:class: exercise 
What is the influence of the basis set size on the accuracy of the result? How do the split-valence bases compare to STO-3G?
```

Your answer here

```{admonition} Exercise 9
:class: exercise 
How does the resulting relative energies for helium compare to the hydrogen case? And why?
```

Your answer here

:::{admonition} Exercise 10
:class: exercise 
Include in your report the coordinates you set for your water molecules and a screenshot of how it looks like in 3D representation.
:::

Your answer here

```{admonition} Exercise 11
:class: exercise
How do you calculate the spin multiplicity of a species? Compare the case of the water molecule to the previous examples of the hydrogen atom and the helium atom.
```

Your answer here

:::{admonition} Exercise 12
:class: exercise 
Compute energy calculations for the different basis sets indicated below with a loop similar to the one used before.  Include a table of the the calculated energies. Specify what is the difference between the basis sets that we used.

**Bonus:** which of the additional functions introduced with respect to the `6-31G` basis set are more reasonable for the present case, i.e. a water molecule? Why?
:::

Your answer here

```{admonition} Exercise 13
:class: exercise
What can you say about the relative energies and stability of a linear water molecule compared to our original bent case? And why?
```

Your answer here

```{admonition} Exercise 14
:class: exercise
What can you say about the stability of the bent and linear beryllium hydride conformations? How does it compare to the water case and why?
```

Your answer here