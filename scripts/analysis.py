import pandas as pd
from typing import Optional, Dict, Any


def analyze_data(data: pd.DataFrame) -> Optional[Dict[str, Any]]:
    """Return basic statistics and correlation when columns exist.
    Returns None on error."""
    if data is None or data.empty:
        print("analyze_data: no data provided")
        return None

    result = {}
    try:
        if "age" in data.columns:
            result["mean_age"] = pd.to_numeric(data["age"], errors="coerce").mean()
            result["median_age"] = pd.to_numeric(data["age"], errors="coerce").median()
            result["age_distribution"] = data["age"].value_counts().sort_index()
        else:
            result["mean_age"] = None
            result["median_age"] = None
            result["age_distribution"] = pd.Series(dtype=int)

        if {"age", "satisfaction"}.issubset(data.columns):
            age_num = pd.to_numeric(data["age"], errors="coerce")
            sat_num = pd.to_numeric(data["satisfaction"], errors="coerce")
            # compute Pearson correlation, result may be NaN
            corr = age_num.corr(sat_num)
            result["age_satisfaction_correlation"] = corr
        else:
            result["age_satisfaction_correlation"] = None

        return result
    except Exception as e:
        print(f"analyze_data error: {e}")
        return None


def analyze_data_by_country(data: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Group statistics by country for selected numeric columns."""
    if data is None or data.empty:
        print("analyze_data_by_country: no data provided")
        return None
    if "country" not in data.columns:
        print("analyze_data_by_country: 'country' column missing")
        return None
    try:
        numeric_cols = []
        for c in ("age", "satisfaction", "salary"):
            if c in data.columns:
                numeric_cols.append(c)
        if not numeric_cols:
            print("analyze_data_by_country: no numeric columns to aggregate")
            return None
        agg_dict = {c: ["mean", "median", "count"] if c == "age" else "mean" for c in numeric_cols}
        grouped = data.groupby("country").agg(agg_dict)
        return grouped
    except Exception as e:
        print(f"analyze_data_by_country error: {e}")
        return None