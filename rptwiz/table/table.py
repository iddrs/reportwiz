# from abc import ABC, abstractmethod
# from typeguard import typechecked
# import pandas as pd
#
# @typechecked
# class TableBase(ABC):
#
#     def __init__(self, df: pd.DataFrame):
#         self.df = df
#
#     @abstractmethod
#     def save(self, filepath: str):
#         pass