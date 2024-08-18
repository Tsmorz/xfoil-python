from src.xfoil.xfoil import XFoil
from typing import Any
from src.xfoil.model import Airfoil
import pandas as pd
import matplotlib.pyplot as plt


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


def load_airfoil(filename: str, plot=True) -> Airfoil:
    """
    Load airfoil data from .dat file.

    Args:
    filename (str): File path of airfoil data.

    Returns: Airfoil object

    """
    coords = pd.read_csv(filename, sep=",", header=None).to_numpy()
    x, y = coords[:, 0], coords[:, 1]

    if plot:
        fig, ax = plt.subplots(1, 1, figsize=(8, 2))
        plt.plot(x, y)
        plt.title("Airfoil plot")
        plt.xlabel("x-coordinate")
        plt.ylabel("y-coordinate")
        ax.set_aspect("equal")
        plt.show()  # Display airfoil plot for verification
    return Airfoil(x, y)


def main() -> None:
    # Load airfoil data from file
    airfoil = load_airfoil("/data/sd7062.csv", plot=False)
    _ = run_xfoil(airfoil, 0, 2e5, max_iter=50)  # Run XFoil simulation with
    return None


if __name__ == "__main__":
    main()
