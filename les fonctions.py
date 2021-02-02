#!/usr/bin/python
import math as m
import sympy as sym
import scipy.integrate
import numpy as n

a=6378137
b=6356752.3142


def get_applatissment(a, b):
    return 1 - b / a


def get_1er_excentricite(a, b):
    return 1 - (b / a)**2


def get_2eme_excentricite(a, b):
    return (a / b)**2 - 1


def get_excentricite_angulaire(a, b):
    return m.acos(b / a)


def get_courbure_pole(a, b):
    return (a**2) / b

def convert_geo2cart(Phi, L, h):
    # (lat, lon) in WSG-84 degrees
    # h in meters
    lamb = m.radians(Phi)
    phi = m.radians(L)
    s = m.sin(lamb)
    N = a / m.sqrt(1 - get_1er_excentricite(a, b) * s * s)

    sin_lambda = m.sin(lamb)
    cos_lambda = m.cos(lamb)
    sin_phi = m.sin(phi)
    cos_phi = m.cos(phi)

    x = (h + N) * cos_lambda * cos_phi
    y = (h + N) * cos_lambda * sin_phi
    z = (h + (1 - get_1er_excentricite(a, b)) * N) * sin_lambda

    return x, y, z


def convert_cart2geo(x, y, z):
    r = m.sqrt(x**2 + y**2 + z**2)
    u = m.atan((z / m.sqrt(x**2 + y**2) * ((1 - get_applatissment(a, b)) + (a * get_1er_excentricite(a, b)) / r))   )

    L = m.atan(y/x)
    phi = m.atan( (z*(1 - get_applatissment(a, b)) + (get_1er_excentricite(a, b)*a*m.sin(u)**2)) / ((1 - get_applatissment(a, b)) * (m.sqrt(x**2 + y**2) - get_1er_excentricite(a, b) * a * m.cos(u)**3)) )
    h = m.sqrt(x**2 + y**2) * m.cos(phi) + z * m.sin(phi) - a * m.sqrt(1 - get_1er_excentricite(a, b) * m.sin(phi)**2)

    return m.degrees(phi), m.degrees(L), h


def get_3_altitudes(x):
    beta = m.acos(x / a)
    psi = m.atan((b/a * m.tan(beta)))
    phi = m.atan(a/b * m.tan(beta))

    return beta, phi, psi


def get_rayon_courbure(Phi):
    phi = m.radians(Phi)
    w = m.sqrt(1 - get_1er_excentricite(a, b) * m.sin(phi)**2)

    return (a * (1 - get_1er_excentricite(a, b)) / w**3)


def get_rayon_1ere_verticale(Psi):
    psi = m.radians(Psi)
    phi = m.atan(a**2 / b**2 * m.tan(psi))
    w = m.sqrt(1 - get_1er_excentricite(a, b) * m.sin(phi)**2)

    return a / w


def get_courbure_azimut(Alpha, Psi):
    psi = m.radians(Psi)
    phi = m.atan(a**2 / b**2 * m.tan(psi))

    alpha = m.radians(Alpha)

    M = get_rayon_courbure(phi)
    N = get_rayon_1ere_verticale(Psi)

    return (M * m.sin(alpha)**2 + N * m.cos(alpha)**2) / M * N


def get_longeur_meridien(Phi):
    f = lambda x:(1 - get_1er_excentricite(a, b) * n.sin(x)**2)**(-3/2)
    return b * scipy.integrate.quad(f, 0, m.radians(Phi))[0] / 1000


def get_longueur_parallele(Phi, delta_lambda):
    phi = m.radians(Phi)
    N = a / (1 - get_1er_excentricite(a, b) * m.sin(phi)**2)

    return N * m.cos(phi) * delta_lambda


def get_surface_partie_terre(L1, L2, Phi1, Phi2):
    l1 = m.radians(L1)
    l2 = m.radians(L2)
    phi1 = m.radians(Phi1)
    phi2 = m.radians(Phi2)

    f = lambda x:n.cos(x) * (1 - get_1er_excentricite(a, b) * n.sin(x)**2)**-2
    integral = scipy.integrate.quad(f, phi1, phi2)
    return b**2 * (l2 - l1) * integral[0]
    


print(get_surface_partie_terre(0, 90, 0, 90))

#beta = (1 - get_applatissment(a, b)) * m.tan(m.radians(1))
