from typing import Tuple
from rptwiz.plot.bar import HorizontalBarChart
from pandas import DataFrame, Series
import pandas as pd

def money_formatter(x, pos=0):
    if pd.isnull(x):
        return ''
    if x < 0.0:
        return f'({x:,.2f})'.replace(',', '_').replace('.', ',').replace('_', '.').replace('-', '')
    if x > 0.0:
        return f'{x:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.')
    if x == 0.0:
        return '-'

class DespesaPorDepartamento(HorizontalBarChart):

    def __init__(self, data: DataFrame) -> None:
        super().__init__(title='Maiores despesas por departamento', subtitle='R$ acumulado')
        self.set_invert_y(False)
        self.set_formatter_x(money_formatter)
        x, y = self.prepare(data)
        self.build(x=x, y=y)

    def prepare(self, data: DataFrame) -> Tuple[Series]:
        data = data.sort_values('executado_acum')
        return data['executado_acum'], data['departamento']