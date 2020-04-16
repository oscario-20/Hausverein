
import pandas as pd

aprt_name = 'wohnungen.xlsx'
jobs_name = 'aemtli.xlsx'

aprt_df = pd.read_excel(aprt_name)
jobs_df = pd.read_excel(jobs_name)

print(aprt_df)
