# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as pl

t, x, y, z, vx, vy, vz, d, d2 = np.loadtxt(sys.argv[1]+".txt").transpose()
#t2, x2, y2, z2, vx2, vy2, vz2, ekin2, epot2, d3, d23 = np.loadtxt("NoImpuls/"+sys.argv[1]).transpose()

pl.title("Diffusion")
pl.plot(t, d2, label="kein Gesamtimpuls")
#pl.plot(t2, d23, label="mit Gesamtimpuls")
pl.loglog()
pl.xlabel("Zeit t [a.u.]")
pl.ylabel(ur"Diffusion $\left< \left[\vec{r}(t)-\vec{r}(0)\right]^2 \right>$")
pl.legend(loc="lower right")
pl.axhline(42.0*42.0)
pl.grid()
#pl.savefig("DiffL14.png", dpi=300)
pl.show()