from rptwiz.provider.provider import ExcelProvider, SQLProvider

# provider = ExcelProvider(r'C:\Users\Everton\Desktop\Prefeitura\PAD\2023-05\excel\BAL_DESP.xlsx')
# df = provider.get_data(usecols=['orgao', 'uniorcam', 'funcao', 'subfuncao'])

provider = SQLProvider(r'postgresql://postgres:lise890@localhost:5432/iddrs')
df = provider.get_data('SELECT orgao, dotacao_atualizada, valor_empenhado FROM pad."BAL_DESP"')
print(df.sample(10))