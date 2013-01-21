# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as pl
import scipy.optimize as optimize

L  = np.loadtxt("data/A4L5.txt").transpose()
pl.errorbar(L[0]*np.pi , L[1] , yerr = L[2] , label = ur"L = 5", linewidth=2, fmt="-")
L  = np.loadtxt("data/A4L10.txt").transpose()
pl.errorbar(L[0]*np.pi , L[1] , yerr = L[2] , label = ur"L = 10", linewidth=2, fmt="-")
L  = np.loadtxt("data/A4L15.txt").transpose()
pl.errorbar(L[0]*np.pi , L[1] , yerr = L[2] , label = ur"L = 15", linewidth=2, fmt="-")
L  = np.loadtxt("data/A4L20.txt").transpose()
pl.errorbar(L[0]*np.pi , L[1] , yerr = L[2] , label = ur"L = 20", linewidth=2, fmt="-")
#L  = np.loadtxt("data/A4L25.txt").transpose()
#pl.errorbar(L[0]*np.pi , L[1] , yerr = L[2] , label = ur"L = 25", linewidth=2, fmt="-")

pl.title(ur"Perkolation")
pl.xlabel(ur"Dichte $\rho$")
pl.ylabel(ur"Wahrscheinlichkeit für perkolierendes Cluster")
pl.legend(loc = "upper left")
pl.xlim(0,0.7*np.pi)
pl.grid()
pl.savefig("A4_perkolation.png", dpi=300)
pl.show()