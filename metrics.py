"""Simple metrics helper functions file."""


from datetime import datetime
from flask import Flask


metric_list_traffic: list[datetime] = []
metric_list_downloads: list[datetime] = []

app = Flask(__name__)


@app.route("/")
def traffic_counter() -> None:
    metric_list_traffic.append(datetime.now())

@app.route("/") # TODO add URL for download
def download_counter() -> None:
    metric_list_downloads.append(datetime.now())