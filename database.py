from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

mysql_user = "root"
mysql_password = quote_plus("xxxx")
mysql_host = "localhost"
mysql_port = "3306"
mysql_database = "fastapi_db"

DATABASE_URL = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}"

#connecting the db though the create engine
engine = create_engine(DATABASE_URL)

#session - catching the data like addevent listener
sessionLocal = sessionmaker(autoflush=False, autocommit = False,bind=engine)
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

#base
Base = declarative_base()
