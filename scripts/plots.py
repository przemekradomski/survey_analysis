# python
import matplotlib.pyplot as plt
import pandas as pd
from typing import Optional, Iterable

def _ensure_column(data: pd.DataFrame, col: str) -> bool:
    if data is None or data.empty:
        print(f"plot: no data for column {col}")
        return False
    if col not in data.columns:
        print(f"plot: column '{col}' missing")
        return False
    return True


def plot_experience_distribution(data: pd.DataFrame) -> None:
    if not _ensure_column(data, "experience"):
        return
    series = data["experience"].dropna().astype(str).value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    series.plot(kind="bar")
    plt.title("Dystrybucja doświadczenia programistów")
    plt.xlabel("Lata doświadczenia")
    plt.ylabel("Liczba programistów")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_satisfaction_by_experience(data: pd.DataFrame) -> None:
    if not _ensure_column(data, "experience") or "satisfaction" not in data.columns:
        return
    df = data[["experience", "satisfaction"]].dropna()
    df["satisfaction"] = pd.to_numeric(df["satisfaction"], errors="coerce")
    grouped = df.groupby(df["experience"].astype(str))["satisfaction"].mean().sort_index()
    plt.figure(figsize=(10, 6))
    grouped.plot(kind="bar")
    plt.title("Średnia satysfakcja w zależności od doświadczenia")
    plt.xlabel("Doświadczenie")
    plt.ylabel("Średnia satysfakcja")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_salary_by_experience(data: pd.DataFrame) -> None:
    if not _ensure_column(data, "experience") or "salary" not in data.columns:
        return
    df = data[["experience", "salary"]].dropna()
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
    grouped = df.groupby(df["experience"].astype(str))["salary"].mean().sort_index()
    plt.figure(figsize=(10, 6))
    grouped.plot(kind="bar")
    plt.title("Średnia pensja w zależności od doświadczenia")
    plt.xlabel("Lata doświadczenia")
    plt.ylabel("Średnia pensja")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_data(data: pd.DataFrame, which: Optional[Iterable[str]] = None) -> None:
    """
    Convenience function used by `main.py`.
    - If `which` is None, shows all available plots.
    - `which` can be an iterable of: 'experience', 'satisfaction', 'salary'.
    """
    if data is None or data.empty:
        print("plot_data: no data to plot")
        return

    mapping = {
        "experience": plot_experience_distribution,
        "satisfaction": plot_satisfaction_by_experience,
        "salary": plot_salary_by_experience,
    }

    # Normalize which into a list of keys
    if which is None:
        keys = list(mapping.keys())
    else:
        if isinstance(which, str):
            keys = [which]
        else:
            keys = list(which)

    for key in keys:
        fn = mapping.get(key)
        if fn is None:
            print(f"plot_data: unknown plot key '{key}' - skipping")
            continue
        try:
            fn(data)
        except Exception as e:
            print(f"plot_data: error while plotting '{key}': {e}")
            # continue with other plots
