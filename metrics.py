"""Simple metrics helper functions file."""


from datetime import datetime


def initialize_metrics_lists() -> None:
    """Initializes our metrics lists. To be called when the website goes online."""
    metric_list_traffic: list[datetime] = []
    metric_list_downloads: list[datetime] = []


# Call this function when someone visits the website
def traffic_counter() -> None:
    """A function that records the date and time of the visit to the website in our metrics list for traffic."""
    metric_list_traffic.append(datetime.now())


# Call this funcion when someone downloads Cloudify
def download_counter() -> None:
    """A function that records the date and time of the download in our metrics list for downloads."""
    metric_list_downloads.append(datetime.now())


if __name__ == "__main__":
    initialize_metrics_lists()