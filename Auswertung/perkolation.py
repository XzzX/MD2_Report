# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as pl
import scipy.optimize as optimize

L4  = np.loadtxt("data/A4L4.txt").transpose()
L6  = np.loadtxt("data/A4L6.txt").transpose()
L8  = np.loadtxt("data/A4L8.txt").transpose()
L10 = np.loadtxt("data/A4L10.txt").transpose()
L12 = np.loadtxt("data/A4L12.txt").transpose()
L14 = np.loadtxt("data/A4L14.txt").transpose()
L16 = np.loadtxt("data/A4L16.txt").transpose()
L18 = np.loadtxt("data/A4L18.txt").transpose()
L20 = np.loadtxt("data/A4L20.txt").transpose()

pl.title(ur"Perkolation")
pl.errorbar(L4[0] , L4[1] , yerr = L4[2] , label = ur"L = 4", linewidth=2, fmt="x")
pl.errorbar(L6[0] , L6[1] , yerr = L6[2] , label = ur"L = 6", linewidth=2, fmt="x")
pl.errorbar(L8[0] , L8[1] , yerr = L8[2] , label = ur"L = 8", linewidth=2, fmt="x")
pl.errorbar(L10[0], L10[1], yerr = L10[2], label = ur"L = 10", linewidth=2, fmt="x")
pl.errorbar(L12[0], L12[1], yerr = L12[2], label = ur"L = 12", linewidth=2, fmt="x")
pl.errorbar(L14[0], L14[1], yerr = L14[2], label = ur"L = 14", linewidth=2, fmt="x")
pl.errorbar(L16[0], L16[1], yerr = L16[2], label = ur"L = 16", linewidth=2, fmt="x")
pl.errorbar(L18[0], L18[1], yerr = L18[2], label = ur"L = 18", linewidth=2, fmt="x")
pl.errorbar(L20[0], L20[1], yerr = L20[2], label = ur"L = 20", linewidth=2, fmt="x")
pl.xlabel(ur"Teilchenzahl")
pl.ylabel(ur"Wahrscheinlichkeit für perkolierendes Cluster")
pl.legend(loc = "upper left")
pl.grid()
pl.savefig("A4_perkolation.png", dpi=300)
pl.show()