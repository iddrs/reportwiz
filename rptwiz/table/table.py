from abc import ABC, abstractmethod
from typing import Union, Optional
import pandas as pd
from rptwiz import VisualizationBase

class Table(VisualizationBase):

    totals: dict = dict()
    def __init__(self, df: pd.DataFrame, caption: Optional[str] = None, labels: Optional[dict] = None, formatters: Optional[dict] = None):
        self.df = df
        self.formatters = formatters
        self.labels = labels
        self.caption = caption

    def set_formatter(self, column: str, formatter: Union[callable, str]) -> 'TableBase':
        if column in self.formatters.keys():
            self.formatters[column] = formatter
            return self
        else:
            raise KeyError(column)
    def set_label(self, column: str, name: str) -> 'TableBase':
        if column in self.labels.keys():
            self.labels[column] = name
            return self
        else:
            raise KeyError(column)

    def set_total_columns(self, column: str, fn: Union[callable, str]) -> 'TableBase':
        if column in self.totals.keys():
            self.totals[column] = fn
            return self
        else:
            raise KeyError(column)

    def build(self, template) -> str:
        # constroi o html da tabela de acordo com o template
        return template