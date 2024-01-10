import os
from dotenv import load_dotenv


class Env:
    def __init__(self):
        load_dotenv()

    @property
    def csv_path(self) -> str:
        return os.environ['CSV_PATH']
