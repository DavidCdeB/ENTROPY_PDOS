#
import matplotlib.pyplot as plt
import sys
import numpy as np
import os
import glob
import fileinput

folder_111 = './1_times_landau_supercell'
folder_222 = './2_times_landau_supercell'
folder_333 = './3_times_landau_supercell'
folder_444 = './4_times_landau_supercell'

#vols_all = ["62.9226515"]
vols_all = ["62.923"]

vols = vols_all
#files_222_0_3 = files_222

nu_127_SCEL_111  = np.loadtxt('./1_times_landau_supercell/All_freq.dat', skiprows = 1).T  
nu_127_SCEL_222  = np.loadtxt('./2_times_landau_supercell/All_freq.dat', skiprows = 1).T  
nu_127_SCEL_333  = np.loadtxt('./3_times_landau_supercell/All_freq.dat', skiprows = 1).T  
nu_127_SCEL_444  = np.loadtxt('./4_times_landau_supercell/All_freq.dat', skiprows = 1).T


################### CONSTANTS   ###############
global KB, h, c, T

# KB = boltmann cte, KB = 1.38064852(79)x10-23 J/K
KB = 1.38064852E-23

# h = plank constant, h = 6.626070040(81)x10-34 J s
h = 6.626070040E-34

# T = temperature, T = 298.15 K
T = 298.15

# c = speed of light, c = 2.99792458E8 m/s
c = 2.99792458E+8

def S(nu):
 S = -KB * np.log(1 - np.exp(-h * nu * 1E+2 * c  / (KB*T)))     + ( (h/T) * ( nu * 1E+2 * c * ( (np.exp(h *  nu  * 1E+2 * c  / (KB*T)) - 1)**(-1) )    )  )

 # Conversion: S above this line is in mHartree/K:
 return S  *((1/4.3597482)*1E+18 * 1E+3)

S_127_SCEL_111 = S(nu_127_SCEL_111)
S_127_SCEL_222 = S(nu_127_SCEL_222)
S_127_SCEL_333 = S(nu_127_SCEL_333)
S_127_SCEL_444 = S(nu_127_SCEL_444)

for i in xrange(1,len(S_127_SCEL_111)):
   S_127_SCEL_111[i] = S_127_SCEL_111[i] + S_127_SCEL_111[i-1]

for i in xrange(1,len(S_127_SCEL_222)):
    S_127_SCEL_222[i] = S_127_SCEL_222[i] + S_127_SCEL_222[i-1]

for i in xrange(1,len(S_127_SCEL_333)):
    S_127_SCEL_333[i] = S_127_SCEL_333[i] + S_127_SCEL_333[i-1]

for i in xrange(1,len(S_127_SCEL_444)):
    S_127_SCEL_444[i] = S_127_SCEL_444[i] + S_127_SCEL_444[i-1]

#Now, the normalization of the entropy to the number of K points = 64

S_127_SCEL_111 = S_127_SCEL_111 / 2.0
S_127_SCEL_222 = S_127_SCEL_222 / 16.0
S_127_SCEL_333 = S_127_SCEL_333 / 54.0
S_127_SCEL_444 = S_127_SCEL_444 / 128.0

output_array_127_SCEL_111 = np.vstack((nu_127_SCEL_111, S_127_SCEL_111)).T
output_array_127_SCEL_222 = np.vstack((nu_127_SCEL_222, S_127_SCEL_222)).T
output_array_127_SCEL_333 = np.vstack((nu_127_SCEL_333, S_127_SCEL_333)).T
output_array_127_SCEL_444 = np.vstack((nu_127_SCEL_444, S_127_SCEL_444)).T

np.savetxt('./1_times_landau_supercell/nu_S.dat', output_array_127_SCEL_111, header="nu\tS", fmt="%0.12g")
np.savetxt('./2_times_landau_supercell/nu_S.dat', output_array_127_SCEL_222, header="nu\tS", fmt="%0.12g")
np.savetxt('./3_times_landau_supercell/nu_S.dat', output_array_127_SCEL_333, header="nu\tS", fmt="%0.12g")
np.savetxt('./4_times_landau_supercell/nu_S.dat', output_array_127_SCEL_444, header="nu\tS", fmt="%0.12g")

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
plt.title('Calcite I, PBE-D3, pob-TVPZ, V$_{eq}$ = ' + vols[0] + ' $\AA^{3}$/ F.U.', fontsize=12)  

template_111 = os.path.join(folder_111, '*.PHONDOS')
template_222 = os.path.join(folder_222, '*.PHONDOS')
template_333 = os.path.join(folder_333, '*.PHONDOS')
template_444 = os.path.join(folder_444, '*.PHONDOS')

x_111, y_111 = np.loadtxt(fileinput.input(glob.glob(template_111)), skiprows = 4).T
x_222, y_222 = np.loadtxt(fileinput.input(glob.glob(template_222)), skiprows = 4).T
x_333, y_333 = np.loadtxt(fileinput.input(glob.glob(template_333)), skiprows = 4).T
x_444, y_444 = np.loadtxt(fileinput.input(glob.glob(template_444)), skiprows = 4).T

nu_SCEL_111, S_SCEL_111 = np.loadtxt(os.path.join(folder_111, 'nu_S.dat'), skiprows = 1).T
nu_SCEL_222, S_SCEL_222 = np.loadtxt(os.path.join(folder_222, 'nu_S.dat'), skiprows = 1).T
nu_SCEL_333, S_SCEL_333 = np.loadtxt(os.path.join(folder_333, 'nu_S.dat'), skiprows = 1).T
nu_SCEL_444, S_SCEL_444 = np.loadtxt(os.path.join(folder_444, 'nu_S.dat'), skiprows = 1).T

lns1 = ax.plot(x_111, y_111, color='salmon', label='1xLandau') 
lns2 = ax.plot(x_222, y_222, color='red', label='2xLandau') 
lns3 = ax.plot(x_333, y_333, color='maroon', label='3xLandau') 
lns4 = ax.plot(x_444, y_444, color='black', label='4xLandau') 

ax2 = ax.twinx()
lns5 = ax2.plot(nu_SCEL_111, S_SCEL_111, 'salmon', linestyle='--', label='Entropy')
lns6 = ax2.plot(nu_SCEL_222, S_SCEL_222, 'red', linestyle='--', label='Entropy')
lns7 = ax2.plot(nu_SCEL_333, S_SCEL_333, 'maroon', linestyle='--', label='Entropy')
lns8 = ax2.plot(nu_SCEL_444, S_SCEL_444, 'black', linestyle='--', label='Entropy')

ax.grid()

x_value = 0.6    #Offset by eye
y_value = .45
axbox = ax.get_position()

lns = lns1+lns2+lns3+lns4
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc = (axbox.x0 + x_value, axbox.y0 + y_value))

ax.set_ylabel('PDOS (states/cm$^{-1}$/cell)')
ax2.set_ylabel('Entropy (mHartree/(cell$\cdot$K))\nat T = 298.15 K')
ax.tick_params(labelbottom='on') 


ax.set_xlabel('Energy (cm$^{-1}$)')

fig.savefig("PDOS_0_and_8_plus_cum_entropy_T_298K_plus_4x.pdf", bbox_inches='tight', pad_inches=0.3)#, tight_layout() )#, bbox_inches=bbox)


plt.show()

