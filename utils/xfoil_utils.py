from xfoil import XFoil
from typing import List


def run_xfoil(airfoil, alpha: float, reynolds_number: float, max_iter: int) -> List:
    xf = XFoil()
    xf.airfoil = airfoil
    xf.Re = reynolds_number
    xf.max_iter = max_iter

    a, cl, cd, cm, cp = xf.aseq(alpha, alpha + 1, 1)

    return xf.aseq(alpha, alpha + 1, 1)
