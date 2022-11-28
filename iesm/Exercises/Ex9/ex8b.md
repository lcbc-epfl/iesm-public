# Finding Transition States and Barrier Heights 2

## Recording a Potential Energy Profile: The Intrinsic Reaction Coordinate (IRC)


A transition state search merely guarantees that one reaches a
first-order saddle point on the PES; there is, however, no guarantee
that it is really linked to the reactant and product. (For instance,
there may be further transition states lying in between.) Although the
visualisation of the imaginary vibrational mode may give some hint as to
whether one has found a reasonable saddle point, this information is not
sufficient to guarantee a connection to the reactant and product well.
Following the negative Hessian eigenvalues from the transition state to
the next local minimum, on the other hand, will immediately reveal
whether such a connection exists. This Hessian-following in
mass-weighted coordinates is referred to as a search along the
*Intrinsic Reaction Coordinate* (IRC). This search will create a
potential energy profile for the reaction, as well as a trajectory that
visualises the lowest energy path from reactant to TS to product. In
this last exercise session, you will verify whether the transition state
you computed in the last exercise is the proper state that connects your
starting material to the product, and you will build the reaction
profile and visualise the trajectory in VMD.

### Finding Products and Reactants: IRC {#finding-products-and-reactants-irc .unnumbered}

Copy the Checkpoint file you saved from the transition state frequency
calculation (section 8.3) to your working directory. Create the
following input:

    %NProcShared=2
    %Mem=1GB
    %OldChk=TSFreq
    %Chk=For
    #P B3PW91/6-31+G* IRC=(RCFC,Forward,Stepsize=10,Maxpoint=100,ReCorrect=Test)
       Guess=Read Geom=Checkpoint 

    IRC Forward

    -1 1

Note that the route section `#` can be distributed over more than one
line. `IRC` instructs Gaussian to perform an IRC Search, `Stepsize`,
`Maxpoint` and `ReCorrect` are variables that are often specific to a
reaction and that, in the worst case, have to be found by trial and
error. For this run, you are provided with working variables. Again, we
use both the `Guess` wavefunction, the Hessian `RCFC` and the `Geom`
from the Checkpoint file to save computational time. `Forward` specifies
the direction of the search. However, `Forward` does not imply that the
search will proceed to the product, as the choice of the direction is
based on the local curvature at the TS. Therefore, `Forward` may
actually lead to the reactants, and the opposite keyword `Reverse` may
lead to the product instead. Create a second input for the `Reverse` IRC
search:

    %NProcShared=2
    %Mem=1GB
    %OldChk=TSFreq
    %Chk=Rev
    #P B3PW91/6-31+G* IRC=(RCFC,Reverse,Stepsize=10,Maxpoint=100,ReCorrect=Test)
       Guess=Read Geom=Checkpoint 

    IRC Reverse

    -1 1

Submit the jobs to Gaussian *one at a time*. (If you work in groups of
two, split the tasks to save time.) Once the runs finish, verify whether
they found a minimum on the PES
(`PES minimum detected on this side of the pathway`). If this is the
case, you may extract the coordinates using the script
`g09_scan_trajectory.sh`:

    bash g09_scan_trajectory.sh -i filename -n number_of_atoms -o output.xyz

Make sure that the `g09_scan_trajectory.sh` output has the extension
`.xyz`. Do this for both the forward and reverse run, and open the xyz
files you obtained in VMD (first one, then the other). You will see that
both trajectories start from the transition state. In order to have a
proper visualisation, you need to reverse one of them. Identify the
trajectory that leads to the reactants (is it `Forward` or `Reverse`?)
and note the number of frames this trajectory contains. This trajectory
is the one that you need to reorder, such that the first frame is given
by the reactants, rather than the TS. Use the script
`reverse_trajectory.sh`:

    bash reverse_trajectory.sh -i filename -n number_of_atoms \
    -f number_of_frames -o output.xyz

Then, you can concatenate the reversed reactant trajectory and the
trajectory that leads to the product to one single trajectory:

    cat reversed_reactant_trajectory product_trajectory > reaction.xyz

Open the concatenated trajectory in VMD. As VMD is by default not able
to redraw bonds during a trajectory, you will have to fiddle with the
representation. Go to `Graphics` in the *VMD Main*, then to
`Representations…` and change the `Drawing method` to `CPK`. Set the
`Bond Radius` to 0.0. Click on `Create Rep` and, for the new
representation, change the `Drawing method` to `Dynamic bonds`. Decrease
the `Bond Radius` to 0.1 and increase the `Distance Cutoff` to 2.0. If
you go through the trajectory now, you will see how bonds are being
broken and formed as the reaction proceeds.\

1.  How do the C-Cl and the two relevant C-O bond lengths change during
    the trajectory? Does the C-C bond in the ring contract as the
    epoxide is formed? Show a graph depicting the evolution of these
    parameters as the reaction progresses. (Hit `2` to select bond
    lengths, and use `Graphics` (*VMD Main*), `Labels` and `Graph`
    (*Labels* Menu) to visualise the changes, just as you did in the PES
    scan of butane.)

2.  What is happening to the methyl group as the reaction proceeds? Find
    a suitable parameter (angle, dihedral) to describe and characterise
    possible changes you observe. (Hit `3` to select angles, or `4` for
    dihedrals.)

3.  Is the stereochemistry at the carbon at which the reaction takes
    place retained?

All the information on the reaction energy profile can be found at the
end of the Gaussian output files after
`Summary of reaction path following`. You can extract this information
using grep:

    grep -A number_of_steps+3 "Summary of reaction path" outputfile > energy_file

Do this for both IRC outputs, writing to different files. Make sure that
you specify a number that exceeds the number of steps by 3. You can then
use a plotting program, LibreOfficeCalc or Microsoft Excel to visualise
this data (both LibreOfficeCalc and Excel have the ability to import
plain text files). We recommend a quick approach. From the command line,
invoke the plotting program gnuplot:

    gnuplot

In the gnuplot interface, type the following:

    set xlabel 'Reaction Coordinate'
    set ylabel 'Energy [kcal/mol]'
    plot './forward_energies' using 3:($2*627.5095) with lines title 'forward',\
    './reverse_energies' using 3:($2*627.5095) with lines title 'reverse'

After every line, hit enter. In the `plot` command, the first number
after `using` specifies the x axis, which is the third column in your
energy file (the reaction coordinate). The second number specifies the y
axis, which corresponds to the second column in the energy file (the
energy of the system). The multiplication by a factor of 627.5095
converts the y-values to kcal mol$^{-1}$. If the resulting graph shows a
reaction that proceeds from right to left, rather than from left to
right as requested by convention, you may replace the x-axis
specification `3` by `-$3`, which will create a plot that takes the
negative of the reaction coordinate as its x axis.

4.  Take a screenshot of the graph of the potential energy profile you
    recorded. Make sure that the left half corresponds to the reactants,
    and that the product state can be found to the right.

5.  Why is the barrier for the epoxide formation so low? Will this be
    the overall barrier for the reaction as depicted in section 8.1?
