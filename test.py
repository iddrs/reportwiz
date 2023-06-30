import datetime

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from rptwiz.provider.provider import ExcelProvider, SQLProvider
from rptwiz.plot.bar import HorizontalBarChart
from rptwiz.plot.line import LineChart
from rptwiz.plot.theme import default as theme
import pandas as pd
import matplotlib.dates as mdates
from rptwiz.table.table import Table
from rptwiz.report.report import Report

def money_formatter(x, pos=0):
    if pd.isnull(x):
        return ''
    if x < 0.0:
        return f'({x:,.2f})'.replace(',', '_').replace('.', ',').replace('_', '.').replace('-', '')
    if x > 0.0:
        return f'{x:,.2f}'.replace(',', '_').replace('.', ',').replace('_', '.')
    if x == 0.0:
        return '-'

def month_name(data_base):
    return data_base.strftime('%b')

jinja_env = Environment(
    loader=PackageLoader('rptwiz.template.jinja'),
    autoescape=select_autoescape()
)

# provider = ExcelProvider(r'C:\Users\Everton\Desktop\Prefeitura\PAD\2023-05\excel\BAL_DESP.xlsx')
# df = provider.get_data(usecols=['orgao', 'uniorcam', 'funcao', 'subfuncao'])

provider = SQLProvider(r'postgresql://postgres:lise890@localhost:5432/iddrs')
df1 = provider.get_data('''SELECT 
                                nome_orgao, 
                                SUM(dotacao_atualizada) AS dotacao, 
                                SUM(valor_empenhado) AS empenhado 
                            FROM pad."BAL_DESP" 
                            GROUP BY nome_orgao 
                            ORDER BY dotacao DESC''')
# print(df.sample(10))

# hbar = HorizontalBarChart(title='Dotação por órgão', subtitle='em R$')
# hbar.set_invert_y(True).set_formatter_x(money_formatter).build(df1['dotacao'], df1['nome_orgao'])
# hbar.show()
# print(hbar.to_base64())

df2 = provider.get_data('''SELECT
                                data_base,
                                SUM(meta_mensal) AS previsto,
                                SUM(receita_realizada) AS arrecadado
                            FROM pad."RECEITA"
                            WHERE controle = 202305
                            GROUP BY data_base
                            ORDER BY data_base ASC''')
yprevista = dict(
    y=df2['previsto'],
    label='Prevista',
    color=theme.colors.grey,
    linestyle='--',
    marker='^'
)
yarrecadado = dict(
    y=df2['arrecadado'],
    label='Arrecadado',
    color=theme.colors.positive,
    # linestyle='--',
    marker='o'
)
line = LineChart(title='Receita', subtitle='valores mensais', figsize=(12, 7)).set_formatter_x(mdates.DateFormatter('%b/%Y')).set_formatter_y(money_formatter).build(df2['data_base'], yprevista, yarrecadado)\
# line.show()
# print(line.to_base64())
# html = line.to_html(jinja_env.get_template('plot_img.html'))

table = Table(df2, caption='Receita prevista e arrecadada', labels=dict(data_base='Mês', previsto='Previsão', arrecadado='Arrecadado'))
table.set_formatter('data_base', month_name)
table.set_formatter('previsto', money_formatter)
table.set_formatter('arrecadado', money_formatter)
table.build()
html = table.to_html(jinja_env.get_template('table.html'))

rpt = Report(env=dict(title='Relatório de teste', data_base='2023-05-31'), viz=dict(graf1=line.to_html(jinja_env.get_template('plot_img.html')), tab1=html))
jenv = Environment(
    loader=FileSystemLoader('.'),
    autoescape=None
)
tpl = jenv.get_template('example.html')
html = rpt.to_html(tpl, subtitulo='Teste', autor='Everton')
with open('test.html', 'w') as f:
    f.write(html)
opt = {
    'page-size': 'A4',
    'title': 'Relatório de teste',
    'orientation': 'Portrait'
}
rpt.to_pdf(html, 'test.pdf', options=opt)