import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load CSV file into DataFrame. Returns empty DataFrame on error."""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"load_data error: {e}")
        return pd.DataFrame()


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: copy, drop duplicates, drop rows that are completely NA,
    strip string columns."""
    if data is None or data.empty:
        return pd.DataFrame()
    df = data.copy()
    df = df.drop_duplicates()
    df = df.dropna(how="all")
    obj_cols = df.select_dtypes(include="object").columns
    for col in obj_cols:
        # convert to string, strip whitespace
        df[col] = df[col].astype(str).str.strip()
        # restore NAs introduced from "nan" strings
        df[col] = df[col].replace({"nan": pd.NA})
    return df


def normalize_yes_no_columns(data: pd.DataFrame) -> pd.DataFrame:
    """Normalize common yes/no-like text into 'yes'/'no'. Operates on object columns."""
    if data is None or data.empty:
        return pd.DataFrame()
    df = data.copy()

    def map_yes_no(x):
        if pd.isna(x):
            return pd.NA
        s = str(x).strip().lower()
        if s in ("yes", "y", "tak", "true", "1", "t"):
            return "yes"
        if s in ("no", "n", "nie", "false", "0", "f"):
            return "no"
        return x

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].apply(map_yes_no)
    return df


def clean_data_pipeline(file_path: str) -> pd.DataFrame:
    """Load -> clean -> normalize pipeline. Returns cleaned DataFrame or empty."""
    data = load_data(file_path)
    if data.empty:
        print("clean_data_pipeline: no data loaded")
        return pd.DataFrame()
    cleaned = clean_data(data)
    normalized = normalize_yes_no_columns(cleaned)
    return normalized


def save_data_cleaned(data: pd.DataFrame, output_file_path: str) -> None:
    """Save cleaned DataFrame to CSV."""
    if data is None or data.empty:
        print("save_data_cleaned: nothing to save")
        return
    try:
        data.to_csv(output_file_path, index=False)
        print(f"Dane zapisane do: {output_file_path}")
    except Exception as e:
        print(f"save_data_cleaned error: {e}")