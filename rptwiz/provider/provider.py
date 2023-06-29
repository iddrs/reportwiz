from abc import ABC, abstractmethod

import pandas as pd
from sqlalchemy import create_engine
from typeguard import typechecked


@typechecked
class ProviderBase(ABC):
    """Classe base abstrata para provedores de dados."""
    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        """Método abstrato para obter dados."""
        pass


@typechecked
class FileProvider(ProviderBase):
    """Classe para provedor de arquivos."""

    def __init__(self, filepath: str):
        """Inicializa o objeto com o caminho do arquivo.

        :param filepath: Caminho do arquivo.
        """
        self.filepath = filepath


@typechecked
class SQLProvider(ProviderBase):
    """Classe para provedor de SQL."""

    def __init__(self, *args, **kwargs):
        """Inicializa o objeto com os argumentos do motor de criação.

        :param args: Argumentos posicionais para create_engine.
        :param kwargs: Argumentos nomeados para create_engine.
        """
        self.con = create_engine(*args, **kwargs)

    def get_data(self, sql: str, **kwargs) -> pd.DataFrame:
        """Obtém dados de uma consulta SQL.

        :param sql: Consulta SQL.
        :param kwargs: Argumentos nomeados para read_sql.

        :return: DataFrame com os dados da consulta.
        """
        return pd.read_sql(sql, self.con, **kwargs)


@typechecked
class ExcelProvider(FileProvider):
    """Classe para provedor de arquivos Excel."""

    def __init__(self, filepath: str):
        """Inicializa o objeto com o caminho do arquivo Excel.

        :param filepath: Caminho do arquivo Excel.
        """
        super().__init__(filepath=filepath)

    def get_data(self, **kwargs) -> pd.DataFrame:
        """Obtém dados de um arquivo Excel.

        :param kwargs: Argumentos nomeados para read_excel.

        :return: DataFrame com os dados do arquivo Excel.
        """
        return pd.read_excel(self.filepath, **kwargs)


@typechecked
class CSVProvider(FileProvider):
    """Classe para provedor de arquivos CSV."""

    def __init__(self, filepath: str):
        """Inicializa o objeto com o caminho do arquivo CSV.

        :param filepath: Caminho do arquivo CSV.
        """
        super().__init__(filepath=filepath)

    def get_data(self, **kwargs) -> pd.DataFrame:
        """Obtém dados de um arquivo CSV.

        :param kwargs: Argumentos nomeados para read_csv.

        :return: DataFrame com os dados do arquivo CSV.
        """
        return pd.read_csv(self.filepath, **kwargs)


@typechecked
class ParquetProvider(FileProvider):
    """Classe para provedor de arquivos Parquet."""

    def __init__(self, filepath: str):
        """Inicializa o objeto com o caminho do arquivo Parquet.

        :param filepath: Caminho do arquivo Parquet.
        """
        super().__init__(filepath=filepath)

    def get_data(self, **kwargs) -> pd.DataFrame:
        """Obtém dados de um arquivo Parquet.

        :param kwargs: Argumentos nomeados para read_parquet.

        :return: DataFrame com os dados do arquivo Parquet.
        """
        return pd.read_parquet(self.filepath, **kwargs)
