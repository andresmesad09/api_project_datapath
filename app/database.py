import logging
from pathlib import Path
from sqlalchemy import create_engine, text
from .utils.config import Config
import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
from .utils.logger import create_logging

ENV_VARS = Config()
DB_USER = ENV_VARS.pg_user
DB_PWD = ENV_VARS.pg_pwd
DB_HOST = ENV_VARS.pg_host
DB_PORT = ENV_VARS.pg_port
DB = ENV_VARS.pg_db
DRIVER = 'postgresql+psycopg2'

SQLALCHEMY_URL = f"{DRIVER}://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB}"

try:
    logger = create_logging()
    logger.info("Logger was created")
except Exception:
    logging.error("Exception at creating logger", exc_info=True)


class Database:
    def __init__(self) -> None:
        self.engine = create_engine(SQLALCHEMY_URL)

    def connect(self):
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB,
            user=DB_USER,
            password=DB_PWD,
            # to include the columns in the results
            cursor_factory=RealDictCursor
        )
        return conn

    def income_by_department(self):
        query_path = Path().cwd() / "app" / "queries" / "income_by_dep.sql"
        with open(query_path, "r") as file:
            data = file.read()
        query = text(data)
        con = self.engine
        try:
            output_dataframe = pd.read_sql(query, con)
            res = output_dataframe.to_json(orient='records')
            return res
        except Exception:
            logger.error("Error in getting data", exc_info=True)
            raise Exception
        finally:
            con.dispose()

    def top_categories(self):
        query_path = Path().cwd() / "app" / "queries" / "top_categories.sql"
        with open(query_path, "r") as file:
            data = file.read()
        query = text(data)
        con = self.engine
        try:
            output_dataframe = pd.read_sql(query, con)
            res = output_dataframe.to_json(orient='records')
            return res
        except Exception:
            logger.error("Error in getting data", exc_info=True)
            raise Exception
        finally:
            con.dispose()

    def top_clients(self):
        query_path = Path().cwd() / "app" / "queries" / "top_clients.sql"
        with open(query_path, "r") as file:
            data = file.read()
        query = text(data)
        con = self.engine
        try:
            output_dataframe = pd.read_sql(query, con)
            res = output_dataframe.to_json(orient='records')
            return res
        except Exception:
            logger.error("Error in getting data", exc_info=True)
            raise Exception
        finally:
            con.dispose()

    def top_products(self):
        query_path = Path().cwd() / "app" / "queries" / "top_products.sql"
        with open(query_path, "r") as file:
            data = file.read()
        query = text(data)
        con = self.engine
        try:
            output_dataframe = pd.read_sql(query, con)
            res = output_dataframe.to_json(orient='records')
            return res
        except Exception:
            logger.error("Error in getting data", exc_info=True)
            raise Exception
        finally:
            con.dispose()

    def top_fraud(self):
        query_path = Path().cwd() / "app" / "queries" / "top_fraud.sql"
        with open(query_path, "r") as file:
            data = file.read()
        query = text(data)
        con = self.engine
        try:
            output_dataframe = pd.read_sql(query, con)
            res = output_dataframe.to_json(orient='records')
            return res
        except Exception:
            logger.error("Error in getting data", exc_info=True)
            raise Exception
        finally:
            con.dispose()
