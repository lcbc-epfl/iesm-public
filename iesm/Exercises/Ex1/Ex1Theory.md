
# Theory
## Operators 

In classical mechanics, an observable is described by a function.
Instead, in quantum mechanics, an observable is represented by a linear
operator that acts on a wavefunction. An operator is itself a function
that, when applied to the state of a system, returns another function. A
simplified view would describe it as an instruction to carry out some
*operation* on a function to obtain the desired result - this may be
anything ranging from a simple multiplication to differentiation,
integration etc. (Strictly speaking, the linear operators used in
quantum mechanics are special cases of a linear mapping
$V \rightarrow W$ where $V = W$ - linear algebra plays a crucial role in
quantum mechanics.)

### Eigenfunctions and eigenvalues

Applying an operator $\hat{\mathrm{A}}$ to some function $f$ can result
in the function being changed, but it may also result in the operator
returning the same function, multiplied by a scalar: 

$$\begin{aligned}
\hat{\mathrm{A}} f = \lambda f.\end{aligned}$$

 The multiplicative
constant $\lambda$ is the *eigenvalue* of the equation, and the function
$f$ is referred to as the *eigenfunction* of the operator
$\hat{\mathrm{A}}$. These terms are derived from the German word
"eigen", meaning "its own", *i.e.* an eigenfunction of an operator is
implied to belong to said operator. (We note *en passant* that the set
of eigenvalues of an operator is called its *spectrum*.)

Together, the eigenfunctions form a *complete basis* such that any
general function $g$ may be expressed in terms of a linear combination
of the eigenfunctions: 

$$\begin{aligned}
\hat{\mathrm{A}} f_i &= \lambda_i f_i\\
g &= \sum_i c_if_i,\end{aligned}$$

 with $c_i$ being the expansion
coefficient and the sum running over all $f_i$. The effect of an
operator on an arbitrary function $g$ can thus be expressed by
decomposing $g$ in terms of its *basis functions*: 

$$\begin{aligned}
\hat{\mathrm{A}}g = \hat{\mathrm{A}}\sum_i c_if_i = \sum_i c_i\hat{\mathrm{A}}f_i = \sum_i c_i \lambda_i f_i.\end{aligned}$$


A quite comprehensive list of quantum mechanical operators can be found
at the end of this chapter.

### Applying several operators: Commutators 

For some operators such as simple multiplications, the order in which
the operators are applied to the function does not matter. Consider this
(trivial) example: 

$$\begin{aligned}
x\cdot y\cdot f(x) = y\cdot x\cdot f(x).\end{aligned}$$

 Turning to
derivatives, however, this is not the case anymore: 

$$\begin{aligned}
x\cdot \frac{\partial}{\partial x} f(x) \ne \frac{\partial}{\partial x} x\cdot f(x).\end{aligned}$$


It is trivial to see that it is indeed relevant in which order operators
are applied to a function. We therefore define the commutator of two
operators as: 

$$\begin{aligned}
\left[\hat{\mathrm{A}},\hat{\mathrm{B}}\right] = \hat{\mathrm{A}}\hat{\mathrm{B}} -\hat{\mathrm{B}}\hat{\mathrm{A}} .\end{aligned}$$


Two operators $\hat{\mathrm{A}},\hat{\mathrm{B}}$ are said to *commute*
if $\left[\hat{\mathrm{A}},\hat{\mathrm{B}}\right]=0$; if they commute,
the order in which they are applied to a function does not matter - if
they do not, i.e. if the commutator is nonzero, it does matter. Note
that the commutator plays a crucial role in quantum mechanics, as it
determines whether two observables can be simultaneously determined
(*cf.* the Heisenberg uncertainty principle). Commuting operators share
the same eigenfunctions (or, *vice versa*, operators sharing the same
eigenfunctions will commute).

## Linear Algebra and Quantum Mechanics: Hermiticity and Matrix Representations


From here on, operators will be applied to some (wave)function $\phi$,
$\psi$ rather than an arbitrary function $f$. This is just a matter of
notation and goes, of course, without loss of generality. (Note that we
chose not to write $\phi(x)$ or the like, because it is not relevant
whether we use the position or the momentum wavefunction, *cf.* the
bra-ket notation that will be discussed below.)

(exercise1)=
## Hilbert Space and Bra-Ket Notation 

Recalling that any arbitrary function can be expressed as a weighted
superposition of eigenfunctions of their underlying operator, one needs
to define a mathematical *functional space* in which these
eigenfunctions reside. An N-dimensional *euclidian space* is restricted
to real numbers, but the eigenfunctions we are interested in may as well
be complex valued (Cartesian space is just an example of a 3-dimensional euclidian space).

The concept of euclidian space was generalised by Hilbert onto an
infinite dimensional complex space of square integrable functions, the
*Hilbert space*. (A Hilbert space is a *Banach space*; a vector space
that has a well-defined metric such that the distance between two
vectors as well as the magnitude of a vector can be computed.)

Each instantaneous state is described by a unit vector (meaning of norm 1)or a *state
vector* in Hilbert space. Just like a position vector in cartesian
space, the state vector is expressed in terms of the orthogonal basis
vectors that are formed by all the eigenfunctions. (The chapter on
Hermitian operators will justify this. One should also note that 'all
eigenfunctions' refers to all eigenfunctions of an operator to which the
Hilbert space under consideration is associated.) All these
eigenfunctions taken together encode all the relevant information: Being
a complete set (a *basis*), they are all that is needed to describe any
arbitrary function $g$ (*cf.* preceeding chapter).\
 \
A proper notation that accurately describes vectors with an infinite
(but countable) number of elements - such as those in Hilbert space -
was introduced by Paul Dirac. In *bra-ket (or Dirac) notation*, a vector
in Hilbert space is denoted by a *ket* 

$$\begin{aligned}
 \Ket{\Psi} = \left(\vdots\right),
 \end{aligned}$$

 which is a column vector. In one-to-one correspondence
to the space formed by the kets, there exists a dual space consisting of
*bra* vectors: 

$$\begin{aligned}
 \Bra{\Psi} = \left(\cdots\right),
 \end{aligned}$$

 which is the adjoint of the ket (*i.e.* a row vector
that is the complex conjugate of the ket). As both bra and ket are normalized vectors, their norm is 1. In Hilbert space, an inner product of two
vectors $\left<\Phi,\Psi\right>$ is always defined. For $\Phi=\Psi$, the
inner product defines the norm of the vectors - we will leave further
specification as an exercise question. For two orthogonal basis vectors
$\psi_i,\psi_j$, we have that: 

$$\begin{aligned}
 \left<\psi_i\middle|\psi_j\right> = \delta_{ij},
 \end{aligned}$$

 where $\delta_{ij}$ denotes the Kronecker delta. Note
that bras and kets themselves are not specified as being dependent on
position or momentum, simply because the position and momentum
wavefunctions are obtained by *projecting* their representation out of a
ket in Hilbert space, as will be shown later. (However, time dependence
of a state is often implicit.)\
 \
Applying bra-ket notation to the previously discussed description of any
function in terms of eigenfunctions, any state of the system is given as
a linear combination: 

$$\begin{aligned}
 \Ket{\Psi} = \sum_j^{\infty} c_j\Ket{\psi_j},
 \end{aligned}$$

 where we introduced capital greek letters for the state
of the system, and lower case letters for its basis (its
eigenfunctions.) The expansion coefficients are simply the projections
of the basis $\psi_j$ onto the total state function $\Psi$ (thinking of
cartesian vectors, the projection of the x axis out of some vector
yields the length of the vector on the x axis - the concept for a
wavefunction expansion is the same). 

$$\begin{aligned}
 c_j = \left<\psi_j\middle|\Psi\right>
 \end{aligned}$$

 Because every state is normalised, just like the basis
vectors it is built upon, any state $\Psi$ must also be of the same
norm. This requirement is conserved if and only if the normalisation
$\sum_j c_j^2 = 1$ is imposed.

### Valid Quantum Mechanical Operators: Linearity and Hermiticity 

In order for an operator to be a valid quantum mechanical operator, it
must be *linear* 

$$\begin{aligned}
 \hat{\mathrm{A}}\left(\psi + \phi\right) = \hat{\mathrm{A}}\psi + \hat{\mathrm{A}}\phi.
 \end{aligned}$$

 For operators that describe a state that is physically
observable, it is further required that the operator be *Hermitian*. (In
the strict mathematical sense, this requirement implies linearity, but
physicists use the less specific definition of hermiticity as given
below.) A Hermitian operator is defined as an operator that is equal to
its conjugate transpose: 

$$\begin{aligned}
 \hat{\mathrm{A}}^T = \overline{\hat{\mathrm{A}}}.\end{aligned}$$


(Strictly speaking, this is true for an operator in a finite vector
space $V$; a Hermitian operator being a special case of a self-adjoint
operator. Hermitian operators are normal operators, whence the spectral
theorem holds.) The eigenvalues of a Hermitian operator have some useful
properties; they are *real* (which is a direct consequence of the
definition of a Hermitian operator, as it shall be pointed out later
again) and *orthogonal* to each other (this is why basis vectors in
Hilbert space are orthogonal - and this is what allows for algebraic
transformations in euclidian space to be easily extended onto the
complex Hilbert space).

### Matrix Representation of Operators

The definition of a Hermitian operator being based on properties known
from matrices implies a link between the two. Indeed, any operator can
be written in a matrix form.

Consider another system $\Phi$ that is defined analogously to $\Psi$:


$$\begin{aligned}
 \Ket{\Psi} = \sum_j^{\infty} c_j\Ket{\psi_i} \quad ; \quad
 \Ket{\Phi} = \sum_k^{\infty} d_k\Ket{\psi_k},
 \end{aligned}$$

 and an operator such that 

$$\begin{aligned}
 \Ket{\Phi} = \hat{\mathrm{A}}\Ket{\Psi}.
 \end{aligned}$$

 (Since a Hermitian operator is a linear map
$V \rightarrow V$, the basis remains unchanged, but the expansion
coefficients differ.) The *matrix elements* of the operator
$\hat{\mathrm{A}}$ in the basis $\left\{\psi\right\}$ are now given as


$$\begin{aligned}
 A_{ij} = \Bra{\psi_i}\hat{\mathrm{A}}\Ket{\psi_j},
 \end{aligned}$$

 describing how the operator acts between the orthogonal
basis vectors $\phi_i$ and $\phi_j$.

From the above, we deduce that 

$$\begin{aligned}
 \sum_k^{\infty} d_k\Ket{\psi_k} = \hat{\mathrm{A}} \sum_j^{\infty} c_j\Ket{\psi_j},
 \end{aligned}$$



 and after multiplication by
$\sum_i^{\infty}\bra{\psi_i}$, exploiting orthogonality of the basis and
applying the above definition of the operator's matrix elements, it
follows that: 

$$\begin{aligned}
 d_i = \sum_j A_{ij}c_j,
 \end{aligned}$$



  where the summation over an infinite but countable
number of elements is implicitly assumed. This equation can be rewritten
in matrix form: 

$$\begin{aligned}
 \left(\begin{matrix}
 d_1 \\
 d_2 \\
 \vdots \\
 d_i
 \end{matrix}\right)
 =
 \left(\begin{matrix}
 A_{11}  & A_{12} & \cdots & A_{1j} \\
 A_{21}  & A_{22} & \cdots & A_{2j} \\
 \vdots  & \vdots & \ddots & \vdots  \\
 A_{i1}  & A_{i2} & \cdots & A_{ij}
 \end{matrix}\right)
 \left(\begin{matrix}
 c_1 \\
 c_2 \\
 \vdots \\
 c_j
 \end{matrix}\right),
 \end{aligned}$$

 $c,d$ are vectors of expansion coefficients of
$\Phi,\Psi$ respectively. Operators for which $A_{ij} = 0$ are, just
like their underlying matrix, *diagonal*.

## The Wavefunction and its Properties - Projections out of Hilbert Space


So far, any state $\Psi$ was discussed as an abstract unit vector in
Hilbert space that is expanded over a basis of eigenfunctions. In this
chapter, it will be demonstrated how the familiar picture of a
wavefunction in position representation is extracted from Hilbert space
and what properties such a wavefunction has. The theory outlined so far
will be applied to the energy eigenvalue problem of Schrödinger (the
time-independent Schrödinger equation).

### The Wavefunction in Position Representation 

The more abstract bra-ket notation and the notation of the wavefunction
as being position or momentum dependent are often used interchangeably.
Position and momentum wavefunctions are obtained by *projecting* the
state function in Hilbert space onto position or momentum space using
the respective operators $\hat{\mathbf{r}}$ and $\hat{\mathbf{p}}$.
First, we note that the (non-square integrable) real space basis at a
point $\mathbf{r}_0$ is given by a delta function, which is the
eigenfunction of the real space operator $\hat{\mathbf{r}}_0$:
$$\begin{aligned}
 \xi_{\mathbf{r}_0}(\mathbf{r}) = \delta(\mathbf{r}-\mathbf{r}_0)
 \end{aligned}$$

 In bra-ket notation, we shall denote this basis
function $\Ket{\mathbf{r}_0}$. The corresponding *projection operator*
$\hat{P}$ is given by: 

$$\begin{aligned}
 \hat{P}_{\mathbf{r}_0} = \Ket{\mathbf{r}_0}\Bra{\mathbf{r}_0},
 \end{aligned}$$

 with the closing relation: 

$$\begin{aligned}
 \int \Ket{\mathbf{r}_0}\Bra{\mathbf{r}_0} \mathrm{d}\mathbf{r}_0 = \mathbb{1},
 \end{aligned}$$

 where $\mathbb{1}$ is a unit matrix. Applying the projection
operator onto the wavefunction, one has 

$$\begin{aligned}
 \Ket{\psi} =  \int \Ket{\mathbf{r}_0}\Braket{\mathbf{r}_0}{\Psi} \mathrm{d}\mathbf{r}.
 \end{aligned}$$

 The representation in the momentum basis can be
developed analogously. The inner product $\Braket{\mathbf{r}_0}{\Psi}$
can be interpreted as the coefficient of the expansion of $\Ket{\Psi}$
on the basis $\Ket{\mathbf{r}_0}$. After multiplication by a suitably
chosen ket and making use of the orthogonality of the basis, one then
readily finds: 

$$\begin{aligned}
 \Psi\left(\mathbf{r},t\right) &= \left<\mathbf{r}\middle|\Psi\right>\\
 \Psi\left(\mathbf{p},t\right) &= \left<\mathbf{p}\middle|\Psi\right>,
 \end{aligned}$$

 where the position and momentum vectors $\mathbf{r}$
and $\mathbf{p}$ are 3-dimensional. (Often, $\mathbf{r}$ is just used
for the length of a vector in position representation, and $\mathbf{q}$
is used for coordinates. We will however resort to using $\mathbf{r}$
throughout this script to denote a vector of (cartesian) coordinates.)
Position and momentum wavefunction still contain all the information we
need, and they conserve the properties of unit vectors in Hilbert space
as discussed in the preceeding sections. Specifically, the L$^2$ norm in
real space is naturally given by: 

$$\begin{aligned}
 \left<\Psi\middle|\Psi\right> = \int \Psi^\ast\left(\mathbf{r},t\right)\Psi\left(\mathbf{r},t\right)\mathrm{d}\mathbf{r}.
 \end{aligned}$$



### Probabilities and Observables

Whereas a wavefunction contains all the neccessary information, it lacks
any direct physical interpretation. Its square, however, fulfills the
requirements of a *probability distribution*. Namely, for a
many-electron wavefunction, where N electrons are associated to N
coordinate vectors $\left\{\mathbf{r}_i\right\}$: 

$$\begin{aligned}
 P\left(\mathbf{r}_1,\mathrm{d}\mathbf{r}_1;\dots;\mathbf{r}_N,\mathrm{d}\mathbf{r}_N\right)
 = \left|\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\dots,\mathbf{r}_N\right)\right|^2\mathrm{d}\mathbf{r}
 = \left|\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\dots,\mathbf{r}_N\right)\right|^2\mathrm{d}\mathbf{r}_1,\mathrm{d}\mathbf{r}_2,\dots,
 \mathbf{d}\mathbf{r}_N.
 \end{aligned}$$

 The square of the wavefunction corresponds to the
probability of finding all $N$ electrons simultaneously in the
infinitesimal volume elements
$\mathrm{d}\mathrm{r}_1,\mathrm{d}\mathrm{r}_2,\dots, \mathrm{d}\mathrm{r}_N$.
The probability of finding electron 1 in $\mathrm{d}\mathbf{r}_1$ and
all the other electrons anywhere else is given by the N-1 dimensional
integral: 

$$\begin{aligned}
 P\left(\mathbf{r}_1,\mathrm{d}\mathbf{r}_1\right) = \mathrm{d}\mathbf{r}_1
 \idotsint \Psi^\ast\left(\mathbf{r}_1,\mathbf{r}_2,\dots,\mathbf{r}_N\right)\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\dots,\mathbf{r}_N\right)
 \mathrm{d}\mathbf{r}_2,\dots,\mathrm{d}\mathbf{r}_N
 \end{aligned}$$

 Similarly,
$P\left(\mathbf{r}_1,\mathrm{d}\mathbf{r}_1;\mathbf{r}_2,\mathrm{d}\mathbf{r}_2\right)$
will be given by a N-2 dimensional integral.\
 \
All physically measurable quantities, the *observables*, are associated
to a corresponding Hermitian operator $\hat{\mathrm{O}}$ (it is common
to denote operators that correspond to an observable by the letter $O$).
Applying this operator to the state function of a system returns its
eigenvalue if the state function is an eigenfunction of the operator;
for a generic function $\Psi$, each eigenvalue of the underlying basis
$\left\{\psi\right\}$ may be obtained, with a probability depending on
the expansion coefficient $c_i$ of the eigenfunction. The mean or
*expectation value* of an observable $O$ is then given by:


$$\begin{aligned}
 \left<\hat{\mathrm{O}}\right> = \frac{\Bra{\Psi}\hat{\mathrm{O}}\Ket{\Psi}}{\left<\Psi\middle|\Psi\right>} = \Bra{\Psi}\hat{\mathrm{O}}\Ket{\Psi}
 \end{aligned}$$

 because of the normalisation condition.

\
 \
From the properties of a Hermitian operator, we have that


$$\begin{aligned}
 \int \Phi^\ast\left(\mathbf{r}\right)\hat{\mathrm{O}}\Psi\left(\mathbf{r}\right)\mathrm{d}\mathbf{r}
 = \left( \int \Psi^\ast\left(\mathbf{r}\right)\hat{\mathrm{O}}\Phi\left(\mathbf{r}\right)\mathrm{d}\mathbf{r} \right)^\ast
 \end{aligned}$$

 which proves that its eigenvalues are real, as stated
earlier. This is a requirement for a physical observable and
demonstrates why Hermitian operators are of great value in quantum
mechanics.

### Solving the Eigenvalue Problem of the Time-Independent Schrödinger Equation 

The preceeding theoretical considerations shall now be put to good use.
Until now, it has not been stated which operator of interest spans the
Hilbert space. The time-independent Schrödinger equation is an
eigenvalue problem that applies the system's Hamiltonian (the sum of
kinetic and potential energy) 

$$\begin{aligned}
 \hat{\mathrm{H}} = \hat{\mathrm{T}}+\hat{\mathrm{V}}
 \end{aligned}$$

 onto a wavefunction, returning the expectation value of
the energy, the energy eigenvalue: 

$$\begin{aligned}
 \hat{\mathrm{H}}\Ket{\Psi} = E\Ket{\Psi}.
 \end{aligned}$$

 The time evolution of the system at any point is given
by the time-dependent Schrödinger equation: 

$$\begin{aligned}
 \hat{\mathrm{H}}\Ket{\Psi} = i\hbar\frac{\partial}{\partial t}\Ket{\Psi}
 \end{aligned}$$

 The former is an eigenvalue problem, the latter is
not.\
 \
One may rewrite the time-independent Schrödinger equation for an
arbitrary state $\Psi$ in matrix form. 

$$\begin{aligned}
 \hat{\mathrm{H}}\Ket{\Psi} &= E\Ket{\Psi} \\
 \sum_j c_j \hat{\mathrm{H}}\Ket{\psi_j} &= E \sum_j c_j\Ket{\psi_j}
 \end{aligned}$$

 All constants can be moved in front of the operator,
and after multiplying by the bra $\bra{\psi_i}$, one obtains


$$\begin{aligned}
 \sum_j c_j\Bra{\psi_i}\hat{\mathrm{H}}\Ket{\psi_j} = \sum_j H_{ij}c_j = Ec_i.
 \end{aligned}$$

 Consequently, one recovers an infinite-dimensional
matrix eigenvalue problem: 

$$\begin{aligned}
 \left(\begin{matrix}
 H_{11}  & H_{12} & \cdots & H_{1j} \\
 H_{21}  & H_{22} & \cdots & H_{2j} \\
 \vdots  & \vdots & \ddots & \vdots  \\
 H_{i1}  & H_{i2} & \cdots & H_{ij}
 \end{matrix}\right)
 \left(\begin{matrix}
 c_1 \\
 c_2 \\
 \vdots \\
 c_j
 \end{matrix}\right)
 =
 E 
 \left(\begin{matrix}
 c_1 \\
 c_2 \\
 \vdots \\
 c_i
 \end{matrix}\right).
 \end{aligned}$$

 For a general matrix eigenvalue problem, there exist
$n$ solutions with eigenvalues $E_k$. Generalising to the above problem
results in: 

$$\begin{aligned}
 \sum_i H_{ij}c_{jk} = c_{ik}E_k.
 \end{aligned}$$

 This introduces the additional index $k$, and the final
eigenvalue problem that is to be solved is given by: 

$$\begin{aligned}
 \left(\begin{matrix}
 H_{11}  & H_{12} & \cdots & H_{1j} \\
 H_{21}  & H_{22} & \cdots & H_{2j} \\
 \vdots  & \vdots & \ddots & \vdots  \\
 H_{i1}  & H_{i2} & \cdots & H_{ij}
 \end{matrix}\right)
 \left(\begin{matrix}
 c_{11}  & c_{12} & \cdots & c_{1k} \\
 c_{21}  & c_{22} & \cdots & c_{2k} \\
 \vdots  & \vdots & \ddots & \vdots  \\
 c_{j1}  & c_{j2} & \cdots & c_{jk}
 \end{matrix}\right)
 =
 \left(\begin{matrix}
 c_{11}  & c_{12} & \cdots & c_{1k} \\
 c_{21}  & c_{22} & \cdots & c_{2k} \\
 \vdots  & \vdots & \ddots & \vdots  \\
 c_{i1}  & c_{i2} & \cdots & c_{ik}
 \end{matrix}\right)
 \left(\begin{matrix}
 E_{1}  & 0      & \cdots & 0 \\
 0      & E_{2}  & \cdots & 0 \\
 \vdots & \vdots & \ddots & \vdots  \\
 0      & 0      & \cdots & E_{k}
 \end{matrix}\right).
 \end{aligned}$$

 The eigenvalue problem of the time-independent
Schrödinger equation *can now be solved as the classical eigenvalue
problem of a matrix*, by resorting to simple linear algebra.

### Bosons and Fermions: Use of Determinants to Describe Many-Body Wavefunctions 

Quantum mechanics imposes certain symmetry constraints on permutations
of indistinguishable particles. For bosons, the wavefunction must remain
unchanged upon exchange of particles. For fermions (such as electrons)
instead, it has to change sign for an odd number of permutations.
Formally,



$$\begin{aligned}
 \wp \Psi\left(\mathbf{r}_1,\mathbf{r}_2,\dots,\mathbf{r}_N\right)
 = \epsilon_p \Psi\left(\mathbf{r}_1,\mathbf{r}_2,\dots,\mathbf{r}_N\right),\end{aligned}$$


such that $\epsilon_p = +1$ and $\epsilon_p = -1$ for an even and an odd
number of permutations respectively. This poses a problem for the
construction of a many-particle (many-electron) wavefunction.\
 \
If one wishes to write a many-particle wavefunction as a simple product
of one-particle wavefunctions 

$$\begin{aligned}
 \Phi\left(\mathbf{r}_1,\dots,\mathbf{r}_N\right) = \prod_i^N \phi_i\left(\mathbf{r}_i\right),
 \end{aligned}$$

 the resulting wavefunction will be even upon
permutation of a single electron: 

$$\begin{aligned}
 \Phi(\textbf{r}_1,\textbf{r}_2)=\phi_1(\textbf{r}_1) \phi_2(\textbf{r}_2)
 \neq - \phi_1(\textbf{r}_2) \phi_2(\textbf{r}_1) = -\Phi(\textbf{r}_2,\textbf{r}_1).
 \end{aligned}$$

 A simple product of single-particle wavefunctions
clearly violates the permutation requirement. A determinant of a matrix,
however, has exactly the desired property: 

$$\begin{aligned}
 \det A =
 \begin{vmatrix}
 a_{11} & \cdots & a_{1N} \\
 \vdots & \ddots & \vdots \\
 a_{N1} & \cdots & a_{NN}
 \end{vmatrix}
 = \sum_{i=1}^{N!} \left(-1\right)^\alpha a_{1p_1}a_{2p_2}\dots a_{Np_N},
 \end{aligned}$$

 where $\alpha$ is the number of permuted pairs
$(p_i,p_j)$ with $p_i > p_j$ and $i < j$; the sum runs over all
permutations $(p_1,p_2,\dots,p_N)$ of the set $(1,2,\dots,N)$. Upon
exchange of two columns, the determinant changes sign (which is easily
demonstrated using a simple 2x2 determinant). Exploiting this property,
one defines a general N-electron wavefunction: 

$$\begin{aligned}
 \Phi\left(1,2,\dots,N\right) = \frac{1}{\sqrt{N!}}
 \begin{vmatrix}
 \phi_{1} \left(\mathbf{r}_1\right) &  \phi_{2} \left(\mathbf{r}_1\right) & \cdots & \phi_{N} \left(\mathbf{r}_1\right) \\
 \phi_{1} \left(\mathbf{r}_2\right) & \phi_{2} \left(\mathbf{r}_2\right) & \cdots & \phi_{N} \left(\mathbf{r}_2\right)\\
 \vdots & \vdots & \ddots  & \vdots  \\
 \phi_{1} \left(\mathbf{r}_N\right) & \phi_{2} \left(\mathbf{r}_N\right) & \cdots & \phi_{N} \left(\mathbf{r}_N\right)
 \end{vmatrix}
 \end{aligned}$$

 where the $\phi_i$ are one-electron wavefunctions and
$\frac{1}{\sqrt{N!}}$ is a normalisation factor. For a two-electron
wavefunction, this reduces to 

$$\begin{aligned}
 \Psi\left(\mathbf{r}_1,\mathbf{r}_2\right)
 = \frac{1}{\sqrt{2}}
 \begin{vmatrix}
 \psi_1\left(\mathbf{r}_1\right) & \psi_2\left(\mathbf{r}_1\right) \\
 \psi_1\left(\mathbf{r}_2\right) & \psi_2\left(\mathbf{r}_2\right)
 \end{vmatrix}
 \end{aligned}$$

 and 

$$\begin{aligned}
 \Psi\left(\mathbf{r}_2,\mathbf{r}_1\right)
 = \frac{1}{\sqrt{2}}
 \begin{vmatrix}
 \psi_2\left(\mathbf{r}_1\right) & \psi_1\left(\mathbf{r}_1\right) \\
 \psi_2\left(\mathbf{r}_2\right) & \psi_1\left(\mathbf{r}_2\right)
 \end{vmatrix}
 = \Psi\left(\mathbf{r}_1,\mathbf{r}_2\right)
 \end{aligned}$$

 which is in agreement with the permutation requirement.
