from src.config import * 
import src.config

sheetName = '2023-DF-Tri'
pd.set_option('display.max_columns', None)
df = pd.read_excel(src.config.excel_path, sheet_name=sheetName)
df = df.loc[:, ["REF", "Indicateur", "Période", "Périmètre"]]
print(df)