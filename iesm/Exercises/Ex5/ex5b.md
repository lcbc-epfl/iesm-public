# Density Functional Theory 2 

In this set of exercises, you will assess the performance of various
state-of-the-art density functionals in the prediction of geometric
properties, and you will again compare your results to both wavefunction
theory and experimental data. The second part of this exercise script
constitutes a brief *résumé* of DFT and a description of the various
*exchange-correlation* approximations used.

## Structural Parameters of NO$_3\cdot$: Performance of DFT, HF and MP2

Before diving into the theoretical aspects of exchange-correlation
functionals, you will put a representative selection of functionals to
good use in a notoriously tricky system, the NO$_3\cdot$ radical.
Nitrite radicals are highly reactive species that are rapidly destroyed
by sunlight, but as the sun sets, they start to play an important role
in chemical transformations (in what is called the night-time chemistry
of the atmosphere). There exist various experimental and theoretical
studies of NO$_3\cdot$ (*Phys. Chem. Chem. Phys.*, **2014**, 16,
*19437*), with the experiment indicating a fully symmetric D$_3^h$
structure with equal N-O bond lengths of 1.24 Å and O-N-O bond angles of
120$^\circ$. In this exercise, you will be comparing the performance of
various DFT exchange-correlation functionals, Hartree-Fock theory and
MP2 in predicting these structural parameters. Your input file should
contain the following coordinates:

    %NProcShared=2
    %Mem=1GB
    %Chk=CHECKPOINTNAME
    #P GFINPUT IOP(6/7=3) METHOD/6-31+G* Opt Symmetry=None

    NO3

    0 2
    N  0.000  0.000  0.000
    O  1.400  0.000  0.000
    O -1.000  1.000  0.000
    O -1.000 -1.000  0.000

The new keywords `GFINPUT` and `IOP(6/7=3)` will force Gaussian to write
additional orbital information to the output file, which makes it
possible to visualise the orbitals with Molden. Do not forget to change
the name for the Checkpoint file for each method.

1.  Create inputs for MP2, HF and two of the following density
    functionals (where the Gaussian keyword differs from the functional
    abbreviation, it is given in parentheses): LDA (SVWN5), BLYP, BP86,
    PBE (PBEPBE), B3LYP, B97-2 (B972), M06-L (M06L), M06-2X (M062X),
    TPSS (TPSSTPSS), mPW1PW (mPW1PW91). Your assistants will assign to
    you which functionals to use. For this small system, Hartree-Fock
    and MP2 will be surprisingly fast; however, you may rest assured
    that for larger molecules and basis sets, all the DFT methods will
    outperform MP2 in computational efficiency, with some of them even
    beating Hartree-Fock. Make sure just to submit *one job at once*.
    Open the output files in Molden and complete the following table
    (you can again easily extract this structural information from the
    `ZMAT Editor`):

![image](../images/NO3.png)\

  Method:     $\phi_1$ \[$^\circ$\]   $\phi_2$ \[$^\circ$\]   $\mathbf{r}_1 (O-N)$ \[Å\]   $\mathbf{r}_2 (O-N)$ \[Å\]   $\mathbf{r}_3 (O-N)$ \[Å\]   Symmetry
  ---------- ----------------------- ----------------------- ---------------------------- ---------------------------- ---------------------------- ----------
  Exp.                 120                     120                       1.24                         1.24                         1.24              D$_3^h$
  HF                   All                                                                                                                          
  MP2                  All                                                                                                                          
  SVWN5              Quentin                                                                                                                        
  BLYP                Artur                                                                                                                         
  BP86               Sergei                                                                                                                         
  PBE                Damien                                                                                                                         
  B3LYP               Jann                                                                                                                          
  B97-2              Louise                                                                                                                         
  M06-L             Patricia                                                                                                                        
  M06-2X              Amin                                                                                                                          
  TPSS              Alexandre                                                                                                                       
  mPW1PW91           Heorhiy                                                                                                                        

2.  Compare the performance of the methods in predicting accurate
    structures. For the DFT methods, specify what approximations are
    used in the exchange functional (you may refer to chapter 5.3 to
    obtain this information). Is there a trend relating the complexity
    of the exchange-correlation functional (LDA, GGA, hybrid, ...) to
    the quality of your results?

In order to assess the reliability of an electronic structure
calculation, it is usually not sufficient to simply glance at the
optimised structure and energies. One should as well examine the
orbitals. This is also valid for DFT: Although the Kohn-Sham orbitals
lack, in a strict sense, any physical interpretation, experience shows
that they are *very close* to wavefunction-based single particle
orbitals (*cf.* chapter 5.3). Thus, the DFT Kohn-Sham orbitals provide a
useful interpretative tool to visualise changes in the electronic
structure between different species (or in a chemical transformation),
but one should bear in mind that they have to be interpreted with care.





3.  Take a screenshot of the MP2 orbital and include it in your report.
    Then, open a DFT outputfile of your choice in Molden and repeat the
    orbital visualisation. Take a screenshot of the DFT HOMO as well.
    How do the orbitals differ from each other? How does the symmetry of
    the HOMO relate to the predicted structure?

4.  Explain the difference between static and dynamic correlation.
    Relate this to the different results you obtained for the nitrate
    radical. What kind of correlation do HF, MP2 and DFT take into
    account?

5.  If you needed a highly accurate structure and energy for
    NO$_3\cdot$, which method would you use?
