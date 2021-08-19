
```{admonition} Exercise
:class: exercise
The LDA is the simplest approximation to an exchange-correlation
    functional. In what cases would it perform well, and when would you
    expect it to fail?
```
```{admonition} Exercise
:class: exercise
What is a self-interaction error, and which of the methods that you
    used so far will suffer from it?

```
```{admonition} Exercise
:class: exercise
What is the meaning and physical interpretation of the Kohn-Sham
    orbitals?
```
```{admonition} Exercise
:class: exercise
Density Functional Theory is sometimes referred to as being a
    semi-empirical method. Comment on this.
```
```{admonition} Exercise
:class: exercise
In a related matter, it may be mentioned that DFT is
    non-variational. Comment on this statement.
```
```{admonition} Exercise
:class: exercise
Derive a flow chart describing the self-consistent solution of the
    Kohn-Sham equations (eq. 95 to 99). Indicate which terms are
    obtained from the results of the previous cycle, and which terms are
    obtained in the new cycle. For which terms is the initial Kohn-Sham
    orbital guess $\psi_{guess}^{(KS)}$ used?
```
```{admonition} Bonus Exercise
:class: exercise
 In Kohn-Sham DFT, the total energy is *not* simply given
    by a sum over orbital eigenvalues (recall that this is a situation
    similar to what one encounters in Hartree-Fock theory). Instead, one
    finds that 

    $$
    \begin{aligned}
    E = \sum_i^{N} \epsilon_i - J[\rho] + E_{xc}[\rho] - \int \frac{\delta E_{xc}[\rho]}{\delta \rho(\mathbf{r})}\rho(\mathbf{r}) \mathrm{d}\mathbf{r}.\end{aligned}$$


    Explain why this expression is not equal to 

    $$
    \begin{aligned}
    E = \sum_i^N \epsilon_i - J[\rho],
    \end{aligned}
    $$
    
    i.e. why the last
    two terms in eq. 107 do not cancel. #TODO

```
```{admonition}   Bonus Exercise
:class: exercise
 The energy minimisation in DFT is given by the
    functional: 

    $$
    \begin{aligned}
    E_{v} [\rho]= T[\rho] + V_{ee} [\rho] + \int v_{ext}(\mathbf{r})\rho(\mathbf{r}) \mathrm{d}\mathbf{r}.\end{aligned}$$


    Specify where approximations are made. Compare these terms to the
    Kohn-Sham effective single-particle Hamiltonian: 

    $$
    \begin{aligned}
    \mathrm{\hat{H}}_{eff} = \mathrm{\hat{T}}_s + v_{eff} (\mathbf{r}),
    \end{aligned}
    $$
    and elaborate on the connection between the approaches.
```