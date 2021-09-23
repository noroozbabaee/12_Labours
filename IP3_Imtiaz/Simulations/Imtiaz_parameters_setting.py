import opencor as oc
sim = oc.open_simulation("IP3_Imtiaz_2002.sedml")
data = sim.data()
sim.run()

# Access simulation results
results = sim.results()

states = data.states()
newStates = {k:states[k] for k in states}
constants = data.constants()
newConstants = {k:constants[k] for k in constants}
variables = {'states': newStates, 'constants': newConstants}
import json
with open("IP3_default.json", 'w') as fp:
    json.dump(variables, fp)