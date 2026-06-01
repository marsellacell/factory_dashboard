# Factory Production Dashboard (Sample Project)

This repository contains a self‑contained Django project that
demonstrates how to build a simple data dashboard using standard web
technologies—HTML5, CSS3, JavaScript (Chart.js) and Python.  The
dashboard reads production data from a local Excel file using
`pandas.read_excel()`, aggregates the results, and displays the
information in a tabular format alongside a bar chart and summary
statistics.

## Project goals

* Provide an uncomplicated example that undergraduate students can use
  during a **Software Testing** practicum to practise manual UI and
  GUI testing.
* Show how to integrate the Python ecosystem (Django, pandas) with
  front‑end libraries (Chart.js) without resorting to heavy
  frameworks like React or Vue.
* Keep the code modular so that each concern—data loading, filtering,
  view logic and presentation—is isolated in its own file.

## Directory structure

```
factory_dashboard/
├── manage.py                 # Django management script
├── data.xlsx                 # Dummy production dataset (Excel)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation (this file)
├── factory_dashboard/        # Project configuration package
│   ├── __init__.py
│   ├── settings.py           # Global Django settings
│   ├── urls.py               # Root URL routing
│   ├── asgi.py
│   └── wsgi.py
└── dashboard/                # Dashboard application
    ├── __init__.py
    ├── apps.py
    ├── urls.py               # App‑specific URL patterns
    ├── utils.py              # Helper functions for data loading and summarisation
    ├── views.py              # Views connecting HTTP requests to data processing
    ├── templates/
    │   └── dashboard/
    │       └── home.html     # HTML template for the dashboard
    └── static/
        └── dashboard/
            ├── css/
            │   └── style.css # Dashboard styling
            └── js/
                └── script.js # Placeholder for additional JavaScript
```

## Data source

The file **`data.xlsx`** lives in the project root and contains dummy
production records.  Each row has the following columns:

* `Date` – the date of production
* `Division` – factory division name (e.g., Assembly, Packaging, etc.)
* `Machine` – machine identifier
* `Production` – units produced on that day
* `MachineStatus` – status of the machine (Running, Stopped, Maintenance)

The sample dataset was generated programmatically using Python and
pandas.  Students may substitute their own Excel files as long as
they provide the same column names.

## Reading Excel with pandas

The dashboard uses the function [`pandas.read_excel()`] to load
the spreadsheet into a pandas `DataFrame`.  According to the official
pandas documentation, `read_excel()` accepts a path to an Excel file
and returns a DataFrame.  It supports various file formats (`.xls`,
`.xlsx`, `.xlsm`, `.xlsb`, `.odf`, `.ods`, `.odt`) and will
automatically select the correct engine when reading the file
【692949147086483†L127-L140】.  You can also specify sheet names,
headers and other options via keyword arguments.

In this project the helper function `load_data()` defined in
`dashboard/utils.py` calls `read_excel()` like this:

```python
file_path = settings.BASE_DIR / "data.xlsx"
df = pd.read_excel(file_path)
```

If the Excel file contains a column named **`Date`**, the helper
converts it to a proper `datetime64` type so that date filters work
correctly.  The docstring in `load_data()` explains the expected
columns and where the file should be placed.

## Request/Response flow

1. A user visits the root URL (`/`).  Django routes this request to
   `dashboard.views.dashboard_view()` via the URL pattern defined in
   `dashboard/urls.py` and `factory_dashboard/urls.py`.
2. The view calls `load_data()` to read **`data.xlsx`** into a
   DataFrame.
3. Query parameters `start_date`, `end_date` and `division` are
   extracted from `request.GET`.  The helper `filter_data()` applies
   these filters to the DataFrame, creating a new DataFrame with only
   the relevant rows.
4. The view computes summary statistics with `get_summary()` (total
   production and machine status counts) and groups data by date for
   charting via `get_chart_data()`.
5. The filtered records, summary and chart data are placed in a
   context dictionary and passed to the template `home.html`.
6. The template renders an HTML page that includes a filter form,
   summary section, bar chart and table of detailed records.  Chart.js
   is imported from a CDN, and the chart is instantiated using
   JavaScript embedded at the bottom of the page.  The documentation
   for Chart.js shows how to include the library using a `<script>` tag
   and create bar charts by specifying a `type` of `bar`, labels and
   datasets【960523207259154†L23-L43】.

Because the dashboard responds to GET parameters, users can apply
filters simply by selecting values and submitting the form.  Django
will regenerate the page with the updated context.

## Running the project locally

1. Install Python 3.10 or later and create a virtual environment.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run migrations (even though the project does not use a custom
   database model, Django requires minimal tables for sessions and
   authentication):
   ```sh
   python manage.py migrate
   ```
4. Start the development server:
   ```sh
   python manage.py runserver
   ```
5. Open a web browser and navigate to `http://127.0.0.1:8000/` to
   view the dashboard.

If you wish to test different data, replace **`data.xlsx`** with your
own file or change the path in `dashboard/utils.py`.  Ensure the
column names remain consistent.

## Extending the dashboard

The modular structure of this project makes it easy to extend:

* **Additional charts** – modify `get_chart_data()` to group by
  division or machine and pass multiple datasets to the template.
* **AJAX updates** – move the chart initialization code to
  `static/dashboard/js/script.js` and use JavaScript to fetch JSON
  endpoints for live updates without reloading the page.
* **Authentication** – enable Django’s authentication system to
  restrict access to the dashboard.

Feel free to experiment and adapt the project to your own needs.  The
source code is intentionally clear and thoroughly commented for
educational use.