import sqlite3
import pandas as pd
from openpyxl import load_workbook
from sqlalchemy import create_engine


db = pd.read_excel(r'D:\Nivelamento\Planilhas.xlsx', sheet_name='Teste')
print(db)
