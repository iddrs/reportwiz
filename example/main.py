import sys
sys.path.append('../')

from rptwiz.provider.provider import ExcelProvider

from charts import DespesaPorDepartamento


# Prepara os dados
provider = ExcelProvider('sample_data.xlsx')
df_depto = provider.get_data(sheet_name='Departamentos')
df_receita = provider.get_data(sheet_name='Receita')
df_despesa = provider.get_data(sheet_name='Despesa')

# Cria os gráficos
despesa_depto = DespesaPorDepartamento(df_depto)
