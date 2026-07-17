import sqlite3
import pandas as pd
from openpyxl import load_workbook
from sqlalchemy import create_engine


db = pd.read_excel('D:/Nivelamento/Planilha.xlsx', sheet_name='Sheet1')
print(db)
