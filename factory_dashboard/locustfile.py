from random import choice

from locust import HttpUser, between, task

DIVISIONS = ["Assembly", "Logistics", "Packaging", "Quality"]
DATE_RANGES = [
    ("2026-03-01", "2026-03-15"),
    ("2026-03-16", "2026-03-31"),
    ("2026-04-01", "2026-04-15"),
    ("2026-04-16", "2026-04-30"),
]

class FactoryDashboardUser(HttpUser):
    wait_time = between(1, 3)

    @task(5)
    def open_dashboard(self):
        self.client.get("/", name="dashboard: all data")

    @task(3)
    def filter_by_division(self):
        self.client.get(
            "/",
            params={"division": choice(DIVISIONS)},
            name="dashboard: filter division",
        )

    @task(3)
    def filter_by_date_range(self):
        start, end = choice(DATE_RANGES)
        self.client.get(
            "/",
            params={"start_date": start, "end_date": end},
            name="dashboard: filter date range",
        )

    @task(2)
    def filter_combined(self):
        start, end = choice(DATE_RANGES)
        self.client.get(
            "/",
            params={
                "start_date": start,
                "end_date": end,
                "division": choice(DIVISIONS),
            },
            name="dashboard: combined filter",
        )