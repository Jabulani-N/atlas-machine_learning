#!/usr/bin/env python3
"""task 11"""


import sklearn.mixture


def gmm(X, k):
    """calculate gmm of dataset"""
    gaussian_mix = sklearn.mixture.GaussianMixture
    mix = gaussian_mix(n_components=k)
    mix.fit(X)
    pi = mix.weights_
    m = mix.means_
    S = mix.covariances_
    clss = mix.predict(X)
    kmin = 1
    kmax = k
    bic = []
    for i in range(kmin, kmax + 1):
        mix = gaussian_mix(n_components=i)
        mix.fit(X)
        bic.append(mix.bic(X))
    bic = np.array(bic)

    return pi, m, S, clss, bic
