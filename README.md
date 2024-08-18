
General
-------
This repo is forked from https://github.com/DARcorporation/xfoil-python

Installing the Python Module
-----------------------------------------
1. Install Poetry
2. Run these commands in your terminal
```bash
poetry shell
poetry install
```
3. Make sure it was installed correctly
```bash
make test
```

Using
-----------------------------------------
```pycon
airfoil = load_airfoil("airfoil.txt")
a, cl, cd, cm, cp = run_xfoil(
    airfoil, alpha, reynolds_number, max_iter
)
```
