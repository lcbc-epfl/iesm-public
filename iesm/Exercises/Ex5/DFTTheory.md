
# Exact Theory and Approximate Functionals: Comparison of Various Density Functionals


The successful application of DFT requires some knowledge on where, why
and how approximations to the density functional are made. The following
is a brief review of the *Kohn-Sham Density Functional Theory* as it is
ubiquitously used today.

## The Hohenberg-Kohn Theorems

In 1964, Hohenberg and Kohn provided two theorems for 'the ground state
of an interacting electron gas in an external potential $v(\mathbf{r})$'
(such as the external potential that is due to the nuclei). The first
theorem states that an external potential $v_{ext}(\mathbf{r})$ is, up
to a constant, uniquely determined by the density $\rho(\mathbf{r})$.
Since $v_{ext}(\mathbf{r})$ fixes the Hamiltonian of the system, *the
many-particle ground state is a unique functional of the density*.
Therefore, a density functional $F[\rho]$ exists such that the energy
$E_v$ of a system subjected to the potential $v_{ext}$ is given by


$$\begin{aligned}
E_{v}[\rho] = \int v_{ext}(\mathbf{r})\rho(\mathbf{r}) \mathrm{d}\mathbf{r} + F [\rho].\end{aligned}$$


Hohenberg and Kohn also provided a variational principle stating that
*the density minimising the total energy corresponds to the ground-state
density* (*cf.* course script, chapter 4.3): 

$$\begin{aligned}
E_{v}^{GS} [\rho] = \min_{\Psi \rightarrow \rho} \Bra{\Psi[\rho]}\mathrm{\hat{H}}\Ket{\Psi[\rho]}\end{aligned}$$



## The Kohn-Sham Formalism

Although the exact density functional exists, it is not known, and
finding approximations to it is quite a formidable task. In 1965, Kohn
and Sham introduced a formalism that, in practice, considerably
simplifies the determination of the functional $F[\rho]$. According to
Hohenberg and Kohn, one may separate the Coulomb energy $J$ out of eq.
89: 

$$\begin{aligned}
E_{v}[\rho] = \int v_{ext}(\mathbf{r})\rho(\mathbf{r}) \mathrm{d}\mathbf{r} + J[\rho] + G[\rho],\end{aligned}$$


which leaves a functional $G[\rho]$ that takes all the non-classical
terms into account. Kohn and Sham suggested to further split this term:


$$\begin{aligned}
G[\rho] \equiv T_s[\rho]+ E_{xc}[\rho],\end{aligned}$$

 where $T_s$ is
the kinetic energy of a system of non-interacting particles (*s* stands
for 'single particle') , and $E_{xc}$ is taking care of all
non-classical *exchange-correlation* effects. This
*exchange-correlation* energy will thus be given by the difference
between the non-interacting kinetic energy $T_s$ and the (true)
interacting kinetic energy $T$ of the system, as well as the difference
between classical ($J$) and (true) quantum mechanical interaction
(potential) energy ($V_{ee}$) of the electrons: 

$$\begin{aligned}
E_{xc}[\rho] \equiv \underbrace{T[\rho]-T_s[\rho]}_{\text{kinetic terms}} + \underbrace{V_{ee}[\rho]-J[\rho]}_{\text{potential terms}}\end{aligned}$$


The use of the non-interacting $T_s$ allows for a simple evaluation of
the dominant part of $T$. In order to determine $T_s$, Kohn and Sham
introduced *auxiliary single-particle wavefunctions* $\psi^{(KS)}$, the
purpose of which is to simply yield the correct density $\rho$. The
total energy is then obtained from the density: 

$$\begin{aligned}
\rho\left(\mathbf{r}\right) = \sum_i^N \left|\psi_i^{(KS)}\left(\mathbf{r}\right)\right|^2
 \quad ; \quad
 \int\psi_i^{(KS)*}\left(\mathbf{r}\right)\psi_i^{(KS)}\left(\mathbf{r}\right)d\mathbf{r} = \delta_{ij}.\end{aligned}$$


These single-particle wavefunctions minimise $T_s$ for a given density
$\rho$; they have *no other physical interpretation* (*cf.* the
following section) - they are simply an auxiliary tool, based on the
assumption that the difference $T-T_s$ is much easier to account for in
a functional than the complete $T$ at once. The $\psi^{(KS)}$ are
orbitals that correspond to a system of *non-interacting electrons*
which has the same *density* as the true, physical system. Since the
true ground-state energy of a system is solely given by its density, the
use of an auxiliary (*i.e.* non-physical) wavefunction does not
introduce any error and still yields the exact result.

Taking advantage of the now known expression for the non-interacting
kinetic energy $T_s$, one finds for the energy that:
$$E_v[\rho] = \sum_i^N \int \psi_i^{(KS)*}\left(\mathbf{r}\right)\left(-\frac{1}{2}\nabla^2\right)\psi_i^{(KS)}\left(\mathbf{r}\right)d\mathbf{r}
+J[\rho]+E_{xc}[\rho] + \int\upsilon_{ext}\left(\mathbf{r}\right)\rho\left(\mathbf{r}\right)d\mathbf{r}.$$
We note that $T_s$, although expressed in terms of an auxiliary
wavefunction, is still an implicit functional of the density, as the
auxiliary wavefunctions or *Kohn-Sham orbitals*
$\psi^{(KS)}(\mathbf{r})$ are themselves determined by the density.

By subjecting eq. 95 to a constrained minimisation, *i.e.* by applying
the variational principle, Kohn and Sham derived a set of *single
particle equations* for the Kohn-Sham orbitals $\psi^{(KS)}$ that yield
the ground-state density: 

$$\begin{aligned}
\left[-\frac{1}{2}\nabla^2+\upsilon_{eff}\right]\psi_i^{(KS)} = \epsilon_i\psi_i^{(KS)},\end{aligned}$$


where $v_{eff}$ is an effective potential given by: 

$$\begin{aligned}
\upsilon_{eff} = \upsilon_{ext}\left(\mathbf{r}\right) + \frac{\delta J[\rho]}{\delta \rho\left(\mathbf{r}\right)}
 + \frac{\delta E_{xc}[\rho]}{\delta \rho\left(\mathbf{r}\right)}\end{aligned}$$


or, alternatively, 

$$\begin{aligned}
\upsilon_{eff} = \upsilon_{ext}\left(\mathbf{r}\right)
 + \int \frac{\rho\left(\mathbf{r^\prime}\right)}{\left|\mathbf{r}-\mathbf{r^\prime}\right|}d\mathbf{r^\prime}
 + \upsilon_{xc}\left(\mathbf{r}\right).\end{aligned}$$

 By definition,


$$\begin{aligned}
\upsilon_{xc} \equiv \frac{\delta E_{xc}[\rho]}{\delta \rho\left(\mathbf{r}\right)} \end{aligned}$$


is the *exchange-correlation potential*, the part of the potential that
is due to non-classical effects. Besides the external potential
$v_{ext}$ that uniquely determines the ground-state density, the
single-particle equations contain an additional potential due to the
electron-electron interaction (the Coulomb term), as well as a local
ficticious potential for all non-classical effects $v_{xc}$.

The sum of all the potentials in eq. 98 can be regarded as a 'new'
$v_{ext}^{\prime}$ that fixes the density and thus the ground-state
energy, as proven by Hohenberg and Kohn. To stress its ficticious
nature, this new Kohn-Sham single particle potential is denoted the
*effective potential* $v_{eff}$, and the corresponding Hamiltonian is
referred to as the *effective Hamiltonian* $\mathrm{\hat{H}}_{eff}$.
Given an expression for the *exchange-correlation functional*
$E_{xc}[\rho]$, eq. 96 is now easily solved self-consistently (*cf.*
course script, chapter 8.4.2). The exchange-correlation potential as
defined by eq. 99 and used in eq. 96 is obtained from the
exchange-correlation energy computed in the *previous* cycle; hence, the
procedure calls for a self-consistent solution. (Recall that in
Hartree-Fock theory, this was made neccessary by the dependence of the
Fock operator on the previous iteration; in Kohn-Sham DFT, it is the
functional derivative of the exchange-correlation functional that
imposes this requirement.)

The beauty of the Kohn-Sham approach lies in the mapping of an
interacting, physical problem, onto an artificial, but easy-to-solve
auxiliary non-interacting problem. The real interacting system and the
Kohn-Sham non-interacting system just share the same N-electron density.
The link (mapping) between the two systems is accounted for by the
exchange-correlation functional $E_{xc}[\rho]$.

## Interpretation of the Kohn-Sham Orbitals

In the early years of Kohn-Sham DFT, great emphasis was put on the fact
that, based on their derivation, Kohn-Sham orbitals are *physically
meaningless*. As single-particle orbitals from wavefunction theory are
often the base of a more intuitive interpretation of chemical processes,
this could be regarded as a severe drawback. However, experience shows
that Kohn-Sham orbitals are in praxis very close to the orbitals
obtained from wavefunction-based methods; and they have been used as an
illustrative tool for *e.g.* chemical transformations for many years. It
has been demonstrated that the Kohn-Sham orbitals have an intriguing
interpretation, which is linked to their response to changes of the
exchange-correlation hole (the exchange-correlation hole is quite an
important concept both in wavefunction and density functional theory;
*J. Am. Chem. Soc.*, **1999**, 121, *3414*). We do, however, note *en
passant* that the meaning of single-particle orbitals in general is
quite limited; even in Hartree-Fock theory, the meaningful quantity is
the total wavefunction, *i.e.* the Slater determinant over all occupied
orbitals.

## Approximations 

Until this point, no approximations were invoked at all. The Kohn-Sham
equations will still yield the exact ground-state energy and
ground-state density for a system, given that $E_{xc}$ is known - but
this is not the case. Although more and more properties of the exact
exchange correlation functional were established over the years, there
is no universal analytical expression for it. This is where one needs to
approximate.

An approximate expression for the exchange-correlation functional will,
however, pose a formal problem. Although the Hohenberg-Kohn variational
principle guarantees that the energy of a trial density will always be
an upper boundary to the ground-state energy, this holds only for the
exact density functional. If approximate functionals are to be used, the
variational theorem just holds *for this specific Hamiltonian* (recall
from the preceeding section that the effective potential $v_{eff}$ fixes
the Hamiltonian; since $v_{eff}$ depends on the exchange-correlation
functional, the exchange-correlation functional determines the
Hamiltonian). If the exchange-correlation functional is approximate, the
Hamiltonian is approximate as well, and *the ground-state energy for a
system with an approximate Hamiltonian may be lower than the physical
ground-state energy*. This violates the general form of the variational
theorem, that strictly calls for an upper boundary for the *physical*
system. However, it has to be stressed that this is not a problem of
Density Functional Theory, but of the approximate exchange-correlation
functionals.

Still, the variational theorem holds in a less general sense, such that,
within the *approximate* Hamiltonian, the Kohn-Sham equations will yield
the density that minimises the energy, and thus a ground-state density
(for this specific Hamiltonian). The accuracy is then determined by how
well the approximate Hamiltonian is able to describe the true, physical
Hamiltonian.

## Local Density Approximation: LDA/LSDA 

The question left standing is how to find a reasonable approximation to
the exchange-correlation functional. A first simplification of the
problem can be achieved by splitting the exchange-correlation functional
into an exchange and a correlation functional: 

$$\begin{aligned}
E_{xc}[\rho] = E_x[\rho] + E_c[\rho],\end{aligned}$$

 which allows for a
convenient separation of the problem. Because the exchange contribution
dominates over correlation effects, exchange-correlation functionals are
usually classified according to the derivation of the exchange
functional.

In order to establish an approximation for the exchange functional, one
may refer to the electron gas (*cf.* the Hohenberg-Kohn Theorem).
Namely, for a *uniform*, homogenuous (interacting) electron gas, there
exists an analytical expression for the exchange energy per volume
element. By assuming that the density of a non-homogenuous system can
locally (meaning, at any point $\mathbf{r}$ in space) be described by
that of the uniform electron gas, one arrives at the following
expression for the exchange functional: 

$$\begin{aligned}
E_x^{LDA}[\rho] = -\frac{3q_e^2}{4}\left(\frac{3}{\pi}\right)^{\frac{1}{3}} \int \rho^{\frac{4}{3}} \mathrm{d}\mathbf{r},\end{aligned}$$


which is known as the *Local (Spin) Density Approximation* or LDA (LSDA
if spin is taken into account). The term for the correlation functional
is substantially more complicated and will not be shown here. LDA was
one of the first successful approaches towards an exchange-correlation
functional, with results for molecules and especially solid state
systems being mostly superior to Hartree-Fock, all whilst having a lower
computational cost. The term LDA is frequently used to denote both the
approximation and the functional. For the functional, there exist
different parametrisations for the correlation energy of the uniform
electron gas: They may either be based on analytical expressions, or on
Quantum Monte Carlo results.

With multiple parametrisations for the same approximation, an
appropriate naming scheme is required. Usually, to denote an
exchange-correlation functional, an abbreviation for the exchange
functional is contracted with one for the correlation functional.
Unequivocally, the Slater exchange functional (abbreviated S) is used
for the exchange part of all LDA functionals. The LDA correlation
functional that is predominantely used is based on a parametrisation by
Vosko, Wilk and Nusair, who obtained the correlation energy from Quantum
Monte Carlo results for the uniform electron gas (the Ceperley-Alder
solution). This correlation functional is denoted VWN5. The full
exchange-correlation functional is then abbreviated as SVWN5.

## Generalised Gradient Approximation: GGA

LDA will perform reasonably well for systems with a slowly varying
density, because in such systems, the density will be almost homogenous
between two infinitesimally close points in space. For more fluctuating
densities, however, the assumption that a local description based on the
electron gas is sufficient starts to break down. An additional term in
the exchange functional that is able to describe the local shape of the
density would seem promising. An intuitive approach could include the
gradient of the density; however, such an expression turns out to be
divergent. Instead, a *generalised gradient expansion* can be derived,
resulting in the *Generalised Gradient Approximation* (GGA):


$$\begin{aligned}
E_{x}^{GGA} [\rho] = E_{x} [\rho,\nabla\rho] = \int f(\rho,\nabla\rho) \mathrm{d}\mathbf{r},\end{aligned}$$


However, the general form for a GGA contains parameters that are
undetermined. How they are obtained is a matter of choice (and dispute);
they may either be recovered from imposing certain limits and conditions
on the functional, or by fitting to experimental or accurate quantum
chemical data to minimise the error made by the functional. The former
group of GGAs are referred to as non-empirical, the latter as
(semi-)empirical. The exact limits that the functional should adhere to
may be given by one or several basic physical concepts, including the
exchange hole, the requirement that the uniform electron gas be
recovered, the recovery of a gradient term of a certain order, *etc.*

An example of a popular non-empirical GGA is the exchange functional due
to Perdew, Burke and Ernzerhof (PBE). The modified Perdew-Wang
functional (mPW91) is an example of a GGA where a functional form was
designed to fit *analytical* data. The missing parameters for other GGA
exchange functionals, like the Becke exchange (B), were instead
determined by a semi-empirical fit to exact exchange energies of rare
gas atoms.

Gradient corrected exchange functionals can be combined with various
elaborate correlation functionals, the most popular of which are the
Lee-Yang-Parr correlation functional (LYP), the Perdew correlation
functional from 1986 (P86), the Perdew-Wang correlation functional of
1991 (PW91) and the PBE correlation functional (PBE). In principle, any
correlation functional could be combined with any exchange functional,
but certain combinations will outperform others based on a remarkable
*error cancellation* between the two exchange and correlation part.
Therefore, functionals derived with similar targets and philosophies
will often work better together, whereas mixing of philosophies may give
catastrophic results (for instance, the combination B-PBE will be
ridiculously off). Popular combinations of GGA exchange with correlation
functionals include BLYP, PBE (acronym for PBEPBE), mPWPW91 and BP86.

## Kinetic Energy Density: Meta-GGA

One step beyond the GGA is given by including the second derivative of
the density. In practice, the *kinetic energy density* $\tau$:


$$\begin{aligned}
 \tau = \sum_i \Bra{\psi_i^{(KS)*}}\nabla^2\Ket{\psi_i^{(KS)}},\end{aligned}$$


is used and the general functional form for a *meta-GGA* follows:


$$\begin{aligned}
 E_{x}^{meta-GGA} [\rho] = E_{x} [\rho,\nabla\rho,\tau] = \int f(\rho,\nabla\rho, \tau) \mathrm{d}\mathbf{r}.\end{aligned}$$


Although these functionals are still completely local, they are in a way
able to sense long-range effects due to the second derivative
information. Whereas LDA and GGA are plagued by a self-interaction error
in certain systems, meta-GGAs are already much less prone to this
pitfall. Examples include the TPSS exchange-correlation functional (due
to Tao, Perdew, Staroverov and Scuseria), and the local *Minnesota
functionals* M05-L and M06-L (developed by Donald Truhlar). Whereas TPSS
was derived purely based on theoretical considerations, the Minnesota
functional parameters were determined by a fit to an experimental
database, resulting in a remarkable accuracy for all systems that are
sufficiently close to the training set.

## Hybrid Functionals: Including Exact Exchange 

From Hartree-Fock theory, the expression for the exchange energy of a
single Slater determinant is known: 

$$\begin{aligned}
E_x^{HF} = \sum_i \sum_{j\ne i} \iint \frac{\phi_i^*(\mathbf{r}_1)\phi_j^*(\mathbf{r}_2)\phi_j(\mathbf{r}_1)\phi_i(\mathbf{r}_2)}{|\mathbf{r}_1-\mathbf{r}_2|}
\mathrm{d}\mathbf{r}_2\mathrm{d}\mathbf{r}_1.\end{aligned}$$

 In DFT,
this expression is evaluated based on the Kohn-Sham orbitals, and is
usually denoted the *exact exchange* functional (given that
$\rho \rightarrow \psi^{(KS)}$, $E_x^{HF}$ is still an implicit
functional of the density). It can be shown that the exact exchange
expression corresponds to a certain limit in the non-interacting
Kohn-Sham system (this relation is given by the *adiabatic connection
theorem*). Therefore, *hybrid* density functionals may be constructed by
including both contributions from (meta)-GGA and the exact exchange
term: 

$$\begin{aligned}
\begin{split}
E_x^{hybrid}\left[\rho,\nabla\rho,\left\{\psi^{(KS)}\right\}(,\tau)\right] &= \lambda E_x^{(meta-)GGA} \left[\rho,\nabla\rho(,\tau)\right] +  (1-\lambda) \\
&\times \sum_i \sum_{j} \iint
 \frac{\psi_i^{(KS)*}(\mathbf{r}_1)\psi_j^{(KS)*}(\mathbf{r}_2)\psi_j^{(KS)}(\mathbf{r}_1)\psi_i^{(KS)}(\mathbf{r}_2)}{|\mathbf{r}_1-\mathbf{r}_2|}
\mathrm{d}\mathbf{r}_2\mathrm{d}\mathbf{r}_1.
\end{split}\end{aligned}$$

 Again, the fractional contribution $\lambda$
of the exact exchange to the total exchange functional can be derived
based on theoretical considerations or empirical fitting. Hybrid
functionals have constituted a tremendous breakthrough, as they
especially improved the performance of DFT on barrier heights. The first
successful generation of these functionals combined GGA and the exact
exchange term. This generation includes the probably most popular B3LYP,
the Becke three-parameter hybrid, which combines Becke exchange, the
exact exchange term, the LYP and the VWN correlation functional into one
functional (with three empirically determined fitting parameters). An
analytically derived example is given by the PBE0 hybrid (also named
PBE1PBE), the derivation of which is rather involved in terms of the
adiabatic connection theorem. Especially for barrier heights, the
mPW1PW91 functional has been rather popular, adding exact exchange to
the mPWPW91 GGA. The B3PW91 functional constitutes a further notable
example.

The second generation of hybrid-GGAs (*e.g.* B97 due to Becke) were
presented towards the end of the 1990ies and have improved accuracy over
the first generation. The quite recent (2005 and 2006) Minnesota
functionals M05 and M06 combine a meta-GGA expression with the exact
exchange functional, and all the free parameters were fit to a
benchmarking set of molecules. These highly empirical functionals are of
remarkable accuracy over a wide range of systems, further improving over
the M05-L and M06-L functionals.

