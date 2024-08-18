from src.xfoil import XFoil
from typing import Any
from src.xfoil.model import Airfoil
from src.xfoil.test import naca0012


def run_xfoil(
    airfoil: Airfoil, alpha: float, reynolds_number: float, max_iter: int = 50
) -> Any:
    """
    Run XFoil with given airfoil, angle of attack, reynolds number, and maximum iterations.

    Args:
    airfoil (Airfoil): Airfoil object.
    alpha (float): Angle of attack in degrees.
    reynolds_number (float): Reynolds number.
    max_iter (int): Maximum number of iterations.

    Returns: simulation results from XFoil

    """
    xf = XFoil()
    xf.airfoil = airfoil
    xf.Re = reynolds_number
    xf.n_crit = 9
    xf.max_iter = max_iter

    return xf.aseq(alpha, alpha + 1, 1)


def main() -> None:
    airfoil = naca0012
    _ = run_xfoil(airfoil, 0, 1e7)
    return None


if __name__ == "__main__":
    main()
