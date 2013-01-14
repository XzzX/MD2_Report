# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as pl
import scipy.optimize as optimize

#loading parameters
seed, N, space, axialRatio, boxWidth, boxHeight, particleSpeed, runs, gui = np.loadtxt("data/"+sys.argv[1]+"_conf.txt").transpose()

t, d, d2 = np.loadtxt("data/"+sys.argv[1]+".txt").transpose()

pl.title("Diffusion")
pl.plot(t, d2, "x", label=ur"$\Lambda=%1.1f$" % (boxWidth/np.sqrt(N)))
#pl.plot(t2, d23, label="mit Gesamtimpuls")
pl.loglog()
pl.xlabel(ur"Zeit t")
pl.ylabel(ur"Diffusion $\left< \left[\vec{r}(t)-\vec{r}(0)\right]^2 \right>$")
#pl.legend(loc="lower right")
pl.axhline(boxHeight*boxHeight)
pl.grid()

#FitFunc = lambda a,b,x : a*x + b
#Residuals = lambda p, y, x: y - FitFunc(p[0], p[1], x)
#pGuess = [1.0, 1.0]
#kd,cov= optimize.leastsq(Residuals, pGuess, args=(np.log(d2[2:10]), np.log(t[2:10])))
#print kd

#pl.plot(t[2:10], np.exp(kd[1])*t[2:10]**kd[0], linewidth=2)

#kd,cov= optimize.leastsq(Residuals, pGuess, args=(np.log(d2[100:]), np.log(t[100:])))
#print kd

#pl.plot(t[100:], np.exp(kd[1])*t[100:]**kd[0], linewidth=2)

#pl.savefig("Diff08.png", dpi=300)

#pl.show()
