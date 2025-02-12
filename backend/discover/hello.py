from src.pypi_query import PackageStatsExtractor
import datetime

# loadenv
from dotenv import load_dotenv

load_dotenv()


from sqlmodel import Session, SQLModel, create_engine

from src.config import settings
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    from google.cloud import bigquery

    client = bigquery.Client()
    viewer = PackageStatsExtractor(client)
    with Session(engine) as session:
        viewer.from_big_query_to_db(datetime.date(2023, 1, 1), session)
