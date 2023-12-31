from abc import ABC, abstractmethod
import io
import base64

import matplotlib.pyplot as plt
from typing import Tuple
from rptwiz.plot.theme import default
from rptwiz import VisualizationBase
from jinja2 import Template


class ChartBase(VisualizationBase):

    plt: plt = None
    theme: dict = default
    formatter_x = lambda x: str(x)
    formatter_y = lambda y: str(y)
    is_builded = False

    def __init__(self, title: str = '', subtitle: str = '', figsize: Tuple[int, int] = (8, 5), theme = None):
        self.title = title
        self.subtitle = subtitle
        self.plt = plt
        self.figsize = figsize
        if theme != None:
            self.theme = theme

    def set_formatter_x(self, fn: callable) -> 'ChartBase':
        self.formatter_x = fn
        return self

    def set_formatter_y(self, fn: callable) -> 'ChartBase':
        self.formatter_y = fn
        return self

    def build(self):
        self.fig, self.ax = plt.subplots(figsize=self.figsize, tight_layout=True, facecolor=self.theme.colors.face)
        if self.title != '':
            self.plt.suptitle(self.title, **self.theme.title)
        if self.subtitle != '':
            self.plt.title(self.subtitle, **self.theme.subtitle)
        self.is_builded = True

    def show(self):
        if not self.is_builded:
            self.build()
        self.plt.show()

    def savefig(self, filepath: str, **kwargs):
        if not self.is_builded:
            self.build()
        self.plt.savefig(filepath, **kwargs)


    def to_base64(self) -> bytes:
        if not self.is_builded:
            self.build()
        pic = io.BytesIO()
        self.plt.savefig(pic, format='png')
        pic.seek(0)
        return base64.b64encode(pic.read()).decode()

    def to_html(self, template: Template) -> str:
        if not self.is_builded:
            self.build()
        return template.render(b64str=self.to_base64())