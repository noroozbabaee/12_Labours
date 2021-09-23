# To reproduce the data needed for Figure 2A in associated original paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:
#
#  In [1]: cd path/to/folder_this_file_is_in
#  In [2]: run Imtiaz_IP3_sim.py

import opencor as oc
import numpy as np
prefilename= 'Fig1_A'
simfile = 'IP3_Imtiaz_2002.sedml'
simulation = oc.open_simulation(simfile)
data = simulation.data()
# Reset states and parameters
simulation.reset(True)
# Set constant parameter values
time_s = 10
start = 0
end = 10
pointInterval = 0.01
data.set_starting_point(start)
data.set_ending_point(end)
data.set_point_interval(pointInterval)
simulation.run()
# Access simulation results
results = simulation.results()
# Grab a selected algebraic variable results
varName = np.array([ "time", "Vm", "z","ip3","y"])
vars = np.reshape(varName, (1, 5))
rows = time_s * 100 + 1
print(rows)
r = np.zeros((rows, len(varName)))

r[:,0] = results.voi().values()
r[:,1] = results.states()['vm/vm'].values()
r[:,2] = results.states()['ca/z'].values()
r[:,3] = results.states()['p_ip3/p_ip3'].values()
r[:,4] = results.states()['ca/y'].values()
filename = '%s.csv' % prefilename
np.savetxt(filename, vars, fmt='%s', delimiter=",")
with open(filename, "ab") as f:
    np.savetxt(f, r, delimiter=",")
f.close

# Grab a selected algebraic variable results
varName_rate = np.array([ "time", "Vm_rate", "z_rate", "ip3_rate", "y_rate"])
vars = np.reshape(varName_rate, (1, 5))
rows = time_s * 100 + 1
print(rows)
r = np.zeros((rows, len(varName_rate)))

r[:,0] = results.voi().values()
r[:,1] = results.rates()['vm/vm/prime'].values()
r[:,2] = results.rates()['ca/z/prime'].values()
r[:,3] = results.rates()['p_ip3/p_ip3/prime'].values()
r[:,4] = results.rates()['ca/y/prime'].values()
# clear the results except the last run
simulation.clear_results()
# Save the simulation result of the last run
filename = '%s_rate.csv' % prefilename
np.savetxt(filename, vars, fmt='%s', delimiter=",")
with open(filename, "ab") as f:
    np.savetxt(f, r, delimiter=",")
f.close


