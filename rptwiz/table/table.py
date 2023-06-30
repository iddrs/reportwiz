from typing import Union, Optional
import pandas as pd
from rptwiz import VisualizationBase
from jinja2 import Template

class Table(VisualizationBase):

    data = None
    def __init__(self, df: pd.DataFrame, caption: Optional[str] = None, labels: Optional[dict] = dict(), formatters: Optional[dict] = dict()):
        self.df = df
        self.formatters = formatters
        self.labels = labels
        self.caption = caption

    def set_formatter(self, column: str, formatter: Union[callable, str]) -> 'Table':
        if column in self.df.columns:
            self.formatters[column] = formatter
            return self
        else:
            raise KeyError(column)
    def set_label(self, column: str, name: str) -> 'Table':
        if column in self.df.columns:
            self.labels[column] = name
            return self
        else:
            raise KeyError(column)

    def build(self) -> 'Table':
        data = self.df.copy()
        for col, fmt in self.formatters.items():
            data[col] = data[col].apply(fmt)
        self.data = data
        return self

    def to_html(self, template: Template) -> str:
        if self.data is None:
            self.build()
        data = self.data
        if self.caption == None:
            caption = None
        else:
            caption = self.caption
        labels = self.get_labels()
        return template.render(
            caption=caption,
            labels=labels,
            data=data
        )

    def get_labels(self) -> list:
        labels = []
        if len(self.labels) == 0:
            labels = self.df.columns
        else:
            for k in self.df.columns:
                if k in self.labels:
                    labels.append(self.labels[k])
                else:
                    labels.append(k)
        return labels