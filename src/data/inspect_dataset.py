
from pathlib import Path
import pandas as pd

# Chemin du projet
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "household_power_consumption.txt"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset introuvable : {DATA_PATH}"
        )

    print("=" * 60)
    print("SMART ENERGY — DATA INSPECTION")
    print("=" * 60)

    df = pd.read_csv(
        DATA_PATH,
        sep=";",
        na_values=["?"],
        low_memory=False
    )

    print("\n1. Dimensions :")
    print(f"Nombre de lignes : {df.shape[0]:,}")
    print(f"Nombre de colonnes : {df.shape[1]}")

    print("\n2. Noms des colonnes :")
    print(df.columns.tolist())

    print("\n3. Aperçu des données :")
    print(df.head())

    print("\n4. Types des colonnes :")
    print(df.dtypes)

    print("\n5. Valeurs manquantes :")
    print(df.isna().sum())

    print("\n6. Doublons :")
    print(df.duplicated().sum())

    print("\n7. Statistiques descriptives :")
    print(df.describe(include="all").T)

    print("\nInspection terminée.")


if __name__ == "__main__":
    main()
