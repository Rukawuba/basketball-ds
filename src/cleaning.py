import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV into a DataFrame."""
    return pd.read_csv(path)

def add_pts_per_min(df: pd.DataFrame) -> pd.DataFrame:
    """Add a points-per-minute column safely."""
    df = df.copy()
    df["pts_per_min"] = df["pts"] / df["min"].replace(0, pd.NA)
    return df
