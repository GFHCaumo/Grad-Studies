#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 03:03:04 2025

@author: guilhermecaumo
"""

import numpy as np
import matplotlib.pyplot as plt

#Changed Some of the Functions
def r1(kT, A, K):
    return ((-np.exp(K/kT)*np.sinh(2*A/kT))/
            ((np.exp(K/kT)*np.cosh(2*A/kT))+1))
    
def r1r2(kT, A, K):
    return ((np.exp(2*K/kT)-1)/
            (((np.exp(K/kT)*np.cosh(2*A/kT))+1)**2))


kT_vals = np.linspace(1,100,int(1e5))

#Varying K for <r1>
plt.plot(kT_vals, r1(kT_vals, 1, 1), 'b', label = 'K = 1')
plt.plot(kT_vals, r1(kT_vals, 1, 10), 'r', label = 'K = 10')
plt.plot(kT_vals, r1(kT_vals, 1, 100), 'g', label = 'K = 100')

plt.xlabel('$k_{B}T$')
plt.ylabel('$<r1>$')
plt.title('$<r1>$ with respect to $k_{B}T$ for K = 1, 10, 100, A = 1')

plt.legend()
plt.savefig('r1k')
plt.show()

#Varying A for <r1>
plt.plot(kT_vals, r1(kT_vals, 1, 10), 'b', label = 'A = 1')
plt.plot(kT_vals, r1(kT_vals, 10, 10), 'r', label = 'A = 10')
plt.plot(kT_vals, r1(kT_vals, 50, 10), 'g', label = 'A = 50')

plt.xlabel('$k_{B}T$')
plt.ylabel('$<r1>$')
plt.title('$<r1>$ with respect to $k_{B}T$ for A = 1, 10, 50, K = 10')

plt.legend()
plt.savefig('r1A')
plt.show()

#Varying K for <deltar1deltar2>
plt.plot(kT_vals, r1r2(kT_vals, 1, 1), 'b', label = 'K = 1')
plt.plot(kT_vals, r1r2(kT_vals, 1, 10), 'r', label = 'K = 10')
plt.plot(kT_vals, r1r2(kT_vals, 1, 100), 'g', label = 'K = 100')

plt.xlabel('$k_{B}T$')
plt.ylabel('$< \delta r1 \delta r2 >$')
plt.title('$< \delta r1 \delta r2 >$ with respect to $k_{B}T$ for K = 1, 10, 100, A = 1')

plt.legend()
plt.savefig('r1r2k')
plt.show()

#Varying A for <deltar1deltar2>
plt.plot(kT_vals, r1r2(kT_vals, 1, 10), 'b', label = 'A = 1')
plt.plot(kT_vals, r1r2(kT_vals, 10, 10), 'r', label = 'A = 10')
plt.plot(kT_vals, r1r2(kT_vals, 50, 10), 'g', label = 'A = 50')

plt.xlabel('$k_{B}T$')
plt.ylabel('$< \delta r1 \delta r2 >$')
plt.title('$< \delta r1 \delta r2 >$ with respect to $k_{B}T$ for A = 1, 10, 50, K = 10')

plt.legend()
plt.savefig('r1r2A')
plt.show()