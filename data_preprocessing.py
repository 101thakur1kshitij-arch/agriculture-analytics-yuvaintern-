"""Utility functions for the agriculture analytics project."""

from pathlib import Path
import pandas as pd

def load_csv(path):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)

def basic_quality_report(df):
    """Return basic data-quality information."""
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }
