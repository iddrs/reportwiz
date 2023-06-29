from rptwiz.plot.chart import ChartBase
from pandas import Series
from typeguard import typechecked, Tuple


@typechecked
class HorizontalBarChart(ChartBase):
    invert = False

    def __init__(self, title: str = '', subtitle: str = '', figsize: Tuple[int, int] = (16, 9), theme=None):
        super().__init__(title=title, subtitle=subtitle, figsize=figsize, theme=theme)
        self.formatter_x = lambda x: str(x)

    def set_invert_y(self, invert: bool) -> 'HorizontalBarChart':
        self.invert = invert
        return self

    def build(self, x: Series, y: Series) -> 'HorizontalBarChart':
        super().build()
        self.plt.barh(y, x, left=0, **self.theme.barh1)
        if self.invert:
            self.ax.invert_yaxis()
        for i, v in enumerate(x):
            self.ax.text(v, i, '  ' + self.formatter_x(v), **self.theme.barh_labels)
        self.ax.set_xticks([])
        self.ax.tick_params(left=False)
        self.ax.set_frame_on(False)
        return self
