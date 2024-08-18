from argparse import ArgumentParser
from src.xfoil.xfoil import XFoil
from utils.xfoil_utils import load_airfoil
import matplotlib.pyplot as plt


def main() -> None:
    parser = ArgumentParser(
        prog="XFoil", description="Run XFoil simulation on a given airfoil."
    )
    parser.add_argument("airfoil", type=str, help="Path to airfoil data file (.csv)")
    parser.add_argument("alpha", type=float, help="Angle of attack in degrees")
    parser.add_argument(
        "--max_iter", type=int, default=50, help="Maximum number of iterations"
    )
    parser.add_argument(
        "--plot", action="store_true", help="Plot airfoil", default=True
    )
    args = parser.parse_args()

    xf = XFoil()
    xf.airfoil = load_airfoil(args.airfoil, plot=args.plot)
    xf.Re = 2e5
    xf.n_crit = 9
    xf.max_iter = 150
    step = 0.25
    a, cl, cd, cm, cp = xf.aseq(-9, 19, step)

    plt.plot(a, cl)
    plt.xlabel("Angle of Attack (degrees)")
    plt.ylabel("Lift Coefficient (CL)")
    plt.grid()
    plt.show()
    return None


if __name__ == "__main__":
    main()
