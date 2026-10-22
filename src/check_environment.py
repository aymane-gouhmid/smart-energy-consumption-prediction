
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import sklearn
import matplotlib
import seaborn
import streamlit
import fastapi
import pytest


def main():
    # Racine du projet
    project_root = Path(__file__).resolve().parent.parent

    print("=" * 55)
    print("SMART ENERGY CONSUMPTION PREDICTION")
    print("=" * 55)

    print(f"\nPython version : {sys.version.split()[0]}")
    print(f"Project root   : {project_root}")
    print(f"Python path    : {sys.executable}")

    print("\nInstalled libraries:")
    print(f"Pandas         : {pd.__version__}")
    print(f"NumPy          : {np.__version__}")
    print(f"Scikit-learn   : {sklearn.__version__}")
    print(f"Matplotlib     : {matplotlib.__version__}")
    print(f"Seaborn        : {seaborn.__version__}")
    print(f"Streamlit      : {streamlit.__version__}")
    print(f"FastAPI        : {fastapi.__version__}")
    print(f"Pytest         : {pytest.__version__}")

    required_dirs = [
        "data/raw",
        "data/processed",
        "notebooks",
        "src/data",
        "src/features",
        "src/models",
        "app",
        "tests",
        "reports",
    ]

    print("\nChecking project structure:")

    all_exist = True

    for folder in required_dirs:
        exists = (project_root / folder).is_dir()
        status = "OK" if exists else "MISSING"

        print(f"[{status}] {folder}")
        all_exist = all_exist and exists

    print("\n" + "=" * 55)

    if all_exist:
        print("SUCCESS: Environment is ready!")
    else:
        print("ERROR: Some folders are missing.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
