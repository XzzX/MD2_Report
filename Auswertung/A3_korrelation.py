# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as pl
import scipy.optimize as optimize

hist = 300

pl.subplot(411)

#loading parameters
seed, N, space, axialRatio, boxWidth, boxHeight, particleSpeed, runs, gui = np.loadtxt("data/A3L21_conf.txt").transpose()
r = np.loadtxt("data/A3L21_correlation.txt").transpose()
[h,x] = np.histogram(r,hist, range=(0,r.max()))
g = h*boxWidth*boxHeight/(np.pi**x[1]*x[1]*N*N*(np.arange(len(h))+1-0.5))
pl.plot(x[1:], g, label = ur"$\Lambda = %1.1f$" % (boxWidth/np.sqrt(N)))
pl.grid()
pl.xlim(0,20)
pl.legend()

pl.subplot(412)

#loading parameters
seed, N, space, axialRatio, boxWidth, boxHeight, particleSpeed, runs, gui = np.loadtxt("data/A3L22_conf.txt").transpose()
r = np.loadtxt("data/A3L22_correlation.txt").transpose()
[h,x] = np.histogram(r,hist, range=(0,r.max()))
g = h*boxWidth*boxHeight/(np.pi**x[1]*x[1]*N*N*(np.arange(len(h))+1-0.5))
pl.plot(x[1:], g, label = ur"$\Lambda = %1.1f$" % (boxWidth/np.sqrt(N)))
pl.grid()
pl.xlim(0,20)
pl.legend()

pl.subplot(413)

#loading parameters
seed, N, space, axialRatio, boxWidth, boxHeight, particleSpeed, runs, gui = np.loadtxt("data/A3L23_conf.txt").transpose()
r = np.loadtxt("data/A3L23_correlation.txt").transpose()
[h,x] = np.histogram(r,hist, range=(0,r.max()))
g = h*boxWidth*boxHeight/(np.pi**x[1]*x[1]*N*N*(np.arange(len(h))+1-0.5))
pl.plot(x[1:], g, label = ur"$\Lambda = %1.1f$" % (boxWidth/np.sqrt(N)))
pl.grid()
pl.xlim(0,20)
pl.legend()
pl.ylabel("Zwei-Punkt-Korrelationsfunktion g")

pl.subplot(414)

#loading parameters
seed, N, space, axialRatio, boxWidth, boxHeight, particleSpeed, runs, gui = np.loadtxt("data/A3L24_conf.txt").transpose()
r = np.loadtxt("data/A3L24_correlation.txt").transpose()
[h,x] = np.histogram(r,hist, range=(0,r.max()))
g = h*boxWidth*boxHeight/(np.pi**x[1]*x[1]*N*N*(np.arange(len(h))+1-0.5))
pl.plot(x[1:], g, label = ur"$\Lambda = %1.1f$" % (boxWidth/np.sqrt(N)))
pl.grid()
pl.xlim(0,20)
pl.legend()


pl.xlabel("Abstand r")

pl.show()