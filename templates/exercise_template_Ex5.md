# Exercise 5

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

* Calculate the HF energy for Boron using the 6-311+G** basis set, then determine the value of the correlation energy for boron assuming an "experimental" energy of -24.608 Hartrees ([Schaefer III, Henry F., and Frank E. Harris. "Electronic Structure of Atomic Boron." Physical Review 167.1 (1968): 67](https://journals.aps.org/pr/abstract/10.1103/PhysRev.167.67)).  
* Using the same basis set, perform an energy calculation with CISD and full CI. 
* Using the same basis set, perform an energy calculation with MP2, MP3 and MP5. 
* Using the same basis set, perform an energy calculation with CCSD and CCSD(T).

Determine the percentage of the correlation energy recovered for HF, MP2, MP5, CCSD, CCSD(T). 

Compare the performances of the different methods. In particular, you will see that some of the methods seem to overestimate the correlation recovered. How is it possible? (*Hint:* Think both about the theoretical aspects of the methods and *how* we are computing the recovered correlation energy).
:::

Your answer here

:::{admonition} Exercise 2
:class: exercise 
Perform the calculations below and complete the following table.

 |Method:         |   HF   | MP2  |  MP3  |          Exp.          |
 | :--------------| :----: | :--- | :---- |  :-------------------- |
 |$E^{F\cdot}$    |        |      |       |        n/a             |
 |$E^{H_3C\cdot}$ |        |      |       |        n/a             |
 |$E^{CH_3F}$     |        |      |       |        n/a             |
 |$E^{BDE}$       |        |      |       |  109.2 kcal mol$^{-1}$ |
:::

Your answer here

:::{admonition} Exercise 3
:class: exercise 
Why is it a reasonable choice to use Hartree-Fock geometries and
    wavefunctions as a starting point for optimisations at the
    Post-Hartree-Fock level? What is the advantage and how is this
    approach justified?
:::

Your answer here

:::{admonition} Exercise 4
:class: exercise 
Why do you think it is reasonable to choose not to carry out a geometry optimisation for mp3?
:::

Your answer here

:::{admonition} Exercise 5
:class: exercise 
Is the homolytic cleavage of the H$_3$C-F bond likely, based on the
    BDE that you calculated? (Think of radical processes in general.)
:::

Your answer here

:::{admonition} Exercise 6
:class: exercise 
What is the trend in energies when moving from HF over MP2 to MP3 for your calculations? Does this series converge? Do you expect the same trend for higher order MPn methods? Why? 

*Hint*: You can check the convergence for MP2 and MP3 by running the code cell below.
:::

Your answer here

:::{admonition} Exercise 7
:class: exercise 
Comment on the accuracy of the HF approach for this system. If the
    error associated with HF or with MPn bigger, and why?
    (*Hint*: Think in terms of the scale of the absolute energy of the
    reaction, as well as of the different components of the system.)
:::

Your answer here

:::{admonition} Exercise 8
:class: exercise 

Assess and comment on the performance of the different methods with respect to experimental values. Can you think of possible reasons for differences between the experimental and computed values?
:::

Your answer here