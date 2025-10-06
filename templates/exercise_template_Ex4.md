# Exercise 4

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
Define $S_{ij}$ using Dirac notation.
:::

Your answer here

:::{admonition} Exercise 2
:class: exercise
For an orthonormal basis, what does the overlap integral array, `S`, look like?
:::

Your answer here

:::{admonition} Exercise 3
:class: exercise
 Use `B` and `B_dagger` and the matrix rules above to calculate the matrix `S`.
 :::

Your answer here

:::{admonition} Exercise 4
:class: exercise
Describe how the notation of the `np.einsum` command correlates to the implicit summation formula written above.
:::

Your answer here

:::{admonition} Exercise 5
:class: exercise
 Use the function `np.einsum()` to calculate the matrix `S`, and confirm that your answer is the same as above.
 :::

Your answer here

:::{admonition} Exercise 6
:class: exercise
Propose a different orthonormal basis, modify `phi1` and `phi2`, and verify that `S` still has the same form. There are infinitely many choices. It isn't complex... or *is* it?!
:::

Your answer here

:::{admonition} Exercise 7
:class: exercise
How many electrons are there in total in H$_2$O?
How many occupied molecular orbitals would you expect?
:::

Your answer here

:::{admonition} Exercise 8
:class: exercise
 Explain the shape (number of rows and columns) of `S` in terms of the AO basis set we chose.
 :::

Your answer here

:::{admonition} Exercise 9
:class: exercise

 Based on your observations of `S` in the AO basis, answer the following questions
1. What do the diagonal elements of `S` indicate?
2. What do the off-diagonal elements of `S` indicate?
3. Does the Gaussian atomic orbital basis set form an orthonormal basis? 

:::

Your answer here

:::{admonition} Exercise 10
:class: exercise
Does the result of your extra evaluation agree with what you determined previously?
:::

Your answer here

:::{admonition} Exercise 11
:class: exercise
 Use the function `np.linalg.inv()` to calculate the inverse of `S`, and the function `splinalg.sqrtm()` to take its (matrix) square root. Execute the code below and examine the matrix `A`.
 :::

Your answer here

:::{admonition} Exercise 12
:class: exercise
 What do you observe about the elements of `A`? Is the matrix real or complex? Is the matrix symmetric or not?
 :::

Your answer here

:::{admonition} Exercise 13
:class: exercise
Use the orthogonalization matrix `A` to transform the overlap matrix, `S`. Check the transformed overlap matrix, `S_p`, to make sure it represents an orthonormal basis.
:::

Your answer here

:::{admonition} Exercise 14
:class: exercise

The product A S A does not take the complex conjugate transpose of A. What conditions (properties of A) make that ok?

:::

Your answer here

:::{admonition} Exercise 15
:class: exercise
Based on the definition of $C'$, propose a definition of $C$ in terms of $A$ and $C'$. Justify your equation.
:::

Your answer here

:::{admonition} Exercise 16
:class: exercise
 In the cell below, use the core Hamiltonian matrix as your initial guess for the Fock matrix. Transform it with the same A matrix you used above.  To calculate the eigenvalues, `vals`, and eigenvectors, `vecs`, of matrix `M` using  `vals, vecs = np.linalg.eigh(M)`.
 :::

Your answer here

:::{admonition} Exercise 17
:class: exercise
 Display, i.e., `print`, the coefficent matrix and confirm it the correct size
 :::

Your answer here

:::{admonition} Exercise 18
:class: exercise
Use `A` and the formula you proposed previously to transform the coefficient matrix back to the AO basis. Confirm that the resulting matrix appears reasonable, i.e., similar size and magnitude
:::

Your answer here

:::{admonition} Exercise 19
:class: exercise

 Build the density matrix, `D`, from the occupied orbitals, `C_occ`, using the function `np.einsum()`. **Hint** Look at {eq}`DensityMatrix`
 :::

Your answer here

:::{admonition} Exercise 20
:class: exercise
Define J  in terms of the density matrix, `D`, and the electron repulsion integral tensor, `I`, using `np.einsum()`. 
:::

Your answer here

:::{admonition} Exercise 21
:class: exercise
 Define K  in terms of the density matrix, `D`, and the electron repulsion integral tensor, `I`, using `einsum()`. 
 :::

Your answer here

:::{admonition} Exercise 22
:class: exercise

 Define F in terms of H, J, and K. (Recall {ref}`hf`)

 :::

Your answer here

:::{admonition} Exercise 23
:class: exercise
 Calculate the SCF energy based on H, F, and D using `np.einsum()`.
:::

:::{margin} Hint
 The right hand side of the equation is the sum of the product of two terms, each of which has two indices (p and q). The result, E, is a number, so it has no indices. In `einsum()` notation, this case will be represented with the indices for the matrices on the left of the `->`, and no index on the right of the `->`. For example, in the case of just one matrix, the sum of all its elements of a matrix `M` is `sum_of_m = np.einsum('pq->',M )`. In your answer below, be sure to account for any modifications required of an element-wise product of two matrices.
:::

Your answer here

:::{admonition} Exercise 24
:class: exercise
 Based on the result of the calculation in {ref}`basisset`, is this a reasonable answer? 
 :::

Your answer here

:::{admonition} Exercise 25
:class: exercise
 Describe a procedure (i.e. identify the steps) that will update coefficients and compute a new density matrix based on the updated values of the Fock matrix. 
 :::

Your answer here

:::{admonition} Exercise 26
:class: exercise
 Using the procedure proposed above, calculate the updated coefficients
 :::

Your answer here

:::{admonition} Bonus Exercise 27
:class: exercise
Modify the value of E_conv and describe its effect the number of iterations.Provide your code, the output of the SCF calculation and the number of iterations.
:::

Your answer here