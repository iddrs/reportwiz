from rptwiz.plot.chart import ChartBase
from pandas import Series
from typing import Tuple
from matplotlib.ticker import FuncFormatter
import random

class LineChart(ChartBase):
    invert = False

    def __init__(self, title: str = '', subtitle: str = '', figsize: Tuple[int, int] = (16, 9), theme=None):
        super().__init__(title=title, subtitle=subtitle, figsize=figsize, theme=theme)

    def build(self, x: Series, *yspec: dict) -> 'LineChart':
        super().build()
        for spec in yspec:
            y = spec['y']
            del spec['y']
            self.plt.plot(x, y, **spec)
        self.ax.set_frame_on(False)
        self.ax.xaxis.set_major_formatter(self.formatter_x)
        self.ax.yaxis.set_major_formatter(self.formatter_y)
        self.ax.set_xticks(x)
        self.ax.set_ylim(bottom=0)
        self.plt.legend(loc='best', ncol=len(yspec))
        # self.plt.grid(self.theme.line_grid)
        return self