
import logging
from .database import Database
from pathlib import Path
import pandas as pd
from .utils.column_details import COLUMNS

db = Database()


def populate_tables_with_csv():
    try:
        conn = db.engine
        data_folder = Path.cwd() / "app" / "data"
        list_of_files = data_folder.rglob('*')
        for file in list_of_files:
            df = pd.read_csv(
                file,
                encoding='ISO-8859-1',
                # nrows=100,  # TODO: Remove this line
                sep='|',
                header=None,
                names=list(COLUMNS[file.name].keys())
            )
            df.to_sql(
                name=file.name,
                con=conn,
                schema='public',
                if_exists='replace',
                index=False,
                dtype=COLUMNS[file.name],
                chunksize=5000,
                method='multi'
            )
    except Exception:
        logging.error('Error at populating the database', exc_info=True)
    finally:
        conn.dispose()
