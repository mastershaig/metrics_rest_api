import csv
from io import StringIO

import requests
from django.core.management.base import BaseCommand
from metrics.models import MetricsModel


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Command started")
        r = requests.get(
            "https://gist.githubusercontent.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/raw/3c2a590b9fb3e9c415a99e56df3ddad5812b292f/dataset.csv",
        )
        f = StringIO(r.text)
        reader = csv.DictReader(f)
        for row in reader:
            MetricsModel.objects.get_or_create(
                date=row["date"],
                channel=row["channel"],
                country=row["country"],
                os=row["os"],
                impressions=row["impressions"],
                clicks=row["clicks"],
                installs=row["installs"],
                spend=row["spend"],
                revenue=row["revenue"],
            )
        print("Done")
