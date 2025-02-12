import datetime

from google.cloud.bigquery import Client

from sqlmodel import Field, Session, SQLModel


# from pepy.domain.pypi import StatsViewer, Result, Row

import datetime


class PackageDailyStat(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    package: str = Field(index=True)
    version: str
    date: datetime.date
    daily_downloads: int

class PackageStatsExtractor():
    TIMEOUT = 30
    PAGE_SIZE = 10000
    def __init__(self, client: Client):
        self.client = client

    def from_big_query_to_db(self, date: datetime.date, session: Session) -> None:
        QUERY = """
            SELECT file.project as package, file.version as version, count(*) AS daily_downloads
            FROM `bigquery-public-data.pypi.file_downloads`
            WHERE timestamp >= '{}' AND timestamp < '{}'
            GROUP BY file.project, file.version
            ORDER BY file.project
        """.format(
            date.strftime("%Y-%m-%d"), date + datetime.timedelta(days=1)
        )

        query_job = self.client.query(QUERY, location="US")
        query_job.result(self.TIMEOUT)
        destination = query_job.destination
        destination = self.client.get_table(destination)
        rows = self.client.list_rows(destination, page_size=self.PAGE_SIZE)
        for (i, row) in enumerate(rows):
            session.add(
                PackageDailyStat(
                    package=row.get("project"), daily_downloads=row.get("daily_downloads"),
                    version=row.get("version"), date=date
                )
            )
            # print every 10000 rows
            if i % 10000 == 0:
                print(f"Inserted {i} rows", end="\r")
        session.commit()

