# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as pl
import scipy.optimize as optimize

#loading parameters
seed, N, space, axialRatio, boxWidth, boxHeight, particleSpeed, runs, gui = np.loadtxt("data/"+sys.argv[1]+"_conf.txt").transpose()

r = np.loadtxt("data/"+sys.argv[1]+"_correlation.txt").transpose()
[h,x] = np.histogram(r,300, range=(0,r.max()))
g = h*boxWidth*boxHeight/(np.pi**x[1]*x[1]*N*N*(np.arange(len(h))+1-0.5))
pl.plot(x[1:], g, label = ur"$\Lambda = %1.1f$" % (boxWidth/np.sqrt(N)))
pl.grid()
pl.xlim(0,20)
pl.xlabel("Abstand r")
pl.ylabel("Zwei-Punkt-Korrelationsfunktion g")
pl.title("Gitterkonstante = 1.4")
#pl.show()