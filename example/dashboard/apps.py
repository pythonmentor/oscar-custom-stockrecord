from oscar.apps.dashboard.apps import (
    DashboardConfig as CoreDashboardConfig,
)  # noqa


class DashboardConfig(CoreDashboardConfig):
    name = "example.dashboard"
