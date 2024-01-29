import os

import pandas as pd
from .data_frame_model import DataFrameModel
from src.pkgs.clickup import Task


class File:
    def __init__(self, path: str) -> None:
        self.__path = path
        self.__header = DataFrameModel.get_header()
        self.__create_or_replace_file()

    def insert_cards_pack(self, cards: list[Task]) -> None:
        new_lines = [DataFrameModel.generate_new_line(card=card) for card in cards]
        data_frame_to_add: pd.DataFrame = pd.DataFrame(new_lines, columns=self.__header)
        data_frame_to_add.to_csv(self.__path, index=False, encoding='utf-8', mode='a', header=False)

    def __create_or_replace_file(self) -> None:
        dir_path = os.path.dirname(self.__path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        data_frame: pd.DataFrame = pd.DataFrame(columns=self.__header)
        data_frame.to_csv(self.__path, index=False, encoding='utf-8', mode='w')
