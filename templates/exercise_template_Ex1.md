# Exercise 1

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

 Calculate the vector product $\mathbf{c}=\mathbf{a}\times\mathbf{b}$
    with 

   $$
    \begin{aligned}
     \mathbf{a} = \left(\begin{matrix}
     2 \\ 6 \\ 4
     \end{matrix}\right)
     \quad
     \mathbf{b} = \left(\begin{matrix}
     5 \\ 1 \\ 7
     \end{matrix}\right)
     \end{aligned}
    $$

  and, for the same $\mathbf{a},\mathbf{b}$, the scalar product
    
   $$
    \begin{aligned}
     d = \mathbf{a}\cdot \mathbf{b}
     \end{aligned}
   $$
:::

Your answer here

:::{admonition} Exercise 2
:class: exercise
 Evaluate the matrix product $\mathbf{C} = \mathbf{A}\mathbf{B}$.

   $$
    \mathbf{A} =\begin{aligned}
     \left(\begin{matrix}
     6 & 8 &2 \\ 9 & 1 & 5 \\ 7 & 4 & 3
     \end{matrix}\right),\quad\mathbf{B}=
      \left(\begin{matrix}
     9 & 6 & 7 \\ 5 & 4 & 4 \\  3 & 2 & 8
     \end{matrix}\right).
     \end{aligned}
    $$

:::

Your answer here

:::{admonition} Exercise 3
:class: exercise
Evaluate the determinant for the matrix $\mathbf{A}$.
    
 $$
    \mathbf{A}=\begin{aligned}
     \left(\begin{matrix}
     1 & 1 & 2 \\ 1 & 0 & 2 \\ 2 & 2 & 3
     \end{matrix}\right)
     \end{aligned}
 $$

:::

Your answer here

:::{admonition} Exercise 4
:class: exercise
 Does the exponent of an operator always satisfy the relation
    $e^{\hat{A}+\hat{B}} = e^{\hat{A}}e^{\hat{B}}$ ? Start from the
    definition of the matrix exponential.
:::

Your answer here

:::{admonition} Exercise 5
:class: exercise
Find the eigenvalues and eigenvectors of the matrix $\mathbf{A}$.
    
  $$
    \mathbf{A} =\begin{aligned}
     \left(\begin{matrix}
     2 & 1 \\ -1 & 4
     \end{matrix}\right)
    \end{aligned}
  $$

:::

Your answer here

:::{admonition} Exercise 6
:class: exercise

 Show that if the product $\mathbf{C}=\mathbf{A}\mathbf{B}$ of two
    Hermitian matrices is also Hermitian, then $\mathbf{A}$ and
    $\mathbf{B}$ commute.

:::

Your answer here

:::{admonition} Exercise 7
:class: exercise

Explain the connection between the Heisenberg uncertainty principle and
the commutation relation.
:::

Your answer here

:::{admonition} Exercise 8
:class: exercise

 What is the meaning of a multiplication of a bra and a ket
    
  $$
    \begin{aligned}
     \left<a\middle|b\right>,
     \end{aligned}
  $$
    
   and, conversely, an operator formed by a ket and a bra? 

  $$
    \begin{aligned}
     \hat{\mathrm{O}} = \left|a\right>\left<b\right|
     \end{aligned}
  $$

:::

Your answer here

:::{admonition} Exercise 9
:class: exercise
 Given a basis $\left\{\psi\right\}$ for which 
    
   $$
    \begin{aligned}
     \left<\psi_i\middle|\psi_j\right> = \delta_{ij},
     \end{aligned}
   $$
   where $\delta_{ij}$ is the Kronecker delta, for any  state $\Psi$ 

  $$
    \begin{aligned}
     \Ket{\Psi} = \sum_j c_j\Ket{\psi_j},
     \end{aligned}
   $$
   the inner product is defined as 

   $$
     \begin{aligned}
     \left<\Psi\middle|\Psi\right> = 1.
     \end{aligned}
   $$

   Show that this holds only as long as    
   
   $$
    \begin{aligned}
     \sum_j c_j^2 = 1,
     \end{aligned}
    $$

   where the $c_j$ are the aforementioned expansion coefficients.

:::

Your answer here

:::{admonition} Bonus Exercise 10
:class: exercise

 Prove that, given the above conditions,
    $c_j=\left<\psi_j\middle|\Psi\right>$.

:::

Your answer here

:::{admonition} Exercise 11
:class: exercise
 Diagonalise the matrices $\mathbf{A}$ and $\mathbf{B}$. Specify which one is Hermitian.
    
 $$
    \mathbf{A}=\begin{aligned}
     \left(\begin{matrix}
     1 & 1-i \\ 1+i & 2
     \end{matrix}\right)
     , \quad
     \mathbf{B} =\left(\begin{matrix}
     1 & 1 \\ 0 & 1
     \end{matrix}\right)
     \end{aligned}
 $$

:::

Your answer here

:::{admonition} Bonus Exercise 12
:class: exercise
 Prove that the eigenvalues of a Hermitian operator are
    real.
:::

Your answer here

:::{admonition} Exercise 13
:class: exercise

 Give the position and the momentum operators (consider only one
    dimension) in the position representation.

:::

Your answer here

:::{admonition} Exercise 14
:class: exercise

Give the commutator of the position and linear momentum operators in
    the position representation (consider one dimension only).
:::

Your answer here

:::{admonition} Exercise 15
:class: exercise
  Is the electronic Hamiltonian $\hat{H}_{el}$ a linear operator and
    why (not)?
:::

Your answer here

:::{admonition} Exercise 16
:class: exercise
 Show that, if two operators $\hat{\mathrm{A}}$, $\hat{\mathrm{B}}$
    commute and if $\Ket{\psi}$ is an eigenvector of $\hat{\mathrm{A}}$,
    $\hat{\mathrm{B}}\Ket{\psi}$ is an eigenvector of
    $\hat{\mathrm{A}}$, too, with the same eigenvalue.

**Bonus**:  If $\Ket{\psi}$ is part of a set of degenerate
    eigenvectors, show that the subspace spanned by the eigenvalues of
    $\hat{\mathrm{A}}$ is invariant under the action of
    $\hat{\mathrm{B}}$.
:::

Your answer here

:::{admonition} Exercise 17
:class: exercise
 Demonstrate that, if two hermitian operators $\hat{\mathrm{A}}$,
    $\hat{\mathrm{B}}$ commute and ${\Ket{\psi_1}}$, ${\Ket{\psi_2}}$
    are eigenvectors of $\hat{\mathrm{A}}$ associated to different
    eigenvalues, then the matrix element
    $\Bra{\psi_1}\hat{\mathrm{B}}\Ket{\psi_2}$ vanishes.
:::

Your answer here

:::{admonition} Bonus Exercise 18
:class: exercise
Show that the potential energy operator
    $\hat{\mathrm{V}}(\mathbf{r})$ is multiplicative when applied to the
    real-space wavefunction.
:::

Your answer here

:::{admonition} Bonus Exercise 19
:class: exercise

The link between position and momentum representation is
given by a Fourier transform. Explain how this relates to the Heisenberg
uncertainty principle.
:::

Your answer here

:::{admonition} Exercise 20
:class: exercise

In a system that consists of only two states (such as an electron spin
in a magnetic field, where the electron spin can be in one of two
orientations), the Hamiltonian has the following matrix elements:
$H_{11}=a, \ H_{22}=b, \ H_{12}=d, \ H_{21}=d$. How would you determine
the energy levels $E$ and the eigenstates $\mathbf{\Psi}$ of the system?
(You do not need to solve this problem explicitly, merely outlining the
procedure is sufficient.)

:::

Your answer here

:::{admonition} Exercise 21
:class: exercise
Define two vectors, `ϕ1` and `ϕ2`, with two elements each, that are normalized, in the sense $\langle\phi_i|\phi_i\rangle=1$, and orthogonal in the sense that $\langle\phi_i|\phi_j\rangle=0$.

**Hint:** In `numpy` a vector `v` with the two elements `1` and `2` is defined through the command
```
v=np.array([1,2])
```
:::

Your answer here

:::{admonition} Exercise 22
:class: exercise
Show that $\phi_1$ and $\phi_2$ are normalized and orthonormal

**Hint:** Here are reported some useful `numpy` functions to work with vectors:
* `v.dot(w)` - inner product (scalar product) of two vectors `v`, `w`
* `v.conj()` - complex conjugate of a vector `v`
* `v.conj().dot(w)` - inner product of $v^\dagger w$

:::

Your answer here