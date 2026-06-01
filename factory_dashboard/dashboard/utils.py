"""
Utility functions for loading and processing production data.

These helper functions encapsulate common operations such as reading
the Excel data file, applying filters based on query parameters, and
computing summary statistics.  Keeping this logic in a separate module
makes the view simpler and easier to read.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import pandas as pd
from django.conf import settings  # type: ignore


def load_data() -> pd.DataFrame:
    """Load the factory production data from the Excel spreadsheet.

    Returns a pandas DataFrame with the following columns:

    - ``Date``: the date of production (converted to ``datetime64[ns]``)
    - ``Division``: the name of the factory division
    - ``Machine``: the machine identifier
    - ``Production``: number of units produced on that day
    - ``MachineStatus``: the status of the machine (e.g., Running, Stopped, Maintenance)

    The Excel file is located at ``BASE_DIR / 'data.xlsx'``.  If you place
    your data file elsewhere, update the path accordingly in this function.
    """
    file_path: Path = settings.BASE_DIR / "data.xlsx"
    df: pd.DataFrame = pd.read_excel(file_path)
    # Ensure that the Date column is parsed as datetime for comparison
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    return df


def filter_data(
    df: pd.DataFrame,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    division: Optional[str] = None,
) -> pd.DataFrame:
    """Return a filtered copy of the production data.

    Parameters
    ----------
    df : pandas.DataFrame
        The unfiltered DataFrame returned by :func:`load_data`.
    start_date : str, optional
        Inclusive start date in ``YYYY-MM-DD`` format.  If provided, only
        rows on or after this date are kept.
    end_date : str, optional
        Inclusive end date in ``YYYY-MM-DD`` format.  If provided, only
        rows on or before this date are kept.
    division : str, optional
        If provided, only rows belonging to this division are kept.

    Returns
    -------
    pandas.DataFrame
        A new DataFrame containing only the rows that satisfy the
        specified filters.  The original DataFrame is not modified.
    """
    filtered: pd.DataFrame = df.copy()
    # Apply date filters
    if start_date:
        filtered = filtered[filtered["Date"] >= pd.to_datetime(start_date)]
    if end_date:
        filtered = filtered[filtered["Date"] <= pd.to_datetime(end_date)]
    # Apply division filter
    if division:
        filtered = filtered[filtered["Division"] == division]
    return filtered


def get_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """Compute high‑level summary statistics for the filtered data.

    The summary includes the total number of units produced and a
    breakdown of machine statuses.

    Parameters
    ----------
    df : pandas.DataFrame
        The filtered production data.

    Returns
    -------
    dict
        A dictionary containing the total production and machine
        status counts.
    """
    total_production: int = int(df["Production"].sum()) if not df.empty else 0
    status_counts: Dict[str, int] = df["MachineStatus"].value_counts().to_dict()
    return {
        "total_production": total_production,
        "machine_status": status_counts,
    }


def get_chart_data(df: pd.DataFrame, group_by: str = "Date") -> Dict[str, Any]:
    """Prepare chart data for Chart.js based on the filtered DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The filtered production data.
    group_by : str, default 'Date'
        Column to group by.  When grouping by ``Date``, production totals
        are aggregated per day.  Other groupings (e.g., ``Division``) can
        be selected to generate different charts.

    Returns
    -------
    dict
        A dictionary with two keys: ``labels`` (x‑axis labels as a list of
        strings) and ``values`` (corresponding production totals as a list
        of integers).
    """
    if df.empty:
        return {"labels": [], "values": []}
    # Group the DataFrame and sum the production
    if group_by == "Date":
        grouped = df.groupby("Date")["Production"].sum().reset_index()
        labels = grouped["Date"].dt.strftime("%Y-%m-%d").tolist()
    else:
        grouped = df.groupby(group_by)["Production"].sum().reset_index()
        labels = grouped[group_by].astype(str).tolist()
    values = grouped["Production"].tolist()
    return {"labels": labels, "values": values}