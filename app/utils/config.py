from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    def __init__(self):
        try:
            self.pg_host = os.getenv('PG_HOST')
            self.pg_db = os.getenv('PG_DB')
            self.pg_user = os.getenv('PG_USER')
            self.pg_pwd = os.getenv('PG_PASSWORD')
            self.pg_port = os.getenv('PG_PORT')
            self.api_url = os.getenv('API_URL')
        except Exception as e:
            print(f"Exception : {e} __init__() for constants class")
