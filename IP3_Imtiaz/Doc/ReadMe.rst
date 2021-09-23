Original Paper
==============

:Original publication:  "A Theoretical Model of Slow Wave Regulation Using Voltage-Dependent
Synthesis of Inositol 1,4,5-Trisphosphate" Biophysical Journal Volume 83 October 2002 1877–1890.

:DOI: https://doi.org/10.1016/S0006-3495(02)73952-0

Model status
=============

The current CellML model implementation runs in OpenCOR_.
The CellML model parameters and equations must be updated regarding each specific model variation to reproduce the related simulations;
The required information is not available in the original article;
we cannot reproduce the results in the current work due to insufficient information.

Model Summary
==============
Slow waves are rhythmic electrical depolarizations that
initiate and control the mechanical activity of many smooth
muscles. The mechanism responsible for generating slow waves involves IP3-induced calcium release and calcium-induced calcium release from IP3-operated intracellular calcium stores. The resultant calcium increases in the subplasmalemmal space then activate calcium-sensitive inward currents across the plasmalemma that result in slow-wave
depolarizations which are according to the previous studies.

According to :ref:`Original Paper`, IP3 oscillations are unnecessary
for calcium oscillations, as IP3 oscillations can occur in many cell types. Imtiaz-2002 is introducing a new feedback mechanism based on membrane potential, which then modulates IP3 synthesis. In this paper, the aim is to study the role of membrane
potential feedback on IP3 synthesis and its role in regulating calcium release and slow waves.

The system is simplified by considering a single
isopotential cell with a single IP3 receptor-operated intracellular
calcium pool. Ryanodine receptor is ignored in the model. It is
important to note that in this model voltage-dependent channels are considered to be blocked.


Model Equations
===============
The model is implemented using a Hodgkin-Huxley type formulation. The cell membrane lipid bilayer is represented as a capacitance (Cm),
and the ion channels in the membrane are represented as conductance. The change in the transmembrane potential (Vm) over time depends on
is the sum of the individual ion currents through each class of ion channel in the cell current:

:math:` \frac{dVm}{dt} = - \frac{I_{tot}}{C_{m}}`.


Model Experiments
=================

Two sets of experiments were designed :

The first set of experiments with the maintained current
injection, investigated the role of membrane potential by holding the
resting membrane potential and :math:`\beta`  at various predetermined
levels.

The second set of experiments investigated the model responses
to injected current pulses. These experiments were simulated
using the model cell by injecting current pulses to
induce step changes in membrane potential.
However, there is no clear information about the protocol they used to inject the current into the cell in both experiments.

Model Issues
===================
1. There is an issue of unit consistency.

In Eq. 3, :math:`V_{in},  V_{1}` and :math:`V_{0}` have a unit of :math:`\mu M /min`, while  P has a unit of :math:`\mu M `.
As a result, one can see the left- and right-hand sides of Eq. 3 has inconsistent units.

:math:` V_{in} = V_{0} + V_{1}* P`.

In Eq. 7, the left-hand side is multiplied by the scale factor of :math:` 60* 0.001` to create the unit consistency.

In Eq. 9, on the left, the term :math:`\beta` that indicates the external stimuli has a unit of :math:`\mu M ` while on the right-hand side, the term :math:`dP /dt`
which indicates IP3 concentration in the cytosol has a unit of  :math:`\mu M /min`.

:math:`dP /dt = \beta - \epsilon *  P  - V_{m4}(P) + P (V)`.



2. In the case of model variation, there is no clear information about the protocol
they used to inject the current into the cell.


3. Applying the default parameters and corrections in regard to the unit consistencies, the model failed to converge. After some sensitivity analysis,
membrane capacitance is considered to switch from 0.0017 F to 0.0017 mF.

Model Validations
===================
Applying the default parameters in the original paper plus few modifications (see :ref:`Model Issues`), the following results were observed:
In the top, on can see the time-series of intracellular calcium concentration; while the second and the third diagrams represent the time-series of IP3 concentrations and membrane voltage.
In Figure 2A (Imtiaz-2002), one can see that  IP3, intracellular Ca (Z) concentrations, and voltage membrane are all plotted in the same diagram
to show that membrane potential (V) oscillations are in phase with intracellular calcium.
There is not enough information if these graphs present the actual state variables or their derivatives.


.. image:: Figure_1.png
    :width: 70%
    :alt: State_variable_derivatives.


Here, one can see all the state variables of the model and their behavior for the first 10 minutes. In the second row, one can see the derivatives of those state variables, which are presented in the first row.

.. image:: Figure_2.png
   :width: 110%
   :alt: All_state_variables_derivative.

Model Simulation
================
To run the simulations,
execute 'Imtiaz_IP3_sim.py' in the Python console in OpenCOR_. This can be done
with the following commands at the prompt in the OpenCOR_ Python console:

 In [1]: cd path/to/folder_this_file_is_in

 In [2]: run Imtiaz_IP3_sim.py
