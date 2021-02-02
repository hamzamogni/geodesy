#!/usr/bin/python
import math as m
import sympy as sym
import scipy.integrate
import numpy as n

a_wgs = 6378137
b_wgs = 6356752.3142


def get_ellipsoid_parameters(a=6378137, b=6356752.3142):
    return {
        "applatissement": 1 - b / a,
        "excentricite_1": 1 - (b / a) ** 2,
        "excentricite_2": (a / b) ** 2 - 1,
        "excentricite_ang": m.acos(b / a),
        "courbure_pole": a ** 2 / b,

    }


# def get_applatissment(a, b):
#     return 1 - b / a
#
#
# def get_1er_excentricite(a, b):
#     return 1 - (b / a) ** 2
#
#
# def get_2eme_excentricite(a, b):
#     return (a / b) ** 2 - 1
#
#
# def get_excentricite_angulaire(a, b):
#     return m.acos(b / a)
#
#
# def get_courbure_pole(a, b):
#     return (a ** 2) / b


def convert_geo2cart(phi, lam, h):
    # (lat, lon) in WSG-84 degrees
    # h in meters
    phi_rad = m.radians(phi)
    lambda_rad = m.radians(lam)
    s = m.sin(lambda_rad)
    N = a_wgs / m.sqrt(1 - get_ellipsoid_parameters()["excentricite_1"] * s * s)

    sin_lambda = m.sin(lambda_rad)
    cos_lambda = m.cos(lambda_rad)
    sin_phi = m.sin(phi_rad)
    cos_phi = m.cos(phi_rad)

    x = (h + N) * cos_lambda * cos_phi
    y = (h + N) * cos_lambda * sin_phi
    z = (h + (1 - get_ellipsoid_parameters()["excentricite_1"]) * N) * sin_lambda

    return x, y, z


def convert_cart2geo(x, y, z):
    applatissement = get_ellipsoid_parameters()["applatissment"]
    excentricite_1 = get_ellipsoid_parameters()["excentricite_1"]
    r = m.sqrt(x ** 2 + y ** 2 + z ** 2)
    u = m.atan((z / m.sqrt(x ** 2 + y ** 2) * ((1 - applatissement) + (
            a_wgs * excentricite_1) / r)))

    L = m.atan(y / x)

    phi = m.atan((z * (1 - applatissement) + (
            excentricite_1 * a_wgs * m.sin(u) ** 2)) / (
                         (1 - applatissement) * (
                         m.sqrt(x ** 2 + y ** 2) - excentricite_1 * a_wgs * m.cos(
                     u) ** 3)))

    h = m.sqrt(x ** 2 + y ** 2) * m.cos(phi) + z * m.sin(phi) - a_wgs * m.sqrt(
        1 - excentricite_1 * m.sin(phi) ** 2)

    return m.degrees(phi), m.degrees(L), h


def get_3_altitudes(x):
    beta = m.acos(x / a_wgs)
    psi = m.atan((b_wgs / a_wgs * m.tan(beta)))
    phi = m.atan(a_wgs / b_wgs * m.tan(beta))

    return beta, phi, psi


def get_rayon_courbure(phi):
    excentricite_1 = get_ellipsoid_parameters()["excentricite_1"]

    phi_rad = m.radians(phi)
    w = m.sqrt(1 - excentricite_1 * m.sin(phi_rad) ** 2)

    return a_wgs * (1 - excentricite_1) / w ** 3


def get_rayon_1ere_verticale(Psi):
    excentricite_1 = get_ellipsoid_parameters()["excentricite_1"]

    psi = m.radians(Psi)
    phi = m.atan(a_wgs ** 2 / b_wgs ** 2 * m.tan(psi))
    w = m.sqrt(1 - excentricite_1 * m.sin(phi) ** 2)

    return a_wgs / w


def get_courbure_azimut(alpha, psi):
    psi_rad = m.radians(psi)
    phi = m.atan(a_wgs ** 2 / b_wgs ** 2 * m.tan(psi_rad))

    alpha_rad = m.radians(alpha)

    courbure = get_rayon_courbure(phi)
    rayon_1_verticale = get_rayon_1ere_verticale(psi)

    return (courbure * m.sin(alpha_rad) ** 2 + rayon_1_verticale * m.cos(alpha_rad) ** 2) / courbure * rayon_1_verticale


def get_longeur_meridien(Phi):
    excentricite_1 = get_ellipsoid_parameters()["excentricite_1"]

    f = lambda x: (1 - excentricite_1 * n.sin(x) ** 2) ** (-3 / 2)
    return b_wgs * scipy.integrate.quad(f, 0, m.radians(Phi))[0] / 1000


def get_longueur_parallele(phi, delta_lambda):
    excentricite_1 = get_ellipsoid_parameters()["excentricite_1"]
    phi_rad = m.radians(phi)
    N = a_wgs / (1 - excentricite_1 * m.sin(phi_rad) ** 2)

    return N * m.cos(phi_rad) * delta_lambda


def get_surface_partie_terre(l1, l2, phi1, phi2):
    excentricite_1 = get_ellipsoid_parameters()["excentricite_1"]

    l1_rad = m.radians(l1)
    l2_rad = m.radians(l2)
    phi1_rad = m.radians(phi1)
    phi2_rad = m.radians(phi2)

    integral = scipy.integrate.quad(
        lambda x: n.cos(x) * (1 - excentricite_1 * n.sin(x) ** 2) ** -2,
        phi1_rad,
        phi2_rad)
    return b_wgs ** 2 * (l2_rad - l1_rad) * integral[0]
