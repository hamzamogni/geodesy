#!/usr/bin/python
import math as m
import sympy as sym
import scipy.integrate
import numpy as n

a_wgs = 6378249.145
b_wgs = 6356515


def get_ellipsoid_parameters(a=a_wgs, b=b_wgs):
    return {
        "applatissement": 1 - b / a,
        "excentricite_1": 1 - (b / a) ** 2,
        "excentricite_2": (a / b) ** 2 - 1,
        "excentricite_ang": m.acos(b / a),
        "courbure_pole": a ** 2 / b,

    }


def convert_geo2cart(phi, lam, h):
    # (lat, lon) in WSG-84 degrees
    # h in meters
    phi_rad = m.radians(phi)
    lambda_rad = m.radians(lam)
    s = m.sin(phi_rad)
    N = a_wgs / m.sqrt(1 - get_ellipsoid_parameters()["excentricite_1"] * s ** 2)

    sin_lambda = m.sin(lambda_rad)
    cos_lambda = m.cos(lambda_rad)
    sin_phi = m.sin(phi_rad)
    cos_phi = m.cos(phi_rad)

    x = (h + N) * cos_phi * cos_lambda
    y = (h + N) * sin_lambda * cos_phi
    z = (h + (1 - get_ellipsoid_parameters()["excentricite_1"]) * N) * sin_phi

    return x, y, z


def convert_cart2geo(x, y, z):
    applatissement = get_ellipsoid_parameters()["applatissement"]
    excentricite_1 = get_ellipsoid_parameters()["excentricite_1"]

    r = m.sqrt(x ** 2 + y ** 2 + z ** 2)
    u = m.atan((z / m.sqrt(x ** 2 + y ** 2) * ((1 - applatissement) + (
            a_wgs * excentricite_1) / r)))

    L = m.atan(y / x)

    phi = m.atan((z * (1 - applatissement) + (
            excentricite_1 * a_wgs * m.sin(u) ** 3)) / (
                         (1 - applatissement) * (
                         m.sqrt(x ** 2 + y ** 2) - excentricite_1 * a_wgs * m.cos(
                     u) ** 3)))

    h = m.sqrt(x ** 2 + y ** 2) * m.cos(phi) + z * m.sin(phi) - a_wgs * m.sqrt(
        1 - excentricite_1 * m.sin(phi) ** 2)

    return m.degrees(phi), m.degrees(L), h


def get_3_altitudes(x):
    beta = m.acos(x / a_wgs)
    psi = m.atan((b_wgs / a_wgs) * m.tan(beta))
    phi = m.atan((a_wgs / b_wgs) * m.tan(beta))

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


def get_longeur_meridien(phi1, phi2):
    excentricite_1 = get_ellipsoid_parameters()["excentricite_1"]

    phi1_rad = m.radians(phi1)
    phi2_rad = m.radians(phi2)

    f = lambda x: (1 - excentricite_1 * n.sin(x) ** 2) ** (-3 / 2)
    zero_phi1 = b_wgs * scipy.integrate.quad(f, 0, m.radians(phi1_rad))[0] / 1000
    zero_phi2 = b_wgs * scipy.integrate.quad(f, 0, m.radians(phi2_rad))[0] / 1000

    return m.fabs(zero_phi1 - zero_phi2)


def get_longueur_parallele(phi, lambda1, lambda2):
    excentricite_1 = get_ellipsoid_parameters()["excentricite_1"]
    phi_rad = m.radians(phi)
    lambda1_rad = m.radians(lambda1)
    lambda2_rad = m.radians(lambda2)
    delta_lambda = m.fabs(lambda1_rad - lambda2_rad)

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
    return m.fabs(b_wgs ** 2 * (l2_rad - l1_rad) * integral[0])


def sigma(distance):
    return distance / (((2 * a_wgs) + b_wgs) / 3)


def probleme_direct(phi1, lambda1, azimuth_depart, distance):
    phi1_rad = m.radians(phi1)
    lambda1_rad = m.radians(lambda1)
    azimuth_depart_rad = m.radians(azimuth_depart)

    phi2 = m.sin(phi1_rad) * m.cos(sigma(distance)) + m.cos(phi1_rad) * m.sin(sigma(distance)) * m.cos(
        azimuth_depart_rad)
    phi2 = sym.asin(phi2)

    lambda2 = sym.cot(sigma(distance)) * sym.sin(sym.pi / 2 - phi1_rad) - sym.cos(sym.pi / 2 - phi1_rad) * sym.cos(
        azimuth_depart_rad)
    lambda2 /= sym.sin(azimuth_depart_rad)
    lambda2 = sym.acot(lambda2)

    lambda2 += lambda1_rad

    azimuth_retour = sym.cos(sigma(distance)) * sym.cos(azimuth_depart_rad) - sym.tan(phi1_rad) * sym.sin(sigma(distance))
    azimuth_retour /= sym.sin(azimuth_depart_rad)
    azimuth_retour = sym.acot(azimuth_retour)

    return m.degrees(phi2), m.degrees(lambda2), m.degrees(azimuth_retour)


def probleme_inverse(phi1, phi2, lambda1, lambda2):
    phi1_rad = m.radians(phi1)
    phi2_rad = m.radians(phi2)
    lambda1_rad = m.radians(lambda1)
    lambda2_rad = m.radians(lambda2)

    delta_lambda = m.fabs(lambda1_rad - lambda2_rad)

    s12 = sym.sin(phi1_rad) * sym.sin(phi2_rad) + sym.cos(phi1_rad) * sym.cos(phi2_rad) * sym.cos(delta_lambda)
    s12 = sym.acos(s12)

    a12 = ((sym.tan(phi2_rad) * sym.cos(phi1_rad)) / sym.sin(delta_lambda)) - sym.sin(phi1_rad) * sym.cot(delta_lambda)
    a12 = sym.acot(a12)

    a21 = ((sym.tan(phi1_rad) * sym.cos(phi2_rad)) / sym.sin(delta_lambda)) - sym.sin(phi2_rad) * sym.cot(delta_lambda)
    a21 = sym.acot(-a21)

    return m.degrees(a12), m.degrees(a21), s12


