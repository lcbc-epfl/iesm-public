# Exercise 6

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

:::{admonition} Exercise 1
:class: exercise 
Why is it important to construct the starting structures in a specific conformation, although one is carrying out a geometry optimisation? Don't we risk to end up in the same conformation after the optimization, since we are dealing in both cases with the same molecule, i.e. methylcyclohexane?
:::


Your answer here

:::{admonition} Exercise 2
:class: exercise 
Compute the energy of the two conformations and calculate the energy difference at 0 K, $\Delta E_{0K} = E_{\text{axial}} - E_{\text{equatorial}}$, i.e. the A-value, filling the table below. Compare the results of different methods with the experimental value for the  A-Value of the methil group in a methylcyclohexane molecule, **1.74 kcal/mol**. For each method, use both 6-31+G* and 6-31+G** basis sets.

By adding `%%time` at the beginning of each cell, the execution time will be printed out. This quantity is related to the computational cost of the calculation and can help you to compare the different methods.


**You can split up the calculations among yourselves to speed up the process.**


| Method      | E_equatorial (Hartrees) | E_axial (Hartrees) | ΔE(0K) (kcal/mol) | Relative error % | Basis set | Remark (ψ /ρ based ?) | Wall time | 
| ----------- | ----------------------- | ------------------ | ----------------- | ---------------- | --------- | --------------------- | --------- |
| HF          |  |  |  |  |  |  |  |  |
| MP2         |  |  |  |  |  |  |  |  |
| BLYP        |  |  |  |  |  |  |  |  |
| MPW1PW91    |  |  |  |  |  |  |  |  |
| B97-2       |  |  |  |  |  |  |  |  |
| PBE         |  |  |  |  |  |  |  |  |
| TPSS        |  |  |  |  |  |  |  |  |
| M06-L       |  |  |  |  |  |  |  |  |
| M06-2X      |  |  |  |  |  |  |  |  |
| B3LYP-D3BJ  |  |  |  |  |  |  |  |  |
| Reference   | //                      | //                 | 1.74              | Experimental         |

:::


Your answer here

:::{admonition} Exercise 3
:class: exercise 
What kind of basis sets were used for ψ based calculations? On which atoms will polarization and diffuse functions be included? Are we close to the basis set limit? Why, or why not?
:::

Your answer here

:::{admonition} Exercise 4
:class: exercise 
Comment on the performance of the wavefunction based methods and DFT, comparing both accuracy and computational time. 

Can you imagine why some DFT methods perform better than others? How does DFT compare to MP2 and HF? 
Would you expect the exchange-correlation functionals to give similar errors in different systems?

An often cited target for the development of exchange-correlation functionals is an error below *chemical accuracy*, *i.e.* within 1
    kcal mol $^{-1}$ of the accurate result. Explain the accuracy of the results also in light of this.
:::


Your answer here

:::{admonition} Exercise 5
:class: exercise
    Fill the above table with the results of your calculations. Compare the performance of the methods in predicting accurate
    structures.     Is there a trend relating the complexity of the exchange-correlation functional (LDA, GGA, hybrid, ...) to the quality of your results?
    
    **Bonus**: For the DFT methods, specify what approximations are
    used in the exchange functional (you may refer to {ref}`dfttheory`). 
:::

Your answer here

:::{admonition} Exercise 6
:class: exercise
Take a screenshot of the MP2 and DFT SOMOs. How do the orbitals differ from each other? How does the symmetry of the SOMO relate to the predicted structure?
:::

Your answer here

:::{admonition} Exercise 7
:class: exercise
Explain the difference between static and dynamic correlation. Relate this to the different results you obtained for the nitrate radical. What kind of correlation do HF, MP2 and DFT take into account?
:::

Your answer here

:::{admonition} Exercise 8
:class: exercise
If you needed a highly accurate structure and energy for  NO$_3\cdot$, which method would you use? Why?
:::

Your answer here