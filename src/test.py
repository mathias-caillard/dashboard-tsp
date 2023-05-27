from config import * 
import config

sheetName = '2023-DF-Tri'
pd.set_option('display.max_columns', None)
df = pd.read_excel(config.excel_path, sheet_name=sheetName)
df = df.loc[:, ["REF", "Indicateur", "Période", "Périmètre"]]
print(df)