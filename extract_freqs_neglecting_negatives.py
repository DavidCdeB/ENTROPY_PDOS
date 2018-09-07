# 
# QHA -son- program: This program is going to be called by the QHA -Master- program
# David Carrasco de Busturia, 13 October 2017 
# Please read the documentation and istructions on: https://github.com/DavidCdeB/QHA
# This program is under the GNU General Public License v3.0. 
# davidcarrascobustur@gmail.com
# d.carrasco-de-busturia@imperial.ac.uk

import re
import os
import glob
from itertools import islice
import numpy as np
import subprocess
import itertools
import sys
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# Extracting the number of k-points ( name of variable = "N_k" ):
path='./'
template = os.path.join(path, '*.out')

ALL_FREQ = []

for fname in glob.glob(template):
  print fname
  f = open(fname, 'r')

  for line in f:

        if 'MODES         EIGV          FREQUENCIES     IRREP' in line:

            f.next()

            while True:
               target = f.next()
               aux = target.split()
               if not aux:
                  break

               first_No = aux[0]
               second_No = aux[1]
               freq = aux[3]
               
               first_No = first_No.translate(None, '-')  # remove the '-'


               factor_freq = abs(int(second_No) - int(first_No)) + 1

               freqs = [freq] * factor_freq

               ALL_FREQ.append(freqs)


ALL_FREQ = [item for sublist in ALL_FREQ for item in sublist]

thing = '0.0000'
while thing in ALL_FREQ: ALL_FREQ.remove(thing)

ALL_FREQ = sorted(ALL_FREQ, key=float) 
ALL_FREQ = [float(i) for i in ALL_FREQ]
num_list = [item for item in ALL_FREQ if item >= 0]
output_array_2 = num_list

output_array_2 = np.vstack((ALL_FREQ))#.T
output_array_2 = np.vstack((num_list))#.T

np.savetxt('All_freq.dat', output_array_2, header="FREQS (CM^-1)", fmt="%s")
sys.exit()
