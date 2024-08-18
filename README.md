
General
-------
This repo is forked from https://github.com/DARcorporation/xfoil-python

Installing the Python Module
-----------------------------------------
1. Install [Poetry](https://python-poetry.org/docs/)
2. ```bash
   git clone <this/repo>
   cd <into/the/repo>
   poetry shell
   poetry install
   make test
   ```

Using
-----------------------------------------
```pycon
airfoil = load_airfoil("airfoil.txt")  # still need to implement
a, cl, cd, cm, cp = run_xfoil(
    airfoil, alpha, reynolds_number, max_iter
)
```
