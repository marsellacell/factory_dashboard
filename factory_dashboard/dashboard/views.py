"""
Views for the factory dashboard application.

Views connect HTTP requests to Python code.  The dashboard view reads
the production data, applies filters supplied by the user, computes
summary statistics and chart data, and passes everything to the
template for rendering.  Separating data loading and transformation
into helper functions (see ``utils.py``) keeps the view concise.
"""
from __future__ import annotations

from django.shortcuts import render  # type: ignore
from django.http import HttpRequest, HttpResponse  # type: ignore

from .utils import load_data, filter_data, get_summary, get_chart_data


def dashboard_view(request: HttpRequest) -> HttpResponse:
    """Render the dashboard page.

    The view reads the production data from the Excel file and applies
    optional filters provided as GET parameters:

    - ``start_date``: inclusive start date (YYYY‑MM‑DD)
    - ``end_date``: inclusive end date (YYYY‑MM‑DD)
    - ``division``: division name

    The filtered data is then summarized, chart data is prepared, and
    both are sent to the template via the context dictionary.
    """
    # Load the full dataset once
    df = load_data()

    # Extract query parameters; default to empty strings when not provided
    start_date: str | None = request.GET.get("start_date") or None
    end_date: str | None = request.GET.get("end_date") or None
    division: str | None = request.GET.get("division") or None

    # Apply filters
    filtered_df = filter_data(df, start_date=start_date, end_date=end_date, division=division)

    # Prepare context data
    summary = get_summary(filtered_df)
    chart_data = get_chart_data(filtered_df, group_by="Date")

    # Unique divisions for the division filter drop‑down
    divisions = sorted(df["Division"].unique())

    context = {
        "data": filtered_df.to_dict("records"),
        "summary": summary,
        "chart_labels": chart_data["labels"],
        "chart_values": chart_data["values"],
        "divisions": divisions,
        "selected_start": start_date or "",
        "selected_end": end_date or "",
        "selected_division": division or "",
    }
    return render(request, "dashboard/home.html", context)