import pandas as pd
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
prefilename ='Fig1_A'
filename = '%s.csv' % prefilename 
data = pd.read_csv(filename)

time = data[ 'time' ]
vm = data['Vm']
ca_y = data['y']
p_ip3 = data['ip3']
ca_z = data[ 'z' ]
# normalize the data (system variables)
vm_norm  = preprocessing.normalize(np.array(vm).reshape(1, -1))
ca_z_norm  = preprocessing.normalize(np.array(ca_z).reshape(1, -1))
p_ip3_norm  = preprocessing.normalize(np.array(p_ip3).reshape(1, -1))
ca_y_norm  = preprocessing.normalize(np.array(ca_y).reshape(1, -1))

filename2 = '%s_rate.csv' % prefilename
data = pd.read_csv(filename2)
time = data[ 'time' ]
vm_rate = data['Vm_rate']
ca_y_rate = data['y_rate']
ca_z_rate = data[ 'z_rate' ]
p_ip3_rate = data['ip3_rate']

# normalize the rate of data variables
vm_rate_norm = preprocessing.normalize(np.array(vm_rate).reshape(1, -1))
ca_y_rate_norm = preprocessing.normalize(np.array(ca_y_rate).reshape(1, -1))
ca_z_rate_norm = preprocessing.normalize(np.array(ca_z_rate).reshape(1, -1))
p_ip3_rate_norm = preprocessing.normalize(np.array(p_ip3_rate).reshape(1, -1))


fig, axs = plt.subplots(2,4, figsize=(13,13), facecolor='w', edgecolor='k')
fig.subplots_adjust(hspace = .3, wspace=.3)

axs[0, 0].plot( time, vm, 'k')
axs[0, 1].plot( time, ca_y, 'k')
axs [0, 2].plot(time, p_ip3, 'k')
axs[0, 3].plot( time, ca_z, 'k')

axs[1, 0].plot( time, vm_rate, 'k')
axs[1, 1].plot( time, ca_y_rate, 'k')
axs[1, 2 ].plot(time, p_ip3_rate, 'k')
axs[1, 3].plot( time, ca_z_rate, 'k')

# axs[2, 0].plot(vm_norm[0], 'k')
# axs[2, 1].plot(ca_y_norm[0], 'k')
# axs[2, 2].plot(p_ip3_norm[0], 'k')
# axs[2,3].plot(ca_z_norm[0], 'k')
# axs[3, 0].plot(vm_rate_norm[0], 'k')
# axs[3, 1].plot(ca_y_rate_norm[0], 'k')
# axs[3, 2].plot(p_ip3_rate_norm[0], 'k')
# axs[3, 3].plot(ca_z_rate_norm[0], 'k')

title = ['A Vm (mv)','B Ca_cytosol(micro-M)','C IP3(micro-M)','D Ca_IP3(micro-M)']
title_r = ['E d_Vm (mv/min)','F d_Ca_cytosol(micro-M/min)','G d_IP3(micro-M/min)','H d_Ca_IP3 (micro-M)/min']
for i in range(4):
    axs [0, i ].set_title(str(title [ i ]))
    axs [1, i].set_xlabel('Time (min)')
    axs [1, i  ].set_title(str(title_r [ i ]))
plt.show()

