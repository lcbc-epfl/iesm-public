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
Which of the following basis sets does not contain polarisation functions?\
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
    c) ...take polarisation into account.\
    d) ...enhance the description of core orbitals.
```

Your answer here

```{admonition} Exercise 5
:class: exercise 
Using the information given about the 3-21G contraction coefficients:\
    a) Give the basis functions corresponding to the 1s, 2s and 2p orbitals of Carbon (**Hint**: use information from **Fig. 2.2** ).\
    b) If you wish to calculate the Hartree-Fock energy of a carbon atom,
    how many coefficients are *optimised* during the calculation?
```

Your answer here

```{admonition} Exercise 6
:class: exercise 
You wish to calculate the wavefunction of ethylene C$_2$H$_2$ using the 6-31G\* basis. \
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

:::{admonition} Exercise 9
:class: exercise 
Include in your report the coordinates you set for your water molecules and a screenshot of how it looks like in 3D representation.
:::

Your answer here

```{admonition} Exercise 10
:class: exercise
How do you calculate the spin multiplicity of a species? Compare the case of the water molecule to the previous example of the hydrogen atom.
```

Your answer here

:::{admonition} Exercise 11
:class: exercise 
Compute energy calculations for the different basis sets indicated below with a loop similar to the one used before.  Include a table of the the calculated energies. Specify what is the difference between the basis sets that we used.

**Bonus:** which of the additional functions introduced with respect to the `6-31G` basis set are more reasonable for the present case, i.e. a water molecule? Why?
:::

Your answer here

```{admonition} Exercise 12
:class: exercise
Have a look at the log files produced so far and answer the following questions:
1.  What is the significance of the statement *Energy and wave function converged*?

2.  What is the meaning of the different *iter* preceding *Energy and wave function converged*? 
    Compare the number of cycles for the different basis sets.
```

Your answer here